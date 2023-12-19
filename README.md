# PrintPrep Tool

## Overview
PrintPrep Tool is a simple yet effective Python script for preparing documents for printing. It currently focuses on resizing and arranging images on A4 sheets, ideal for users needing a quick and straightforward solution for printing dual-sided documents.

## Features
- Resize images to fit standard dimensions.
- Arrange two images (document sides) on a single A4 sheet.
- Center images for optimal printing layout.

## Future Plans
While PrintPrep Tool currently supports basic dimensions, we plan to expand it to include various sizes and formats, catering to a broader range of printing needs.

## Usage
Replace `path/to/image1.jpg` and `path/to/image2.jpg` with the paths to your document images. Adjust the dimensions as needed.

```python
# Example usage code snippet

from PIL import Image

# Chemins de vos images
image_path_face1 = "chemin/vers/face1.jpg"  # Remplacez par le chemin de la première face
image_path_face2 = "chemin/vers/face2.jpg"  # Remplacez par le chemin de la seconde face

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
background.save("chemin/vers/sortie/image_a4.jpg")  # Remplacez par votre chemin de sortie

print("Les deux faces ont été placées sur un fond A4 et sont prêtes à être imprimées.")


```

## Contributions
As a modest project in its early stages, contributions, suggestions, and feedback are warmly welcomed.
