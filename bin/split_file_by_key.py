#!/usr/bin/python
import argparse
import re

def remove_nonalnum(in_str):
	return re.sub('[^0-9a-zA-Z]+', '_', in_str).strip('_')

def filify_keys(keys):
	return '_'.join(['{val}'.format(val=remove_nonalnum(str(key).lower())) for key in keys])

def get_new_file_name(keys,in_filename):
	return '{name}.{keys}.split'.format(name=in_filename,keys=filify_keys(keys))

def get_new_writer(key,in_filename):
	out_filename = get_new_file_name(key,in_filename)
	return open(out_filename,'wb')

def convert_field_nums_to_ints(fields):
	return [int(key)-1 for key in fields.split(',')] # subtract 1 so field numbers align with list indices

def get_values_by_field_nums(line,keys):
	return [line[key] for key in keys]

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Given a *SORTED* file, delimiter, and key(s), split the file into numerous out files based on the key(s).')
	parser.add_argument('in_file',help='Path to input file')
	parser.add_argument('--fields',help='Field number, comma separated starting at 1 (e.g. "6", "6,7", etc)',type=str)	
	parser.add_argument('--delimiter',help='Delimiter (e.g. "\\t", ",", etc)',default='\t')
	parser.add_argument('--line-terminator',help='line terminator (e.g. "\\n", "\\r\\n", etc)',default='\n')
	args = parser.parse_args()

	with open(args.in_file,'r') as opened_in_file:
		last_seen_key = None
		writer = None
		field_nums = convert_field_nums_to_ints(args.fields)
		for line in opened_in_file:
			split_line = line.strip(args.line_terminator).split(args.delimiter)
			current_key = get_values_by_field_nums(split_line,field_nums)
			if last_seen_key == current_key:
				writer.write(line)
			else:
				last_seen_key = current_key
				writer = get_new_writer(last_seen_key,args.in_file)
				writer.write(line)