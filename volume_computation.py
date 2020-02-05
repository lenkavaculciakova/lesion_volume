#OPEN IPython (Py 2.7)

# you might need to install a module called xlrd : 'pip install xlrd'
import sys
sys.path.append('H:\THESIS\results')#set a path to a folder where you will work, copy there func.py, volume_computation.py and lesion_size_areas.xls
import os
os.chdir(r'H:\THESIS\results')
from func import remove_duplicates, volume, computation
filename = "lesion_area_14dpl.xlsx" #NOTE: you cannot have spaces in your file name
d = 105 # distance between two photos in micrometers
computation(filename, d)




