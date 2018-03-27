import sys
from pdf2image import convert_from_path, convert_from_bytes
import pytesseract 
from PIL import Image

images = convert_from_path(sys.argv[1])

i = '1'
text = ''

final_images = []

for image in images:
	image.save("image"+i+".png","PNG")
	final_images.append("image"+i+".png")
	j = int(i)
	j=j+1
	i = str(j)

fp = open("final_text.txt","w")

for i in final_images: 
	text = pytesseract.image_to_string(Image.open(i))
	fp.write(text.encode('utf-8'))


	
