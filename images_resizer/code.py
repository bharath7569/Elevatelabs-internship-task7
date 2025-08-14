from PIL import Image
import os

width = int(input("Enter new width: "))
height = int(input("Enter new height: "))

os.makedirs("images_resized", exist_ok=True)

formats = (".jpg", ".jpeg", ".png", ".bmp", ".gif")

for file in os.listdir("images_input"):
    if file.lower().endswith(formats):
        img = Image.open(f"images_input/{file}")
        img = img.resize((width, height))
        img.save(f"images_resized/{file}")

print("✅ All images resized successfully!")