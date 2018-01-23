"""Comparinator"""
from pathlib import Path
from sys import argv
import json

INDEX_FILE = "index.json"
target_file = ""
output_file = ""

def print_help():
    'MAN page'
    print("Compare.py compares files based on keyword frequency.")
    print("Taxonomy: compare.py target.txt -i index.txt -o output.txt")

def handle_argv(args):
    'Command Arguments handler.'
    end_run = False
    has_index = False
    i = 1

    while i < len(args):
        arg = args[i]
        if i == 1:
            if arg == "-help":
                print_help()
                end_run = True
                break
            else:
                target_file = arg

        if arg == "-i":
            if i < len(args) - 1:
                get_index(args[i+1])
                has_index = True
                i += 1
            else:
                print("Missing Index File Name and Path")
                end_run = True
                break

        if arg == "-o":
            if i < len(args) - 1:
                output_file = args[i+1]
                i += 1
            else:
                print("Missing Output File Name Path")
                end_run = True
                break

        i += 1

    if end_run:
        exit()

    if not has_index:
        load_index()

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


handle_argv(argv)
