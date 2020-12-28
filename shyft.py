from PIL import ImageOps
import pytesseract
from pdf2image import convert_from_path
import numpy as np

input_pdf = r'C:\Users\James\OneDrive\James\BankStatements\Shyft\2020-12-27 Printed.pdf'
tesseract_exe = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
output_csv = r"C:\Users\James\OneDrive\James\BankStatements\Shyft\2020-12-27.csv"


def add_csv_lines(lines, image):
    """
    Find the horizontal gray lines, use the know column widths. OCR each cell.

    :param lines:
    :param image:
    :return:
    """
    vertical_lines = [91, 245, 565, 1030, 1411, 1572]
    gray_image = ImageOps.grayscale(image)

    image_data = np.array(gray_image)

    horizontal_lines = []
    r = 0
    while r < image_data.shape[0] - 10:
        r += 1
        if 255 > image_data[r, 550] > 200 and image_data[r + 5, 550] == 255:
            horizontal_lines.append(r)
            r += 5

    for h in range(len(horizontal_lines) - 1):
        row = []
        for v in range(len(vertical_lines) - 1):

            left = vertical_lines[v]
            right = vertical_lines[v + 1]
            top = horizontal_lines[h]
            bottom = horizontal_lines[h + 1]
            cell_image = gray_image.crop((left, top, right, bottom))
            cell_text = pytesseract.image_to_string(cell_image)
            if v == 0:
                cell_text = f"20{cell_text[6:8]}-{cell_text[3:5]}-{cell_text[0:2]}"
            else:
                cell_text = cell_text[:-2]
                cell_text = cell_text.split("\n")
                cell_text = " ".join(cell_text)
            row.append(cell_text)
        lines.append(",".join(row)+ "\n")


# installed tesseract from https://digi.bib.uni-mannheim.de/tesseract/
pytesseract.pytesseract.tesseract_cmd = tesseract_exe
images = convert_from_path(input_pdf)
lines = []
i = 0
for img in images:
    i += 1
    print(f"processing page {i} of {len(images)}")
    add_csv_lines(lines, img)
    if i == 1:
        break

print(f"writing {output_csv}")
with open(output_csv, 'w') as f:
    f.writelines(lines)



