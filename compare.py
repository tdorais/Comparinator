"""Comparinator"""
from pathlib import Path
from sys import argv
import argparse
import json

INDEX_FILE = "index.json"
target_file = ""
output_file = ""

def get_index(file_path):
    'generates index and saves it to the cache'
    print("build cache off " + file_path)

def generate_index(obj):
    'builds the index off a text file'

def load_index():
    'Loads Index file'
    index = Path(INDEX_FILE)

    if index.is_file():
        with open(INDEX_FILE) as json_data:
            return json.load(json_data)
    else:
        print("Missing index document. Please re-run with the -i parameter.")
        
def save_file(file_path, obj):
    'saves an object to file'

def load_file(file_path):
    'loads a file from the disk'

parser = argparse.ArgumentParser(usage='Compares and Correlates a given target file against the keyword frequency of a given document.', epilog='Good luck with future with them keywords!')
parser.add_argument('target_file', nargs='+', help='File to be compared against index')
parser.add_argument('-i', nargs='?', type=argparse.FileType('r'), help='Sets the file to be used as the index to compare against. Will be saved for future runs and replaces any previous indexes.')
parser.add_argument('-o', nargs='?',type=argparse.FileType('w'), help='Saves the output to a file with the passed name. Will not replace existing file.')
args = parser.parse_args()
print(args)
print(args.target_file[0])