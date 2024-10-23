import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from Backend import align_sequences_from_csv
from PIL import Image, ImageTk

def drop(event):
    file_path = event.data
    output = align_sequences_from_csv(file_path)
    result_text.delete(1.0, tk.END)
    for line in output:
        result_text.insert(tk.END, line + '\n')

# Create main window
root = TkinterDnD.Tk()
root.title("Sequence Alignment Tool")
root.geometry("1000x500")  # Set to exactly 1000x500
root.configure(bg="#f0f0f0")
root.resizable(False, False)

# Set the icon
icon_path = "resources/dna.ico"
root.iconbitmap(icon_path)

# Create main container with two columns
main_container = tk.Frame(root, bg="#f0f0f0")
main_container.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

# Left column (drop area)
left_column = tk.Frame(main_container, bg="#f0f0f0", width=300)
left_column.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
left_column.pack_propagate(False)

# Right column (results)
right_column = tk.Frame(main_container, bg="#f0f0f0", width=600)
right_column.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
right_column.pack_propagate(False)

# Create container frames (now rectangular)
container_width = 510  # Adjusted for 1000x500 window
container_height = 470  # Adjusted for 1000x500 window

left_frame = tk.Frame(left_column, bg="#e0e0e0")
left_frame.place(relx=0.5, rely=0.5, anchor="center", width=container_width, height=container_height)

right_frame = tk.Frame(right_column, bg="#e0e0e0")
right_frame.place(relx=0.5, rely=0.5, anchor="center", width=container_width + 100, height=container_height)  # Expanded width for right frame

# Load and resize the image
image_path = "resources/file.png"
image = Image.open(image_path)
image = image.resize((90, 90), Image.LANCZOS)  # Adjusted size
photo = ImageTk.PhotoImage(image)

# Create drop zone with image and text
drop_zone = tk.Label(
    left_frame,
    image=photo,
    compound=tk.TOP,
    text="Drag and drop your CSV file here",
    font=("Arial", 10),
    bg="#e0e0e0",
    padx=20,
    pady=20
)
drop_zone.image = photo
drop_zone.place(relx=0.5, rely=0.5, anchor="center")

# Right column header (inside the rectangular frame)
header_label = tk.Label(
    right_frame,
    text="Alignment sequence and its score:",
    font=("Arial", 16, "bold"),
    bg="#e0e0e0",
    anchor="w",
)
header_label.place(relx=0.05, rely=0.05)

# Result text area
result_text = tk.Text(
    right_frame,
    wrap=tk.WORD,
    font=("Courier", 12),
    bg="#e0e0e0",
    relief=tk.FLAT,
    bd=0
)
result_text.place(relx=0.05, rely=0.15, relwidth=0.9, relheight=0.8)

# Enable drag and drop
drop_zone.drop_target_register(DND_FILES)
drop_zone.dnd_bind('<<Drop>>', drop)

root.mainloop()
