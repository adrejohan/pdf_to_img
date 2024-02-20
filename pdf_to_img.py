# import module
import argparse
import os
from pathlib import Path
from convert_function import convert

parser = argparse.ArgumentParser()
parser.add_argument('--src', '--source', '--s', nargs='*', help='pdf file source')
parser.add_argument('--out', '-o', nargs='?', default='./output/', help='output results directory, default=./output/')
args = parser.parse_args()

for i in args.src:
    if Path(i).is_file():
        convert(i, args.out)
    
    elif Path(i).is_dir():
        counter = 0
        for fname in os.listdir(i):
            if fname.endswith('.pdf'):
                counter += 1
                convert(fname, args.out)
    
        if counter == 0:
            print("Cannot find PDF file")
    
    else:
        print("Cannot find PDF file")