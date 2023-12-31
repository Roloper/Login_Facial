#Librerias
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory, Response
from config import config
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user #_-----
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from Facial import facial

#Facial
#from Facial.facial import generate

# Models
from models.ModelUser import ModelUser

# Entities
from models.entities.Usuario import User
# from models.entities.Producto import Producto
# from models.entities.Publicacion import Publicacion
# from models.entities.User import User

#------------------------------
app = Flask(__name__, template_folder='template')
csrf = CSRFProtect()

db = MySQL(app)
nom = ''
login_manager_app = LoginManager(app)
app.config['UPLOAD_FOLDER'] = 'static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'NEF'}
#----

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@login_manager_app.user_loader
def load_user(id_usuario):
    return ModelUser.get_by_id(db, id_usuario)

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config['UPLOAD_FOLDER'], name)

#--------
#--------------------------
# URL PRINCIPAL
@app.route('/')
def index():
    return redirect(url_for('login'))

#RUTAS ADMINISTRADOR

@app.route('/index', methods=['GET'])
def home_admin():
    cur = db.connection.cursor()

    cur.execute("SELECT * FROM usuario WHERE admin = 0")

    vendedores = cur.fetchall()

    print(cur)

    insertObject = []
    columnNames = [column[0] for column in cur.description]
    for record in vendedores:
        insertObject.append(dict(zip(columnNames, record)))
    cur.close()

    return render_template('index.html', vendedores = insertObject)

@app.route('/vendedores')
def vendedores():
    return render_template('vendedores.html')


@app.route('/registro-vendedor', methods=['GET', 'POST'])
def registroVendedor():
    global nom
    if request.method == 'POST':
        nom = request.form['nombre']
        dataPath = './Data'
        personPath = dataPath + '/' + request.form['nombre']
        if not os.path.exists(personPath):
            print('Carpeta creada:', personPath)
            os.makedirs(personPath)
        print("----bien post")
        print(request.form['nombre'] + request.form['correo'] + request.form['password'])
        user = User(None, request.form['nombre'], request.form['correo'], User.hash_password(request.form['password']),
                    0, None, personPath)
        try:
            ModelUser.register(db, user)
            return render_template('grabar_cara.html')
        except Exception as ex:
            return str(ex)
    else:
        return render_template('administrador-registra-vendedor.html')


@app.route('/grabar-cara')
def grabarCara():
    return render_template('grabar_cara.html')

@app.route('/registro-completo', methods = ['GET'])
def registroCompletoCara():
    
    cur = db.connection.cursor()

    cur.execute("SELECT * FROM usuario ORDER BY id_usuario DESC LIMIT 1")

    nuevoRegistro = cur.fetchone()
    
    
    columnNames = [column[0] for column in cur.description]
    
    cur.close()

    insertObject = dict(zip(columnNames, nuevoRegistro))
    
    return render_template('administrador-registra-vendedor-completo.html', nuevoRegistro = insertObject)


#RUTAS VENDEDORES

@app.route('/verificacion')
def verificacion():
    return render_template('verificacion.html')

@app.route('/indexUsuario')
def home_ven():
    return render_template('indexUsuario.html')

@app.route('/ventas')
def ventas():
    return render_template('ventas.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')


@app.route('/mision')
def mision():
    return render_template('mision.html')


#RUTAS VIDEO

@app.route("/video_feed")
def video_feed():
     return Response(facial.generate(),
          mimetype = "multipart/x-mixed-replace; boundary=frame")


@app.route("/video_register")
def video_register():
     global nom
     return Response(facial.register(nom),
          mimetype = "multipart/x-mixed-replace; boundary=frame")

# URL PARA EL LOGIN
@app.route('/login', methods=['GET', 'POST'])  # persona o empresa
def login():
    if request.method == 'POST':
        user = User(0, 0, request.form['correo'], request.form['password'], 0)
        logged_user = ModelUser.login(db,user)
        if logged_user != None:
            if logged_user.password and (logged_user.admin == True):
                login_user(logged_user)
                return redirect(url_for('home_admin'))
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('verificacion'))
            else:
                print("contra incorrecta")
                flash("Contraseña Incorrecta")
                return render_template('login.html')
        else:
            print("No se encontro usuario")
            flash("Usuario no encontrado")
            return render_template('login.html')
    else:
        return render_template('login.html')

#___________________________________________

# URL DEL REGISTRO-
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        img_filename = ''
        if 'a_imagenperfil' in request.files:
            file = request.files['a_imagenperfil']
            if file.filename != '':
                img_filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))

        user = User(
            None,
            request.form['a_name'],
            request.form['a_username'],
            User.hash_password(request.form['a_password']),
            request.form['a_email'],
            request.form['a_descripcion'],
            request.form['a_celular'],
            request.form['a_ubicacion'],
            img_filename
        )
        try:
            ModelUser.register(db, user)
            return redirect(url_for('login'))

        except Exception as ex:
            return str(ex)

    else:
        return render_template('register.html')
#--------------------

# Redireccion para el cierre de sesion
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

#@login_required

def status_401(error):
    return redirect(url_for('index'))


def status_404(error):
    return "<h1> Pagina no encontrada </h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
