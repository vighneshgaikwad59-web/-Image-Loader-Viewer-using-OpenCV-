# 🌸 Image Loader & Viewer using OpenCV

A simple Python script that loads an image from disk, displays it in a window using **OpenCV**, and prints its shape (height, width, channels).

This is a beginner-friendly starting point for **image processing** and **computer vision** in Python.

---

## 📌 Features

- Load an image from a local file path
- Display the image in a GUI window
- Wait for a key press, then close the window cleanly
- Handle the case where the image fails to load
- Print the image shape (`height, width, channels`)

---

## 🛠️ Tech Stack

- Python 3.8+
- OpenCV (`opencv-python`)

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/vighneshgaikwad59-web/<your-repo-name>.git
cd <your-repo-name>

# Install dependencies
pip install opencv-python
```

---

## 🚀 Usage

1. Put your image (e.g. `flower.png`) in the project folder, or update the path in the script.
2. Run the script:

```bash
python image_viewer.py
```

3. A window will open showing the image. Press **any key** to close it.

---

## 💻 Code

```python
import cv2

img = cv2.imread("flower.png")  # load image (use your own path)

if img is not None:
    cv2.imshow("window display", img)  # show image
    cv2.waitKey(0)                     # wait for key press
    cv2.destroyAllWindows()            # close window
    print("Image shape:", img.shape)   # (height, width, channels)
else:
    print("Failed to load image.")
```

---

## 🔍 How It Works

| Function | Purpose |
|---|---|
| `cv2.imread(path)` | Reads the image and returns it as a NumPy array (`None` if loading fails) |
| `cv2.imshow(name, img)` | Opens a window and displays the image |
| `cv2.waitKey(0)` | Pauses the program until a key is pressed |
| `cv2.destroyAllWindows()` | Closes all OpenCV windows |
| `img.shape` | Returns `(height, width, channels)` of the image |

---

## 📤 Sample Output

```
Image shape: (512, 512, 3)
```

> `3` channels = **B, G, R** (OpenCV reads images in BGR order, not RGB).

---

## ⚠️ Common Issues

- **"Failed to load image."** → Check that the file path is correct. On Windows, use double backslashes (`\\`) or a raw string (`r"C:\path\to\flower.png"`).
- **Window not responding** → Click on the image window and press a key.

---

## 🔮 Future Improvements

- Convert image to grayscale
- Resize and crop images
- Apply filters (blur, edge detection)
- Save processed images

---

## 👤 Author

**Vighnesh Anand Gaikwad**
MSc Bioinformatics | Python | Data Science
GitHub: [@vighneshgaikwad59-web](https://github.com/vighneshgaikwad59-web)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
