#!/usr/bin/python3
import os
import subprocess as sub


def runcmd(cmd):
    if "date" in cmd:
        output=sub.getoutput(cmd)
        print("\t{0}".format(output))
    elif "cal" in cmd:
        output=sub.getoutput(cmd)
        output="    "+output.replace('\n','\n\t')
        print(output)
    else:
        out=sub.getoutput(cmd)
        print(out,"\n")

def help():
    print("\t\tMAIN MENU")
    print()
    print("\t{:20s}To show date & time".format("date"))
    print("\t{:20s}To show calender".format("cal"))
    print("\t{:20s}To reboot the system".format("reboot"))
    print("\t{:20s}To shutdown the system".format("shutdown"))
    print("\t{:20s}To show status of RAM".format("ram_s"))
    print("\t{:20s}To show status of cpu".format("cpu_s"))
    print("\t{:20s}To show available disk status".format("disk_s"))
    print("\t{:20s}To show ip address of system".format("ip"))
    print("\t{:20s}To configure httpd server".format("press 1"))
    print("\t{:20s}To remote login via ssh".format("press 2"))
    print("\t{:20s}To configure Hadoop DFS".format("press 3"))
    print("\t{:20s}To upload files using scp protocol".format("press 4"))
    print("\t{:20s}To show running docker image status".format("press 5"))
    print("\t{:20s}To show available os images".format("press 6"))
    print("\t{:20s}To install docker image:".format("press 7"))
    print("\t{:20s}To Format a disk:".format("press 8")) 
    print()

def helphttpd():
    print("\t\thttpd SERVER MENU")
    print()
    print("\t{:20s}To start httpd server".format("press 1"))
    print("\t{:20s}To stop httpd server".format("press 2"))
    print("\t{:20s}To start firewall of system".format("press 3"))
    print("\t{:20s}To stop firewall of system".format("press 4"))
    print("\t{:20s}To show status of httpd server".format("press 5"))
    print()

def helphadoop():
    print("\t\tApache Hadoop Menu")
    print()
    print("\t{:20s}To Start Masternode".format("press 1"))
    print("\t{:20s}To start Datanode".format("press 2"))
    print("\t{:20s}To show dfs cluster report".format("press 3"))
    print()

def helpformat():
    print("\t\tDisk Format menu")
    print()
    print("\t{:20s}To Show no. of attached disk ".format("press 1"))
    print("\t{:20s}To make partition".format("press 2"))
    print("\t{:20s}To do format the disk".format("press 3"))
    print("\t{:20s}To mount the formatted disk".format("press 4"))
    print()
    
os.system("tput setaf 3")
print("\twelcome to mycmd menu ")
print("\t\tmy command line...\n")
print("\tEnter h for help ")
print("\tEnter q to quit")
os.system("tput setaf 2")
while True:
    os.system("tput setaf 2")
    cmd=input("\tEnter your command>>")
    if "q" in cmd:
        os.system("tput setaf 7")
        break
    elif "h" in cmd:
        help()
      
    elif "date" in cmd:
        runcmd("date")
    elif "cal" in cmd:
        runcmd("cal")
    elif "reboot" in cmd:
        os.system("init 6")

    elif "shutdown" in cmd:
        os.system("init 0")

    elif "ram_s" in cmd:
        runcmd("free -m")

    elif "cpu_s" in cmd:
        runcmd("lscpu")
    
    elif "disk_s" in cmd:
        runcmd("fdisk -l")
    elif "ip" in cmd:
        os.system("ifconfig")
    elif "1" in cmd:
        print("\t\thttpd command line...")
        print("\tEnter h for help")
        while True:
            print()
            cmd=input("\tEnter your choice:")
            print()
            if "q" in cmd:
                print("\t\tmy command line...")
                print()
                break
            elif "h" in cmd:
                helphttpd()
            elif "1" in cmd:
                out=os.system("systemctl start httpd")
                if out==0:
                    print("\tSuccessfully started httpd server.")
                    print()
                else:
                    print("\tError something goes wrong!")
                    print()

            elif "2" in cmd:
                out=os.system("systemctl stop httpd")
                if out==0:
                    print("\tSuccessfully stopped httpd server.")
                    print()
                else:
                    print("\tError something goes wrong!")
                    print()
            elif "3" in cmd:
                out=os.system("systemctl start firewalld")
                if out==0:
                    print("\tSuccessfully started firewall.")
                    print()
                else:
                    print("\tError something goes wrong!")
                    print()
            elif "4" in cmd:
                out=os.system("systemctl stop firewalld")
                if out==0:
                    print("\tSuccessfully stopped firewall.")
                    print()
                else:
                    print("\tError something goes wrong!")
                    print()
            elif "5" in cmd:
                out=sub.getstatusoutput("systemctl status httpd")
                if out[0]==0:
                    print("\tRunning...")
                    print()
                else:
                    print("\tStopped...")
                    print() 
	
    elif "2" in cmd:
        ip=input("Enter ip:")
        os.system("ssh {}".format(ip))

    elif "3" in cmd:
        print("\t\tHadoop command line...")
        print("\tEnter h for help")
        while True:
            print()
            cmd=input("\tEnter your choice:")
            print()
            if "h" in cmd:
                helphadoop()
            elif "q" in cmd:
                print("\t\tmy command line...")
                print()
                break
            elif "1" in cmd:
                inp=input("Enter ip of master node:")
                command="ssh "+inp+" hadoop-daemon.sh start namenode"
                os.system(command)
            elif "2" in cmd:
                inp=input("Enter ip of slave node:")
                command="ssh "+inp+" hadoop-daemon.sh start datanode"
                os.system(command)
            elif "3" in cmd:
                inp=input("Enter ip of master node:")
                command="ssh "+inp+" hadoop dfsadmin -report"
                os.system(command)
                
    elif "4" in cmd:
        file=input("Enter file name to be uploaded:")
        path=input("Enter path (ip address):/path ")
        os.system("scp {0} {1}".format(file,path))
    elif "5" in cmd:
        runcmd("docker ps")
    elif "6" in cmd:
        runcmd("docker images")
    elif "7" in cmd:
        print("\tAvailable Docker Images\n")
        out=sub.getoutput("docker images")
        print(out,"\n")
        img=input("\tEnter docker image name:")
        os.system("docker run -i -t {}".format(img)) 
        
    elif "8" in cmd:
        print("\t\tDisk Format process...")
        print("\tEnter h for help")

        while True:
            print()
            cmd=input("\tEnter your choice:")
            print()
            if "h" in cmd:
                helpformat()
            elif "q" in cmd:
                print("\t\tmy command line...")
                print()
                break
            elif "1" in cmd: 
                os.system("fdisk -l")
            elif "2" in cmd:
                inp=input("Enter path of disk:")
                command="fdisk "+inp
                os.system(command)
            elif "3" in cmd:
                inp=input("Enter path of disk:")
                command="mkfs.ext4"+inp
                os.system(command) 
            elif "4" in cmd:
                inp=input("Enter name of directory to mount formatted disk")
                command="mkdir /"+inp
                os.system(command) 
    
    else:
        os.system("tput setaf 1")
        print("\tinvalid command")
        os.system("tput setaf 2")
