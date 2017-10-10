import subprocess

ping_command = subprocess.run('ping www.miamioh.edu')

print('\n-----\n')
print('ping_command = {val}'.format(val=ping_command))
