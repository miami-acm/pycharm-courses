import argparse

from fs import open_fs

parser = argparse.ArgumentParser()
parser.add_argument('dir', type=str)
args = parser.parse_args()

folder = open_fs(args.dir)
with folder:
    for filename in folder.listdir('/'):  # type: str
        print(filename)
