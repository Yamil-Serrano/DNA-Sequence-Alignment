import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD  # Importing drag-and-drop functionality
from sequence_alignment import align_sequences_from_csv  # Importing the backend logic to align sequences
from PIL import Image, ImageTk  # Importing for image handling

# Function triggered when a file is dropped into the application
def drop(event):
    """
    Handles the file drop event. Reads the dropped file, aligns sequences, and displays the results.

    Args:
        event: The event object containing information about the file drop.

    Functionality:
        1. Extracts the file path from the event data.
        2. Calls the sequence alignment function from the backend.
        3. Clears the previous results and displays the new alignment results in the text box.
    """
    file_path = event.data
    output = align_sequences_from_csv(file_path)  # Process the file for sequence alignment
    result_text.delete(1.0, tk.END)  # Clear the previous results in the text area
    for line in output:
        result_text.insert(tk.END, line + '\n')  # Insert the new results

# Initialize the main window for the application
root = TkinterDnD.Tk()  # Use TkinterDnD for drag-and-drop capability
root.title("Sequence Alignment Tool")  # Set the title of the window
root.geometry("1000x500")  # Fix window size to 1000x500 pixels
root.configure(bg="#f0f0f0")  # Set background color to light gray
root.resizable(False, False)  # Disable resizing to maintain layout integrity

# Set the window icon
icon_path = "resources/dna.ico"  # Path to the icon file
root.iconbitmap(icon_path)  # Apply the icon to the window

# Create the main container that holds two columns (left for file drop, right for results)
main_container = tk.Frame(root, bg="#f0f0f0")
main_container.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

# Left column to handle the file drop area
left_column = tk.Frame(main_container, bg="#f0f0f0", width=300)
left_column.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
left_column.pack_propagate(False)  # Prevent auto-resizing

# Right column to display the results of the sequence alignment
right_column = tk.Frame(main_container, bg="#f0f0f0", width=600)
right_column.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
right_column.pack_propagate(False)  # Prevent auto-resizing

# Define dimensions for the frames within each column
container_width = 510  # Width for the content frames
container_height = 470  # Height for the content frames

# Create a frame in the left column for the drop area
left_frame = tk.Frame(left_column, bg="#e0e0e0")
left_frame.place(relx=0.5, rely=0.5, anchor="center", width=container_width, height=container_height)

# Create a frame in the right column for the results display
right_frame = tk.Frame(right_column, bg="#e0e0e0")
right_frame.place(relx=0.5, rely=0.5, anchor="center", width=container_width + 100, height=container_height)

# Load and resize the image used for the file drop area
image_path = "resources/file.png"  # Path to the image used in the drop area
image = Image.open(image_path)
image = image.resize((90, 90), Image.LANCZOS)  # Resize image to 90x90 pixels
photo = ImageTk.PhotoImage(image)  # Convert the image to Tkinter-compatible format

# Create the drop zone label with the image and descriptive text
drop_zone = tk.Label(
    left_frame,
    image=photo,  # The image displayed in the drop zone
    compound=tk.TOP,  # Image placed above the text
    text="Drag and drop your CSV file here",  # Instructional text
    font=("Arial", 10),  # Font style and size
    bg="#e0e0e0",  # Background color
    padx=20, pady=20  # Padding around the content
)
drop_zone.image = photo  # Keep a reference to the image to prevent garbage collection
drop_zone.place(relx=0.5, rely=0.5, anchor="center")  # Center the drop zone in the frame

# Create a header in the right column for the results display
header_label = tk.Label(
    right_frame,
    text="Alignment sequence and its score:",  # Descriptive text for the results section
    font=("Arial", 16, "bold"),  # Font style for the header
    bg="#e0e0e0",  # Background color
    anchor="w",  # Left-align the text
)
header_label.place(relx=0.05, rely=0.05)  # Place near the top-left corner of the frame

# Create a text box in the right column to display the alignment results
result_text = tk.Text(
    right_frame,
    wrap=tk.WORD,  # Automatically wrap long lines at word boundaries
    font=("Courier", 12),  # Monospaced font for easy reading of alignment results
    bg="#e0e0e0",  # Background color
    relief=tk.FLAT,  # Remove the default border style
    bd=0  # No border
)
result_text.place(relx=0.05, rely=0.15, relwidth=0.9, relheight=0.8)  # Position the text box in the frame

# Enable drag-and-drop functionality for the drop zone
drop_zone.drop_target_register(DND_FILES)  # Register drop zone for file drops
drop_zone.dnd_bind('<<Drop>>', drop)  # Bind the drop event to the drop function

# Start the Tkinter event loop to run the application
root.mainloop()
