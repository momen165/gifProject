# Image-to-GIF Converter

This a Python application that lets you select multiple image files and convert them into an animated GIF.

## Features

* Easy image selection using a file dialog.
* Resizes images to a consistent size before GIF creation.
* Handles PNG and JPG image formats.

## Installation

**Prerequisites**

* Python 3.6 or later 
* **tkinter** (usually included in standard Python installations)

**External Libraries**

* **Pillow (PIL):**  Used for image manipulation. Install with `pip install Pillow`
* **imageio:**  Provides GIF writing capabilities. Install with `pip install imageio`
* **numpy:**  Used for working with image data as arrays. Install with `pip install numpy`

## Usage

1. Run the `image_to_gif.py`.
2. Click **Open File** to select one or more images (PNG or JPG).
3. Images will resize automatically. 
4. Click **convertToGif** to create the GIF.
5. Choose a save location and filename.
