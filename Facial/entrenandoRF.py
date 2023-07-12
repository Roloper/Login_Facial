import cv2
import os
import numpy as np
#import mysql.connector
from config import config
from models.ModelUser import ModelUser
from models.entities.Usuario import User

development_config = config['development']

def train_face_recognizer():
    dataPath = './Data'
    peopleList = os.listdir(dataPath)
    peopleList = ModelUser.get_all_users() 
    print('Lista de personas:', peopleList)

    labels = []
    facesData = []
    label = 0

    for nameDir in peopleList:
        personPath = dataPath + '/' + nameDir
        print('Leyendo las imágenes')

        for fileName in os.listdir(personPath):
            print('Rostros:', nameDir + '/' + fileName)
            labels.append(label)
            facesData.append(cv2.imread(personPath + '/' + fileName, 0))
        label = label + 1

    face_recognizer = cv2.face.LBPHFaceRecognizer_create()

    print("Entrenamiento")
    face_recognizer.train(facesData, np.array(labels))

    face_recognizer.save('modeloLBPHFace.xml')
    with open('modeloLBPHFace.xml', 'rb') as archivo:
        modeloBytes = archivo.read()

    print("Modelo Listo")

    face_recognizer.write('modeloLBPHFace.xml')
    print("Modelo Listo")

"""
import cv2
import os
import numpy as np
from config import config
from models.ModelUser import ModelUser
from app import db

def train_face_recognizer():
    try:
        users = ModelUser.get_all_users(db) #En Modeluser, esta funcion necesita dos parametros no se cuales son :´v, por eso no compila
        labels = []
        facesData = []

        for user in users:
            if not user[3]: #aqui el not funciona como un false
                labels.append(user[0])#aqui se coloca el id en labels []
                face_image = cv2.imdecode(np.frombuffer(user[5], np.uint8), cv2.IMREAD_GRAYSCALE) #
                facesData.append(face_image) #ahora a facesData, se le pasa la  fotos

        face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        face_recognizer.train(facesData, np.array(labels)) #aqui se entrena

        # Aqui se guardae en el archivo  q descargamos
        face_recognizer.save('modeloLBPHFace.xml')
        print("Modelo entrenado y guardado correctamente")

    except Exception as ex:
        print("Error: ", ex)

train_face_recognizer()

#Conclusion esta casi igual, a diferencia de label+1, y que no se q ponerle en los parametros de cls, y db
"""
