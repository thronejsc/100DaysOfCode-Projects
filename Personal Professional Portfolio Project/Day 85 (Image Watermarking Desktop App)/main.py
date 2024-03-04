import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermarking App")

        self.image_path = None
        self.watermark_text = tk.StringVar()
        self.watermark_text.set("Your Watermark")

        self.create_widgets()

    def create_widgets(self):
        # Frame to hold the widgets
        frame = tk.Frame(self.root, padx=10, pady=10)
        frame.pack(padx=20, pady=20)

        # Select Image Button
        select_image_button = tk.Button(frame, text="Select Image", command=self.select_image)
        select_image_button.grid(row=0, column=0, columnspan=2, pady=10)

        # Watermark Entry
        watermark_label = tk.Label(frame, text="Watermark Text:")
        watermark_label.grid(row=1, column=0, sticky=tk.E)

        watermark_entry = tk.Entry(frame, textvariable=self.watermark_text, width=30)
        watermark_entry.grid(row=1, column=1, pady=10)

        # Watermark Button
        watermark_button = tk.Button(frame, text="Watermark Image", command=self.watermark_image)
        watermark_button.grid(row=2, column=0, columnspan=2, pady=10)

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.image_path = file_path
            self.display_image()

    def display_image(self):
        image = Image.open(self.image_path)
        image.thumbnail((300, 300))  # Resize the image for display

        photo = ImageTk.PhotoImage(image)
        img_label = tk.Label(self.root, image=photo)
        img_label.image = photo  # Keep a reference to avoid garbage collection
        img_label.pack()

    def watermark_image(self):
        if self.image_path:
            original_image = Image.open(self.image_path)

            # Create a copy of the original image
            watermarked_image = original_image.copy()

            # Get image dimensions
            width, height = watermarked_image.size

            # Add text watermark
            draw = ImageDraw.Draw(watermarked_image)
            font = ImageFont.load_default()  # You can customize the font

            text = self.watermark_text.get()
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]


            # Calculate position to center the watermark
            x = (width - text_width) // 2
            y = (height - text_height) // 2

            # Draw the watermark on the image
            draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))

            # Save the watermarked image
            watermarked_image.save("./images/watermarked_image.jpg")

            tk.messagebox.showinfo("Success", "Image Watermarked and saved as watermarked_image.jpg")

        else:
            tk.messagebox.showerror("Error", "Please select an image first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
