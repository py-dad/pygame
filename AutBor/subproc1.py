import subprocess

""" entry = input("Enter c to start calc")

if entry == 'c' or 'C':
    subprocess.Popen('C:\\Windows\System32\\calc.exe')


# alt way using str().lower() method

entry = str(input("Enter c to start calc")).lower()

if entry == 'c':
    subprocess.Popen('C:\\Windows\System32\\calc.exe')
  """

# make it a function?
    
def openCalc():
    entry = input("Enter c to start calc")
    if entry == 'c' or 'C':
        subprocess.Popen('C:\\Windows\System32\\calc.exe')

openCalc()