import face_recognition as fr
from engine import reconhece_face, recupera_rostos

desconhecido = reconhece_face("./images/desconhecido.png")

if(desconhecido[0]):
    rosto_desconhecido = desconhecido[1][0]
    rostos_conhecidos, nome_dos_rostos = recupera_rostos()
    resultados = fr.compare_faces(rostos_conhecidos, rosto_desconhecido)
    print(resultados)

    for i in range (len(nome_dos_rostos)):
        resultado = resultados[i]
        if(resultado):
            print("Rosto reconhecido: ", nome_dos_rostos[i])
            break

else:
    print("Rosto não reconhecido")