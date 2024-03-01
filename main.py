import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import imageio.v3 as iio
import numpy as np

filenames = []
images = []


def open_file():
    file_path = filedialog.askopenfilename(initialdir="/",
                                           title="Select a File",
                                           filetypes=(("imageFile", "*.png*"),
                                                      ("imageFile", "*.jpg*"),
                                                      ("all files", "*.*")))
    if file_path:
        try:
            with Image.open(file_path) as img:
                resized_img = img.resize((1200, 900))
                images.append(np.array(resized_img))
                filenames.append(file_path)
                print("File paths:", filenames)
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".gif",
                                             filetypes=(("GIF files", "*.gif"),
                                                        ("All files", "*.*")))
    if file_path:
        try:
            iio.imwrite(file_path, images, duration=500, loop=0)
        except Exception as e:
            print(f"An error occurred: {e}")


def convert_to_gif():
    if not filenames:  # Check if any files are selected
        messagebox.showwarning("No Files", "Please select image files first.")
        return

    images.clear()
    for filename in filenames:
        with Image.open(filename) as img:
            resized_img = img.resize((1200, 900))
            if img.mode == 'RGBA':
                resized_img = resized_img.convert('RGB')
            images.append(np.array(resized_img))

    save_file()


def configure_button(button, border_radius):
    button.config(borderwidth=3, highlightthickness=1, bd=1)  # Rounded style
    center_widget(button)


def center_widget(widget):  # Simplified centering
    widget.update()  # Ensure widget dimensions are ready
    width = widget.winfo_reqwidth()
    height = widget.winfo_reqheight()
    x = (r.winfo_screenwidth() // 2) - (width // 2)
    y = (r.winfo_screenheight() // 2) - (height // 2)
    widget.place(x=x, y=y)


r = tk.Tk()
messagebox.showinfo('Welcome', 'Welcome to Image to Gif Converter')
r.iconbitmap('icon/myicon.ico')

r.title('Image to Gif Converter')
r.geometry('520x300')
r.maxsize(520, 300)
open_button = tk.Button(r, text="Open File", command=open_file)
configure_button(open_button, border_radius=10)
open_button.pack(pady=10)

convertToGif = tk.Button(r, text="convertToGif", command=convert_to_gif)
convertToGif.config(borderwidth=3, highlightthickness=0, bd=0)
configure_button(convertToGif, border_radius=10)
convertToGif.pack(pady=10)

stop_button = tk.Button(r, text='Stop', width=25, command=r.destroy)
configure_button(stop_button, border_radius=10)
stop_button.pack(pady=10)
r.mainloop()
