import numpy as np
import face_recognition as fr
import cv2
from engine import recupera_rostos

rostos_conhecidos, nome_dos_rostos = recupera_rostos()

video_capture = cv2.VideoCapture(0)
while True:
    ret, frame = video_capture.read()

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    localizacao_dos_rostos = fr.face_locations(rgb_frame)
    rosto_desconhecidos = fr.face_encodings(rgb_frame, localizacao_dos_rostos)

    for (top, right, bottom, left), rosto_desconhecido in zip(localizacao_dos_rostos, rosto_desconhecidos):
        resultados = fr.compare_faces(rostos_conhecidos, rosto_desconhecido)
        print (resultados)
        
        face_distances = fr.face_distance(rostos_conhecidos, rosto_desconhecido)

        melhor_resultado = np.argmin(face_distances)
        if resultados[melhor_resultado]:
            nome = nome_dos_rostos[melhor_resultado]
        else:
            nome = "Desconhecido"

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX

        cv2.putText(frame, nome, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imshow('Webcam', frame)

    if cv2.waitKey(1)==27:
        break

video_capture.release()
cv2.destroyAllWindows()