import filetype
import inputMain
from pdf2image import convert_from_path


kind = filetype.guess(inputMain.inputVal)

if(kind.extension == 'pdf'):
   print("converting to images from pdf")	
   pages = convert_from_path(inputMain.inputVal, 500)
   for page in pages:
    page.save('images\out.jpg', 'JPEG')
else:
	print("proceeding to OCR")