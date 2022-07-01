import requests

def get_update(url, local_version):
    '''
    In order for this to work both sides need to have a variable
    VERSION defined with a verison number in it
    it checks if the version number on the server is higher
    if it is then updates the app
    '''
    outdated = False
    re = requests.get(url)
    for i in re.split('\n'):
        if i.split(' ')[0] == VERSION:
            server_version = i.split(' ')[-1]
    if float(server_version) > float(local_version):
        outdated = True
    return re.text, outdated
