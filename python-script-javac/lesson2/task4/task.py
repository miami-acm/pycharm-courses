import argparse

from fs import open_fs

parser = argparse.ArgumentParser()
# nargs allows this positional argument to be optional
parser.add_argument('dir', type=str, nargs='?', default='~/Downloads/')
args = parser.parse_args()

folder = open_fs(args.dir)
with folder:
    for path in folder.walk.files(filter=['*.java']):
        print(path)
