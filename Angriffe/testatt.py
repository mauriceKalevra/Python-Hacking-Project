import paramiko
import sys

def UploadFileAndExecute(ssh, fileName):

    sftpClient = ssh.open_sftp()
    sftpClient.put(fileName, fileName)
    ssh.exec_command(fileName+ " &")


def main():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(sys.argv[1], username=sys.argv[2], password=sys.argv[3])

    UploadFileAndExecute(ssh, sys.argv[4])

    ssh.close()
