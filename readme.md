# Tesseract OCR for Standard Bank Shyft

The [Standard Bank Shyft App](https://getshyft.co.za/) produces password protected pdf statements
that are not super convenient if you want to do spreadsheet work after your holiday to see where 
all the money went.

This script uses [pdf2image](https://pypi.org/project/pdf2image/) to convert the printed pdf to images
and then [tesseract](https://github.com/tesseract-ocr/tesseract) to convert the images to text. The main
statement is chopped into sub images using the grey color of the horizontal lines and the known column 
widths so it is very sensitive to the pdf format but works as at 2020-12-28.

## Usage
   
I installed Tesseract from https://digi.bib.uni-mannheim.de/tesseract/. The Shyft statement needs to be 
printed to a non password protected pdf, then the paths in ```ocr.py``` need to be updated and the script 
run.

