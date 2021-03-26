#!/usr/bin/python3

import os
import linux_command as l
import hadoop_cluster as h
def main_menu():
    print("\t{:20s}To run Linux commands".format("press 1"))
    print("\t{:20s}To create/configure hadoop cluster".format("press 2"))
    print("\t{:20s}To reboot the system".format("press 3"))
    
if __name__=='__main__':
    os.system("tput setaf 3")
    print("\twelcome to mycmd menu ")
    print("\t\tmy command line...\n")
    print("\tEnter h for help ")
    print("\tEnter q to quit")
    print()
    os.system("tput setaf 2")
    while True:
        os.system("tput setaf 2")
        cmd=input("\tEnter your choice>> ")
        if "q" in cmd:
            os.system("tput setaf 7")
            break
        elif "h" in cmd:
            main_menu()
       
        elif "1" in cmd:
            l.menu()
        elif "2" in cmd:
            h.menu()


