import tkinter as tk
from tkinter import filedialog
from sequence_alignment import align_sequences_from_csv
from PIL import Image, ImageTk
import os
import sys

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def open_file_dialog():
    file_path = filedialog.askopenfilename(
        title="Select a CSV file",
        filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
    )
    if file_path:
        output = align_sequences_from_csv(file_path)
        result_text.delete(1.0, tk.END)
        for line in output:
            result_text.insert(tk.END, line + '\n')

root = tk.Tk()
root.title("Sequence Alignment Tool")
root.geometry("1000x500")
root.configure(bg="#f0f0f0")
root.resizable(False, False)

# Modificado para usar resource_path
icon_path = resource_path("resources/dna.ico")
root.iconbitmap(icon_path)

main_container = tk.Frame(root, bg="#f0f0f0")
main_container.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

left_column = tk.Frame(main_container, bg="#f0f0f0", width=300)
left_column.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
left_column.pack_propagate(False)

right_column = tk.Frame(main_container, bg="#f0f0f0", width=600)
right_column.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
right_column.pack_propagate(False)

container_width = 510
container_height = 470

left_frame = tk.Frame(left_column, bg="#e0e0e0")
left_frame.place(relx=0.5, rely=0.5, anchor="center", width=container_width, height=container_height)

right_frame = tk.Frame(right_column, bg="#e0e0e0")
right_frame.place(relx=0.5, rely=0.5, anchor="center", width=container_width + 100, height=container_height)

# Modificado para usar resource_path
image_path = resource_path("resources/file.png")
image = Image.open(image_path)
image = image.resize((90, 90), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

drop_zone = tk.Label(
    left_frame,
    image=photo,
    compound=tk.TOP,
    text="Click to select your CSV file",
    font=("Arial", 10),
    bg="#e0e0e0",
    padx=20, pady=20
)
drop_zone.image = photo
drop_zone.place(relx=0.5, rely=0.5, anchor="center")

# Añadimos el evento click para abrir el selector de archivos
drop_zone.bind("<Button-1>", lambda e: open_file_dialog())

header_label = tk.Label(
    right_frame,
    text="Alignment sequence and its score:",
    font=("Arial", 16, "bold"),
    bg="#e0e0e0",
    anchor="w",
)
header_label.place(relx=0.05, rely=0.05)

result_text = tk.Text(
    right_frame,
    wrap=tk.WORD,
    font=("Courier", 12),
    bg="#e0e0e0",
    relief=tk.FLAT,
    bd=0
)
result_text.place(relx=0.05, rely=0.15, relwidth=0.9, relheight=0.8)

if __name__ == '__main__':
    root.mainloop()
