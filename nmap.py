import os

def get_nmap(options, ip):
    command = 'nmap ' + options + " " + ip
    process = os.popen(command)
    results = str(process.read())
    return results

#print(get_nmap('-F', '192.206.5.35'))