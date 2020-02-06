# Calculating lesion volume
## Requirements
- Python 2.7.x
- you need to install modules xlrd and numpy: 'pip install xlrd numpy'
## How to use this code
- The input excel document must be layed out in three colums: first column must specify the animal name for each entry, second column contains the area of each lesion, and the third column has to be the radius of each specific area. No formatting nor empty spaces are allowed.
- the functionality is in the `func.py` and can be used like this:
```
import sys
sys.path.append('<path to your folder>')#set a path to a folder where you will work, copy there func.py, volume_computation.py and lesion_size_areas.xls
from func import remove_duplicates, volume, computation
filename = "lesion_area_dem_westerndiet.xlsx" 
d = 96 # distance between two photos in micrometers
computation(filename, d)
```
