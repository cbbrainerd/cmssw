#!/bin/env python
#Crab wrapper script
#Run as python crab.py crabCommand [version]
#Do not use for crab submissions
#Be sure to source /cvmfs/cms.cern.ch/crab3/crab.sh first
import sys
import subprocess
import pickle
import imp
try:
    imp.find_module('CRABAPI')
except ImportError:
    print 'CRAB environment has not been set up. Be sure to source the correct setup script (currently `source /cvmfs/cms.cern.ch/crab3/crab.sh` for bash.)'
    raise SystemExit

try:
    f=open("versionControl.p",'r')
    versions=pickle.load(f)
    f.close()
except Exception:
    print 'Something went wrong. This is expected if `python submit_interactive.py` has not been run yet. Make sure that "versionControl.p" exists and not opened in any other process.'
    raise

if(len(sys.argv) == 1):
    print 'This script requires at least one argument. Usage:'
    print 'python crab.py crabCommand [version]'
    exit()
command=sys.argv[1]
if(len(sys.argv) > 2):
    lastVersion=sys.argv[2]
else:
    lastVersion=len(versions)
try:
    lastVersionInfo=versions['v'+str(lastVersion)]
    lastHash=lastVersionInfo[0].rstrip()
    isMC=lastVersionInfo[1] and lastVersionInfo[2]
    isData=lastVersionInfo[3] and lastVersionInfo[4]
    try:
        MCDirectory=lastVersionInfo[5]
        DataDirectory=lastVersionInfo[6]
    except KeyError:
        MCDirectory=None
        DataDirectory=None
except KeyError:
    print "Version \"v%s\" not found in dictionary. Please enter only one number for the first argument of this script, or no argument to resubmit the last submission." % lastVersion
    exit()
if (command=="submit"):
    print 'Do not use this script to submit jobs.'
    print 'Use python submit_interactive.py to submit jobs.'
    print 'Now executing python submit_interactive.py'
    subprocess.Popen("python submit_interactive.py",shell=True)
    raise SystemExit
print "Git hash of last submit: %s." % lastHash
print "Running command `crab %s` on %s." % (command,("MC and Data" if (isMC and isData) else ("MC" if isMC else ("Data" if isData else "nothing."))))

directory='./Ntupler/crab_'
version='-v'+str(lastVersion)

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException
    
    def job(directory,command):
        print 'Running command "crab %s":' % (command+" -d "+directory)
        try:
            crabCommand(command,d=directory)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)
    if isMC:
        job(MCDirectory if MCDirectory else (directory+'DYMuMu_MC_Ntupler'+version),command)
    if isData:
        job(DataDirectory if DataDirectory else (directory+'DYMuMu_Data_Ntupler'+version,command))
