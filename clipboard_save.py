import tkinter as tk
from tkinter import filedialog
from PIL import ImageGrab
import os

root = tk.Tk()
root.withdraw()

folder_path = filedialog.askdirectory(title="Выберите папку для сохранения файлов")
if folder_path:
    try:
        text_data = root.clipboard_get(type='STRING')
        if text_data.strip():
            with open(os.path.join(folder_path, "clipboard_text.txt"), "w", encoding="utf-8") as f:
                f.write(text_data)
    except tk.TclError:
        pass

    try:
        image = ImageGrab.grabclipboard()
        if image is not None:
            image.save(os.path.join(folder_path, "clipboard_image.png"))
    except Exception as e:
        print(e)