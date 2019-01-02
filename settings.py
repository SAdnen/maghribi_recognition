import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

DIR_DATA_RAW = os.path.join(ROOT_DIR, 'data', 'raw')
DIR_DATA_INTERIM = os.path.join(ROOT_DIR, 'data', 'interim')
DIR_DATA_PROCESSED = os.path.join(ROOT_DIR, 'data', 'processed')
DIR_DATA_EXTERNAL = os.path.join(ROOT_DIR, 'data', 'external')

DIR_DATA_LINES_KHALIL = os.path.join(DIR_DATA_INTERIM, 'LINES KHALIL')

NAME_FILE_KHALIL = 'code_musulman_par_khalil.pdf'
FILE_DATA_RAW_KHALIL = os.path.join(DIR_DATA_RAW, NAME_FILE_KHALIL)
DIR_KHALIL_JPG = os.path.join(DIR_DATA_INTERIM, 'Khalil_jpg')
DIR_KHALIL_PPM = os.path.join(DIR_DATA_INTERIM, 'Khalil_ppm')
NAME_FILE_EXEMPLE = 'exemple.png'
FILE_DATA_EXEMPLE = os.path.join(DIR_DATA_INTERIM, NAME_FILE_EXEMPLE)
