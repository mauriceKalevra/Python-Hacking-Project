import os
import paramiko
import sys

ssh = paramiko.SSHClient() 
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
ssh.connect("172.17.0.2", username="root",password="root")
sftp = ssh.open_sftp()
sftp.put("SW.py", "/root")
sftp.close()
ssh.close()
