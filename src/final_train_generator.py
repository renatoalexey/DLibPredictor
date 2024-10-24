import os

file_treino = "treino.txt"
file_haar = "output/haar_cascade.txt"

haar_cascade = {}

with open(file_haar, 'r') as file:
  lines_haar = file.readlines()
  for line in lines_haar:
    teste = line.split(',')
    haar_cascade[teste[0]] = [teste[1], teste[2], teste[3], teste[4]]

with open(file_treino, 'r') as file:
  lines_treino = file.readlines()
  for line in lines_treino:
    values = line.split()
    #print(values[0])
    cascade_values = haar_cascade.get(f'multipie/{values[0]}')
    #print(cascade_values)
    if cascade_values is not None:
      #print(haar_cascade.get(values[0]))
      cascade_values[3] = cascade_values[3].replace('\n', '')
      with open("final_train.txt", "a") as file:
        line_write = f"{values[0]} {' '.join(list(cascade_values))} {' '.join(values[1:])} \n"
        file.write(line_write)