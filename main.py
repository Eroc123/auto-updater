import updater

VERSION = '0.1'

def update(file):
    pass

file, isoutdated = updater.get_update('https://raw.githubusercontent.com/Eroc123/auto-updater/release/main.py', VERSION)
if isoutdated:
    update(file)
