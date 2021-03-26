import os  #inclusion of os module
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

def menu():
    os.system("tput setaf 3")
    print("\t\tmy Linux command line...\n\n")
    print("\tEnter h for help ")
    print("\tEnter q to quit")
    os.system("tput setaf 2")
    while True:
        os.system("tput setaf 2")
        cmd=input("\tEnter your choice>> ")
        print()
        if "q" in cmd:
            print("\t\tmy command line...\n\n")
            os.system("tput setaf 3")
            break
        elif "h" in cmd:
            help()
        elif "1" in cmd:
            runcmd("date")
        elif "2" in cmd:
            runcmd("cal")
        #To reboot the system
        elif "3" in cmd:
            os.system("init 6")
        #To shutdown the system
        elif "4" in cmd:
            os.system("init 0")
        #To check the status of memory
        elif "5" in cmd:
            runcmd("free -m")
        #To check the cpu status
        elif "6" in cmd:
            os.system("lscpu")

        elif "7" in cmd:
            os.system("fdisk -l")
        #To check the cpu status
        elif "8" in cmd:
            os.system("ifconfig enp0s3")

def help(): #help menu for linux commands
    print("\t{:20s}To show date & time".format("press 1"))
    print("\t{:20s}To show calender".format("press 2"))
    print("\t{:20s}To reboot the system".format("press 3"))
    print("\t{:20s}To shutdown the system".format("press 4"))
    print("\t{:20s}To show status of RAM".format("press 5"))
    print("\t{:20s}To show status of cpu".format("press 6"))
    print("\t{:20s}To show available disk status".format("press 7"))
    print("\t{:20s}To show ip address of system".format("press 8"))



