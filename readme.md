# Calculating lesion volume
## Requirements
- Python 2.7.x
- you need to install modules xlrd and numpy: 'pip install xlrd numpy'
## How to use this code
- the functionality is in the `func.py` and can be used like this:
```
import sys
sys.path.append('<path to your folder>')#set a path to a folder where you will work, copy there func.py, volume_computation.py and lesion_size_areas.xls
from func import remove_duplicates, volume, computation
filename = "lesion_size_areas.xlsx" 
d = 105 # distance between two photos in micrometers
computation(filename, d)
```
