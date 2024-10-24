from PIL import Image
import os
import xml.etree.ElementTree as ET


# Função para adicionar indentação ao XML
def indent(elem, level=0):
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

file_path = "final_train.txt"

# Create the root element
root = ET.Element("dataset")
images_element = ET.SubElement(root, "images")

images_path = "multipie"

if os.path.exists(file_path):
  with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
      full_line = line.split()
      imagem = Image.open(f"{images_path}/{full_line[0]}")

      top, left, width, height = full_line[1:5]

      # Obter a largura e altura da imagem
      width, height = imagem.size

      fiducial_points = full_line[5:]
      #print(fiducial_points)

      image_element = ET.SubElement(images_element, "image")
      image_element.set("file", f"{images_path}/{str(full_line[0])}")
      image_element.set("width", str(width))
      image_element.set("height", str(height))

      box_element = ET.SubElement(image_element, "box")
      box_element.set("top", str(top))
      box_element.set("left", str(left))
      box_element.set("width", str(width))
      box_element.set("height", str(height))

      fiducial_pairs = [fiducial_points[i: i + 2] for i in range(0, len(fiducial_points), 2)]
      #print(fiducial_pairs)

      count = 0
      for pair in fiducial_pairs:
        part_element = ET.SubElement(box_element, "part")
        part_element.set("name", str(count))
        part_element.set("x", str(round(float(pair[0]))))
        part_element.set("y", str(round(float(pair[1]))))
        count += 1

  # Create a tree structure and write to an XML file
  indent(root)
  tree = ET.ElementTree(root)
  with open("training_with_face_landmarks.xml", "wb") as fh:
      tree.write(fh, encoding='utf-8', xml_declaration=True)

  print("XML file 'training_with_face_landmarks.xml' generated successfully!")

else:
  print(f"O arquivo '{file_path}' não existe.")