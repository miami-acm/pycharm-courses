import argparse
import subprocess

from fs import open_fs

parser = argparse.ArgumentParser()
parser.add_argument('dir', type=str, nargs='?', default='~/Downloads/')
args = parser.parse_args()

folder = open_fs(args.dir)
with folder:
    java_files = folder.walk.files(filter=['*.java'])

    # Remove beginning forward slash
    java_files = map(lambda file: file[1:], java_files)

    # Call javac
    subprocess.run(['javac', *java_files], cwd=folder.getsyspath('/'))
