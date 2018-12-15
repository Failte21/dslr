import argparse
import sys

def parse_main():
	parser = argparse.ArgumentParser()
	parser.add_argument('filename', help='Name of the dataset')
	return parser.parse_args()