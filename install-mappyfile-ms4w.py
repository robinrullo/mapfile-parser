#!C:\ms4w\Python\python.exe -u
# -*- coding: utf-8 -*-

import sys
import subprocess

# implement pip as a subprocess:
print("Installing mappyfile using pip:")
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'mappyfile'])

# process output with an API in the subprocess module:
reqs = subprocess.check_output([sys.executable, '-m', 'pip',
'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

print("Installed packages:")
print(installed_packages)
input()
