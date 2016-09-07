import FWCore.ParameterSet.Config as cms

import subprocess

def query(filelist,q_string,limit=0):
    try:
        lines=subprocess.check_output(["das_client.py","--query="+q_string,"--limit="+str(limit)]).splitlines()
    except subprocess.CalledProcessError:
        print "Error"
        exit
    filelist.extend(lines)
    return filelist
