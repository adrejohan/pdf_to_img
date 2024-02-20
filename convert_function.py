import os
from pdf2image import convert_from_path

popler_path = r".\poppler\Library\bin"

def convert(path_name, path_out):
    filename = os.path.splitext(os.path.basename(path_name))[0]
    images = convert_from_path(path_name, poppler_path=popler_path)
    for j in range(len(images)):
        images[j].save(path_out+filename+'_page_'+ str(j) +'.jpg', 'JPEG')