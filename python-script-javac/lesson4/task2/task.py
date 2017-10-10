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
    compilation = subprocess.run(['javac', *java_files], cwd=folder.getsyspath('/'))

    if compilation.returncode != 0:
        # Compilation has failed
        print("This code doesn't compile!")
    else:
        # Compilation has succeeded
        print('This code compiles!')
