**Image to PDF Converter using Tkinter and PIL**

Image to PDF Converter application using the Tkinter library for the graphical user interface and the PIL (Pillow) library for image manipulation and PDF creation. This converter enables users to select multiple image files and convert them into a single PDF document. Here's an overview of the main components and functionalities:

1. **Application Initialization:**
   - The converter is initialized as a Tkinter window titled "Converter from Img to Pdf".
   - The `ImgtopdfConverter` class manages the converter's GUI and functionality.

2. **Image Selection:**
   - Users can click the "Select" button to open a file dialog that allows them to choose multiple image files (JPEG or PNG).
   - The selected image paths are stored in the `image_paths` list.
   - For each selected image, a thumbnail is displayed on the GUI using the `ImageTk.PhotoImage` class.

3. **Image to PDF Conversion:**
   - Upon clicking the "Convert to PDF document" button, users can choose a destination path to save the PDF file.
   - The selected images are opened using PIL, and their RGB representations are collected into the `pdfimages` list.
   - The first image in the list is saved as a PDF, and subsequent images are appended to create the multi-page PDF.
   - The resolution of the images in the PDF is set to 100 DPI.
   - A success message is displayed using a messagebox when the conversion process is completed.

4. **Tkinter Main Loop:**
   - The main loop is started using `root.mainloop()`, allowing the converter GUI to interact with the user.

In summary, this Image to PDF Converter application provides an intuitive interface for users to convert multiple image files into a single PDF document. The use of Tkinter and PIL libraries simplifies the process of selecting images, generating thumbnails, and creating a PDF with minimal effort. This tool can be useful for users who need to compile images into a PDF format for various purposes such as presentations, documentation, or sharing image collections.
