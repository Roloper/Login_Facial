from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from config import config
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user #_-----
from werkzeug.utils import secure_filename
from datetime import datetime
import os
import requests

# Models
from models.ModelUser import ModelUser

# Entities
# from models.entities.Producto import Producto
# from models.entities.Publicacion import Publicacion
# from models.entities.User import User

#------------------------------
app = Flask(__name__, template_folder='template')
csrf = CSRFProtect()
db = MySQL(app)
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
    return render_template('index.html')

@app.route('/mision')
def mision():
    return render_template('mision.html')

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/vendedores')
def vendedores():
    return render_template('vendedores.html')
@app.route('/ventas')
def ventas():
    return render_template('ventas.html')
@app.route('/productos')
def productos():
    return render_template('productos.html')


# URL PARA EL LOGIN
@app.route('/login', methods=['GET', 'POST'])  # persona o empresa
def login():
    if request.method == 'POST':
        user = User(0, 0, request.form['a_username'], request.form['a_password'], 0, 0, 0, 0, 0)
        logged_user = ModelUser.login(db,user)

        if logged_user != None:
            if logged_user.a_password:
                login_user(logged_user)
                return redirect(url_for('Home'))
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

# url de home para pagina principal
@app.route('/Home')
@login_required
def Home():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'imagen' not in request.files:
            print('No file part')
            flash('No file part')
            return redirect(request.url)
        file = request.files['imagen']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            print('No selected part')
            flash('No selected file')
            return redirect(request.url)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        publi = Publicacion(
            None,
            current_user.id_usuario,
            request.form['titulo'],
            request.form['contenido'],
            filename,
        )
        print("todo bien")
        try:
            ModelPublicaciones.create_publicacion(db, publi)
            print("todo bien x2")
            return redirect(url_for('home'))

        except Exception as ex:
            return str(ex)

    else:
        sugeridos = ModelUser.get_no_amigos(db, current_user.id_usuario)
        publicaciones_amigos = ModelPublicaciones.get_publicaciones_amigos(db, current_user.id_usuario)
        all = ModelUser.get_all_users(db)
        return render_template('home.html', sugeridos=sugeridos, publicaciones_amigos=publicaciones_amigos, all = all)




@app.route('/connect/<int:user_id>', methods=['POST'])
@login_required
def connect(user_id):
    # Enviar solicitud de conexión
    ModelUser.enviar_solicitud(db,current_user.id_usuario, user_id)
    flash('Se ha enviado una solicitud de conexión al usuario.')
    return redirect(url_for('Home'))

@app.route('/perfil', methods=['GET','POST'])
@login_required
def perfil():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'imagen' not in request.files:
            print('No file part')
            flash('No file part')
            return redirect(request.url)
        file = request.files['imagen']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            print('No selected part')
            flash('No selected file')
            return redirect(request.url)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        publi = Publicacion(
            None,
            current_user.id_usuario,
            request.form['titulo'],
            request.form['contenido'],
            filename,
        )
        print("todo bien")
        try:
            ModelPublicaciones.create_publicacion(db, publi)
            print("todo bien x2")
            return redirect(url_for('perfil'))

        except Exception as ex:
            return str(ex)

    else:

        solicitudes = ModelUser.get_solicitudes(db, current_user.id_usuario)
        publicaciones = ModelPublicaciones.get_publicaciones_usuario(db, current_user.id_usuario)
        return render_template('perfil/perfil.html',publicaciones=publicaciones, solicitudes = solicitudes)

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
