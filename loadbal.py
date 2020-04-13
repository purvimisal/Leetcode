import sys
import time
from datetime import datetime

from os import path

servers = {}
pstate = ''

def main():
    if len(sys.argv) == 1:
        print("No Arguments Passed.. Exiting...")
        print("Usage: python loadbal.py Server:Size")
        exit()

    if len(sys.argv) > 1:
        if (':' in sys.argv[1]):
            ##print("Good Job")

            noofservers = len(sys.argv) - 1

            for server in range(noofservers):
                ##print(server + 1)
            ## print('Argument Passed is ', sys.argv[server + 1])
                tempdata = sys.argv[server + 1]
                tempserver = tempdata.split(':')[0]
                tempsize = int(tempdata.split(':')[1])
                # create Dict for all servers and sizes
                servers[tempserver] = tempsize

        else :
            print("Usage: python loadbal.py Server:Size")
            print("Server & Size Not Mentioned.. Exiting...")
            exit()

    ## print("\nSorting Servers by Size \n")

    newfile = 'servers.config'
    if not path.exists(newfile):
        fw = open(newfile, "w+")
    ## print(newfile)
        for server in sorted(servers, key = servers.get, reverse = True):
            ##print('Server and its Size', server, servers[server])
            newrecord = server + ":" + str(servers[server]) + '\n'
            fw.write(newrecord)
        fw.close()
    ## print('Doing Transaction')
    pstate = prevstate()
    transdata()




def checkzero():
    allzero = 0
    print("Checking zero")
    with open("servers.config") as fr:
        for rec in fr:
            (vserver, vsize) = rec.split(':')
            transfile = vserver + '.trans'
            with open(transfile) as fo:
                for rec in fo:
                    if int(rec) == 0:
                        allzero = 1
                    else :
                        allzero = 0



    if allzero == 1:
        with open("servers.config") as fr:
            for rec in fr:
                (vserver, vsize) = rec.split(':')
                transfile = vserver + '.trans'
            transrecord = str(vsize)
            fw = open(transfile, "w+")
            fw.write(transrecord)
            fw.close()


def prevstate():

    newfile = 'prev.state'

    pstate = '#'

    if not path.exists(newfile):
        fw = open(newfile, "w+")
        newrecord = '#'
        fw.write(newrecord)
        fw.close()
    else :
        with open("prev.state") as fs:
            for state in fs:
                pstate = state
    return pstate



def changestate(nstate):
    newfile = 'prev.state'
    fw = open(newfile, "w+")
    newrecord = nstate
    fw.write(newrecord)
    fw.close()



def assignstate():
    currentstate = ''
    newstate = ''
    confdict = {}
    with open("prev.state") as fs:
        for state in fs:
            currentstate = state
    print('Current State', currentstate)
    with open("servers.config") as fr:
        for rec in fr:
            (vserver, vsize) = rec.split(':')
            confdict[vserver] = int(vsize.rstrip('\n'))
        for vvserver, vvsize in confdict.items():
            if currentstate == vvserver:
                continue
            else :
                if vvserver == confdict.keys()[-1]:
                    newstate = confdict.keys()[0]
                else :
                    newstate = vvserver
            break
    print('NEW State', newstate)



def transdata():
    ##print('Using Server Optimization')
    configdict = {}
    displayed = 0
    vprevstate = ''
    vnewstate = ''
    with open("servers.config") as fr:
        for rec in fr:
            (vserver, vsize) = rec.split(':')
            configdict[vserver] = int(vsize.rstrip('\n'))
    ## print('ConfigDict is ', configdict)
    ## print('Reading Dictionery item by item')
    for transserver, vvsize in configdict.items():
        ##print transserver, vvsize
        newtransfile = transserver + '.trans'
        if not path.exists(newtransfile):
        ##print(newtransfile)
            transrecord = str(vvsize)
            fw = open(newtransfile, "w+")
            fw.write(transrecord)
            fw.close()
    checkzero()
    vprevstate = prevstate()
    vnewstate = assignstate()
    #    if vprevstate = '#':
        #vnewstate = assignstate()
    print("Previous Sate", vprevstate)
    if displayed == 0:
        for transserver, vvsize in configdict.items():
        ##print transserver, vvsize
            if transserver == vnewstate:
                break
            newtransfile = transserver + '.trans'
            if displayed == 0:
                with open(newtransfile) as fo:
                    for rec in fo:
                        if rec == 0:
                            displayed = 0
                            continue
                        else :
                            displayed = 1
                    print("Displayed - ", transserver)
                    changestate(transserver)
                    NewCount = int(rec) - 1
                    transrecord = str(NewCount)
                    if NewCount >= 0:
                        fn = open(newtransfile, "w")
                        fn.write(transrecord)
                        fn.close()
                        break




if __name__ == "__main__":

    main()