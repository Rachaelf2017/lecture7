#!/usr/bin/env python
import sys
import os
import csv
import glob
from datetime import datetime
from pandas import DataFrame, Series
import pandas as pd

def read_all_files(dir_path) :
	data_files = glob.glob(dir_path + '/*')
	frames = []
	for f in data_files:
		extension = os.path.splitext(f)[1]
		file_reader = reader(extension)
		new_frame = file_reader(f)
		frames.append(new_frame)
	return pd.concat(frames, ignore_index=True)

def reader(extension) :
	if extension == '.csv' :
		return csv_reader
	elif extension == '.json' :
		return json_reader
	else :
		raise Exception('Reader not found for file type %s' % extension)

def json_reader (file_path) :
	return pd.read_json(file_path, orient='records')

def csv_reader (file_path) :
	return pd.read_csv(file_path, names=['purchase_price', 'sale_price', 'purchase_q_since_1970', 'sale_q_since_1970'])

# columns = ['purchase_price', 'sale_price', 'purchase_q_since_1970', 'sale_q_since_1970']
# sales=read_all_files(sys.argv[1], sys.argv[2])
#
#
# def write_all_files(frame, out_file_path):
# 	extension = os.path.splitext(out_file_path)[1]
# 	file_writer = writer(frame, extension)
# 	# frame.to_csv(out_file_path)
#
# def writer(frame, extension) :
# 	if extension == '.csv' :
# 		frame.to_csv(out_file_path)
# 	elif extension == '.json' :
# 		frame.to_json(out_file_path)
# 	else :
# 		raise Exception('Reader not found for file type %s' % extension)


print read_all_files(sys.argv[1])
