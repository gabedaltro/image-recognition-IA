import face_recognition as fr

def reconhece_face(foto):
	foto = fr.load_image_file(foto)
	rostos = fr.face_encodings(foto)
	if (len(rostos) > 0):
		return True, rostos
	
	return False, []

def recupera_rostos():
	rostos_conhecidos = []
	nome_dos_rostos = [] 

	teste = reconhece_face("./images/teste.png")
	if(teste[0]):
		rostos_conhecidos.append(teste[1][0])
		nome_dos_rostos.append("Nome do rosto")


	return rostos_conhecidos, nome_dos_rostos
