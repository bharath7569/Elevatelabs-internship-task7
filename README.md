---

# 🖼 Image Resizer Tool

## 📌 Overview

This is a simple Python tool to *resize and convert multiple images* in one go.
It supports .jpg, .jpeg, .png, .bmp, and .gif formats, making it handy for batch image processing tasks.

---

## 🚀 Features

* Resize all images in a given folder.
* Maintain quality while reducing dimensions.
* Supports multiple image formats.
* Automatically saves resized images to a separate folder.

---

## 🛠 Tools & Libraries

* *Python 3.x*
* *Pillow* (PIL Fork) – for image processing
* *os* – for file and folder handling

---

## 📂 Project Structure


image resizer/
│── code.py            # Main script
│── images_input/      # Folder to store input images
│── images_resized/    # Folder where resized images are saved (auto-created)


---

## 📥 Installation

1. Clone or download this repository.
2. Install dependencies:

bash
pip install pillow


---

## ▶ How to Use

1. Place all the images you want to resize into the images_input folder.
2. Run the script:

bash
python code.py


3. Resized images will be saved in the images_resized folder.

---

## ⚙ Customization

* Change the *resize dimensions* in code.py by editing:

python
resize_width = 800
resize_height = 600


* Add more file formats to the valid_extensions list if needed.

---

## 📌 Example

Before running:


images_input/
 ├── image1.jpg
 ├── image2.png


After running:


images_resized/
 ├── image1_resized.jpg
 ├── image2_resized.png


---

## 📜 License

This project is free to use and modify.

---
