import cv2
import dlib
import imutils
from imutils import face_utils

# Carregar o modelo Haar Cascade para detecção de faces
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_profileface.xml")

predictor = dlib.shape_predictor('./predictor.dat')
# Carregar o modelo LBF para landmarks
#facemark = cv2.face.createFacemarkAAMmarkLBF()
#facemark.loadModel("predictor.dat")  # Certifique-se de que o arquivo lbfmodel.yaml esteja no caminho correto

# Carregar a imagem
image = cv2.imread("1719.jpg")
image = imutils.resize(image, width=500) 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.01, minSize=(50, 50) )

# Loop sobre as detecções de rostos
for (x, y, w, h) in faces:
    # Criar um retângulo dlib a partir das coordenadas do OpenCV
    rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))
    
    # Prever os pontos de landmarks faciais usando o preditor dlib
    shape = predictor(gray, rect)
    shape = face_utils.shape_to_np(shape)  # Converter os pontos para array NumPy
    
    # Desenhar os landmarks faciais na imagem
    for (x, y) in shape:
        cv2.circle(image, (x, y), 2, (0, 255, 0), -1)

    # Desenhar o retângulo do rosto detectado
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Exibir a imagem com os landmarks faciais
cv2.imshow("Landmarks Faciais", image)
cv2.waitKey(0)
cv2.destroyAllWindows()