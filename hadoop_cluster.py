import os

def help():
    print("\t{:20s}To configure master node".format("press 1"))
    print("\t{:20s}To configre data node".format("press 2"))

def m_config(m_node):
    

def d_config(d_node):
    

def menu():
    os.system("tput setaf 3")
    print("\t\t hadoop cluster creation...\n\n")
    print("\tEnter h for help ")
    print("\tEnter q to quit")
    print()
    while True:
        cmd=input("Enter your choice: ")
        if "h" in cmd:
            help()
        elif "q" in cmd:
            break
        elif "1" in cmd:
            # m_node ip of master node
            m_node=input("Enter ip of master node: ")
            m_config(m_node)
         
        elif "2" in cmd:
            # num is the number of datanode  wanna add in cluster
            num=input("Enter no. of data node: ")
            for d_node in range(num):
                d_node[num]=input("Enter ip of data node: ")

        
    
        