from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox


class ImgtopdfConverter:
    def __init__(self, converter):
        self.converter = converter
        converter.title("Converter from Img to Pdf")

        self.image_paths = []

        self.label = Label(converter, text="Select images :")
        self.label.pack()

        self.button = Button(converter, text="Select", command=self.imageselect)
        self.button.pack()

        self.convert_button = Button(converter, text="Convert to PDF document", command=self.imgtopdf)
        self.convert_button.pack()

    def imageselect(self):

        fileextension = (("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*"))
        imagepath = filedialog.askopenfilenames(filetypes=fileextension)
        self.image_paths.extend(imagepath)

        for image_path in imagepath:
            image = Image.open(image_path)
            image.thumbnail((200, 200))
            photo = ImageTk.PhotoImage(image)
            label = Label(self.converter, image=photo)
            label.image = photo
            label.pack()

    def imgtopdf(self):
        fileextension = (("PDF files", "*.pdf"), ("All files", "*.*"))
        pdf_path = filedialog.asksaveasfilename(filetypes=fileextension, defaultextension=".pdf")


        pdfimages = []
        for image_path in self.image_paths:
            image = Image.open(image_path)
            pdfimages.append(image.convert("RGB"))


        if pdfimages:
            pdfimages[0].save(pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=pdfimages[1:])
            message = f"File saved to {pdf_path}"
            messagebox.showinfo("Successfullycompleted", message)
            self.imagepaths = []

root = Tk()
app = ImgtopdfConverter(root)
root.mainloop()
