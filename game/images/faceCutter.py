from PIL import Image

# Carregar a imagem (substitua o caminho pela localização do seu arquivo de imagem)
img_path = './chars/michael/michael.png'
img = Image.open(img_path)

# Dimensões da imagem
img_width, img_height = img.size

# Número de rostos na imagem (ajuste conforme necessário)
num_faces = 4

# Calcula a largura de cada rosto
face_width = img_width // num_faces

# Lista para armazenar cada rosto cortado
face_images = []

# Loop para cortar cada rosto e salvá-los separadamente
for i in range(num_faces):
    # Define a área de corte para cada rosto
    left = i * face_width
    right = left + face_width
    face_img = img.crop((left, 0, right, img_height))  # Corta a imagem
    
    # Adiciona o rosto cortado à lista
    face_images.append(face_img)
    
    # Salva o rosto como imagem separada
    face_img.save(f'michael_{i + 1}.png')

print("Rostos separados e salvos com sucesso!")
