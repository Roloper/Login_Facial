import cv2
import os
import numpy as np
#import mysql.connector
from config import config
from models.ModelUser import ModelUser
from models.entities.Usuario import User

development_config = config['development']

def train_face_recognizer():
    #dataPath = './Data'
    #peopleList = os.listdir(dataPath)
    peopleList = ModelUser.get_all_users() # peopleList = users
    print('Lista de personas:', peopleList)

    labels = []
    facesData = []
    label = 0

    for nameDir in peopleList:
        #personPath = dataPath + '/' + nameDir
        print('Leyendo las imágenes')

        for fileName in os.listdir(personPath):
            print('Rostros:', nameDir + '/' + fileName)
            labels.append(label)
            facesData.append(cv2.imread(personPath + '/' + fileName, 0))
        label = label + 1

    face_recognizer = cv2.face.LBPHFaceRecognizer_create()

    print("Entrenamiento")
    face_recognizer.train(facesData, np.array(labels))


    # Guardar el modelo en la columna imagen_test de la tabla Usuario
    #cursor = conexion.cursor()
    face_recognizer.save('modeloLBPHFace.xml')
    with open('modeloLBPHFace.xml', 'rb') as archivo:
        modeloBytes = archivo.read()

    #cursor.execute("UPDATE Usuario SET imagen_test = %s WHERE id_usuario = 1", (modeloBytes,))
    # conexion.commit()

    print("Modelo Listo")

# conexion.close()
    face_recognizer.write('modeloLBPHFace.xml')
    print("Modelo Listo")

