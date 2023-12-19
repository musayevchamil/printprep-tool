from PIL import Image

# Chemins de vos images
image_path_face1 = "path/to/face1.jpg"  # Remplacez par le chemin de la première face
image_path_face2 = "path/to/face2.jpg"  # Remplacez par le chemin de la seconde face

# Charger les images
face1 = Image.open(image_path_face1)
face2 = Image.open(image_path_face2)

# Dimensions et résolution
dpi = 300
width_cm = 8.5
height_cm = 5.4
width_px = int(width_cm / 2.54 * dpi)
height_px = int(height_cm / 2.54 * dpi)

# Redimensionner les images
resized_face1 = face1.resize((width_px, height_px))
resized_face2 = face2.resize((width_px, height_px))

# Créer un fond A4
a4_width_px = int(21 / 2.54 * dpi)
a4_height_px = int(29.7 / 2.54 * dpi)
background = Image.new('RGB', (a4_width_px, a4_height_px), 'white')

# Calculer les positions
x1 = (a4_width_px - width_px) // 2
y1 = (a4_height_px // 2 - height_px) // 2  # Pour la première image en haut

x2 = (a4_width_px - width_px) // 2
y2 = a4_height_px // 2 + y1  # Pour la seconde image en bas

# Placer les images sur le fond
background.paste(resized_face1, (x1, y1))
background.paste(resized_face2, (x2, y2))

# Sauvegarder l'image finale
background.save("path/to/exit/image_a4.jpg")  # Remplacez par votre chemin de sortie

print("Les deux faces ont été placées sur un fond A4 et sont prêtes à être imprimées.")
