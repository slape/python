import argparse
import sys

# Create command line arguments
parser = argparse.ArgumentParser(
    description='A custom version of the cat command.',
    prog='cot',
    epilog='copyright pirate software, 2019.')
parser.add_argument('-o', '--out', type=argparse.FileType('w'), help='specify an output file.')
parser.add_argument('infile', type=argparse.FileType('r'), help='provide at least one file to concatenate.')
args = parser.parse_args() 

for line in args.infile.readlines():
    if args.out:
        args.out.write(line)
    else:
        print(line)
