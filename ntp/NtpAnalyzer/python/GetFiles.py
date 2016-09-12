import FWCore.ParameterSet.Config as cms

import subprocess

def query(filelist,q_string,limit=0):
    limit=0 #Bug on this- malformed for limit!=0, so there you go
    try:
        lines=subprocess.check_output(["das_client.py","--query="+q_string,"--limit="+str(limit)]).splitlines()
    except subprocess.CalledProcessError:
        print "Error"
        exit
    filelist.extend(lines)
    return filelist
