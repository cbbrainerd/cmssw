import FWCore.ParameterSet.Config as cms

import subprocess

def query(filelist,q_string,limit=0):
    try:
        lines=subprocess.check_output(["das_client.py","--query="+q_string,"--limit=0"]).splitlines() #No limit on query: limit can be imposed below
        try:
            limit=int(limit) #If limit is invalid, just ignore it
            if (limit>0):
                lines=lines[0:limit]
        except ValueError:
            pass
    except subprocess.CalledProcessError:
        print "Error"
        exit
    filelist.extend(lines)
    return filelist
