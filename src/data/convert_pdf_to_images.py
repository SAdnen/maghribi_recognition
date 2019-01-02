import os
import settings
from pdf2image import convert_from_path

DPI = 300
PPM_OUTPUT_PATH = settings.DIR_KHALIL_PPM
JPG_OUTPUT_PATH = settings.DIR_KHALIL_JPG
FILE_PATH = settings.FILE_DATA_RAW_KHALIL

pages = convert_from_path(FILE_PATH, DPI,PPM_OUTPUT_PATH)

for i, p in enumerate(pages):
    p.save(os.path.join(JPG_OUTPUT_PATH, str(i)+'.jpg'), 'JPEG')
