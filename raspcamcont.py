import tkinter as tk
from tkinter import ttk
from picamera2 import Picamera2

# Initialize the camera
picam2 = Picamera2()

# Create the main application window
root = tk.Tk()
root.title("Raspberry Pi Camera Control")

# Define a function to update camera settings
def update_settings():
    iso_value = int(iso_var.get())
    brightness_value = float(brightness_var.get())
    contrast_value = float(contrast_var.get())

    camera_config = picam2.create_still_configuration()
    camera_config["controls"]["AnalogueGain"] = iso_value / 100
    camera_config["controls"]["Brightness"] = brightness_value
    camera_config["controls"]["Contrast"] = contrast_value

    picam2.configure(camera_config)
    picam2.start()
    picam2.capture_file("image.jpg")
    picam2.stop()

    status_label.config(text="Settings updated and image captured!")

# Create GUI elements
iso_label = ttk.Label(root, text="ISO:")
iso_label.grid(column=0, row=0, padx=10, pady=10)

iso_var = tk.StringVar(value="100")
iso_entry = ttk.Entry(root, textvariable=iso_var)
iso_entry.grid(column=1, row=0, padx=10, pady=10)

brightness_label = ttk.Label(root, text="Brightness:")
brightness_label.grid(column=0, row=1, padx=10, pady=10)

brightness_var = tk.StringVar(value="0.5")
brightness_entry = ttk.Entry(root, textvariable=brightness_var)
brightness_entry.grid(column=1, row=1, padx=10, pady=10)

contrast_label = ttk.Label(root, text="Contrast:")
contrast_label.grid(column=0, row=2, padx=10, pady=10)

contrast_var = tk.StringVar(value="1.0")
contrast_entry = ttk.Entry(root, textvariable=contrast_var)
contrast_entry.grid(column=1, row=2, padx=10, pady=10)

update_button = ttk.Button(root, text="Update Settings", command=update_settings)
update_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

status_label = ttk.Label(root, text="")
status_label.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
