import PyPDF2
import pdfplumber

def convert_text_to_uppercase(pdf_path):
    # Abre el archivo PDF
    with pdfplumber.open(pdf_path) as pdf:
        # Itera sobre las páginas del PDF
        for i in range(len(pdf.pages)):
            # Extrae el texto de la página
            page = pdf.pages[i]
            text = page.extract_text()

            # Convierte el texto a mayúsculas
            text_upper = text.upper()

            # Imprime el texto convertido
            print(text_upper)

# Usa la función en tu archivo PDF
convert_text_to_uppercase('tu_archivo.pdf')
