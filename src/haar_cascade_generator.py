import cv2
import os
import glob

# Carregar o classificador Haar Cascade para detecção de faces
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')

# Definir o caminho do diretório onde estão as imagens
caminho_diretorio = 'multipie/'

with open('train.txt', 'r') as fileAux:
  for line in fileAux.readlines():

    with open('output/haar_cascade.txt', 'a') as file:
      # Iterar por todas as imagens no diretório
      arquivo_imagem = caminho_diretorio + line.split()[0]
      # Carregar a imagem
      image = cv2.imread(arquivo_imagem)
      width, height = image.shape[:2]

      # Verificar se a imagem foi carregada corretamente
      if image is not None:
          image = cv2.resize(image, (224, 224))
          flipped_image = cv2.flip(image, 1)
          gray_image = cv2.cvtColor(flipped_image, cv2.COLOR_BGR2GRAY)
          faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.01, minSize=(50, 50)  )
          if len(faces) == 0:
            print("Rosto não encontrado: " + arquivo_imagem)
          elif len(faces) > 1:
            print("Mais de um rosto encontrado: " + arquivo_imagem)
          else:
            for (x, y, w, h) in faces:
                file.write(arquivo_imagem + ',' + str(x) + ',' + str(y) + ',' + str(w) + ',' + str(h) + '\n')

      else:
          print(f"Não foi possível carregar a imagem: {arquivo_imagem}")