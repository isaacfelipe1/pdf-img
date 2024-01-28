import os
import sys
import fitz  
from PIL import Image

def pdf_to_images(pdf_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    pdf_document = fitz.open(pdf_path)
    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        image = page.get_pixmap()
        pil_image = Image.frombytes("RGB", [image.width, image.height], image.samples)
        image_path = os.path.join(output_folder, f"imagem_{page_number + 1}.png")
        pil_image.save(image_path, "PNG")
        print(f"Página {page_number + 1} salva como '{image_path}'")
    pdf_document.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
    
        print("Uso: python script.py caminho_para_o_pdf pasta_de_saida")
    else:
        pdf_path = sys.argv[1]
        output_folder = sys.argv[2]
        pdf_to_images(pdf_path, output_folder)
