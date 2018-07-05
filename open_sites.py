#!/usr/bin/python3
# author: Daniel Moore
# Usage: Takes in a list of ip addresses or hostnames and opens them in the brow
# ser
import webbrowser
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("input", help="Input list of line seperated IP addresses", metavar="<input-file-name>")
args = parser.parse_args()

def main():
	input_file_name=args.input

	f = open(input_file_name, "r")
	data = f.read()
	host_list = data.split('\n')

	ten_count = 0
	for addr in host_list:
		url='http://'+addr+'/'
		webbrowser.open_new_tab(url)
		if ten_count == 10:
			while True:
				prompt = 'Ten tabs opened, enter \'y\' to continue or \'n\' to exit: '
				respone = input(prompt)
				if respone == 'y':
					ten_count = 0
					break
				elif respone == 'n':
					sys.exit()
				else:
					print('Invalid respone')

if __name__ == '__main__':
	main()
