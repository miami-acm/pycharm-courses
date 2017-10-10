import subprocess

javac_invocation = subprocess.run('javac -version')
print('javac is installed!' if javac_invocation.returncode == 0 else
      'javac is not installed')
