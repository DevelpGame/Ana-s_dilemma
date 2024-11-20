from PIL import Image

# Carregar a imagem (substitua o caminho pela localização do seu arquivo de imagem)
base_path = 'chars/michael/'
input_image = f'{base_path}michael_vhappy.png'

img = Image.open(input_image)

# Dimensões da imagem
img_width, img_height = img.size

# Número de rostos na imagem (ajuste conforme necessário) ## 1 para cortar a altura
num_faces = 1

# Calcula a largura de cada rosto
face_width = img_width // num_faces

# Lista para armazenar cada rosto cortado
face_images = []

# Loop para cortar cada rosto e salvá-los separadamente
for i in range(num_faces):
    # Define a área de corte para cada rosto
    left = i * face_width
    right = left + face_width
    face_img = img.crop((left, 0, right, (img_height// 2 )))  # Corta a imagem
    
    # Adiciona o rosto cortado à lista
    face_images.append(face_img)
    
    # Salva o rosto como imagem separada
    face_img.save(f'{base_path}michael_{i + 1}.png')

print("Rostos separados e salvos com sucesso!")
