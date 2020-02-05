from __future__ import print_function
from __future__ import division

def remove_duplicates(values): 
	#this function takes list of values and returns a list that does not contain duplicate values
	output = []
	seen = set()
	for value in values:
    # If value has not been encountered yet,
    # ... add it to both list and set.
		if value not in seen:
			output.append(value)
			seen.add(value)
	return output

def volume(A1, A2, h):
	#this function computes volume of a truncated cone out of areas and distance between them
	import numpy as np
	r1 = np.sqrt(float(A1)/np.pi)
	r2 = np.sqrt(float(A2)/np.pi)
	output = (float(1)/3)*np.pi*(r1**2+r1*r2+r2**2)*h
	return output

def computation(filename, d): 
	#filename is a wole path to your leasions_size_areas.xlsx
	#d is a distance between two photos
	import xlrd
	import numpy as np
	#manipulation with excel objects
	workbook = xlrd.open_workbook(filename)
	sheet = workbook.sheet_by_index(0) #in case of having the results on a different sheet in excel,
	#adjust an index. (NOTICE: Python indexing starts with zero) 
	#following list contains names of animals, that will be used as keys to dictionaries...
	animal_list = remove_duplicates([sheet.cell_value(row,0) for row in range(1,sheet.nrows)])
	#data dictionary contains all the values of areas for every key
	data = {key:[] for key in animal_list}
	results = {key:[] for key in animal_list}
	for row in range(1, sheet.nrows):
		key = sheet.cell_value(row,0)
		data[key].append(sheet.cell_value(row,1))
	#computing volume by adding truncated cones for each animal
	for key in data.keys():
		V = []
		for indx in range(len(data[key])-1):
			V.append(volume(data[key][indx], data[key][indx+1], d))
		results[key] = sum(V)
	#in case there is just one photo per animal, we approximate the lesion by a sphere and compute the volume
	for idx in range(len(results.keys())):
		if results.values()[idx] == 0:
			r = np.sqrt((data[data.keys()[idx]][0])/np.pi)
			results[data.keys()[idx]] = float(4)/3*np.pi*r**3
	#saving output data in a file in the form of Animal - volume			
	with open('results.csv', 'w') as f:
	    [f.write('{0},{1}\n'.format(key, value)) for key, value in results.items()]
