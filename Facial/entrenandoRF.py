import cv2
import os
import numpy as np
#import mysql.connector
from config import config
development_config = config['development']

# conexion = mysql.connector.connect(
#     host=development_config.MYSQL_HOST,
#     user=development_config.MYSQL_USER,
#     password=development_config.MYSQL_PASSWORD,
#     database=development_config.MYSQL_DB
# )
def train_face_recognizer():
    dataPath = './Data'
    peopleList = os.listdir(dataPath)
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

