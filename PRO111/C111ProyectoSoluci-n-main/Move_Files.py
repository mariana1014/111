import os
import shutil

# .exe , .msi,  .gif, .png .jpg, .jpeg, .csv, .pdf , .xls , .xlsx , .ppt , .pptx

from_dir = "C:/Users/ADMIN/Downloads"
to_dir = "C:/WhiteHatJr/"

list_of_files = os.listdir(from_dir)
print(list_of_files)

# Mueve todos los archivos de imagen de la carpeta de descargas a otra carpeta
for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)

   

        
