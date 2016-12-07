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
    imp.find_module('CRABAPI') #If CRAB setup script has not been sourced, exit without wasting any time
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
    print 'python crab.py crabCommand [crabOptions] [version (just a number)]'
    exit()
command=sys.argv[1]
crabCmdOpts=[]
if(len(sys.argv) > 2):
    lastVersion=[]
    for x in sys.argv[2:]:
        try:
            int(x)
            versions['v'+str(x)]
        except ValueError: #If it is not an integer, it must be a crab option. If it's not a valid one, let crab handle the error
            crabCmdOpts.append(x)
        except KeyError:
            print 'Version v'+str(x)+' does not exist.'
            raise SystemExit
        else:
            lastVersion.append(str(x))
    if not lastVersion:
        lastVersion=[len(versions)]
else:
    lastVersion=[len(versions)]
lastHash=[]
isMC=[]
isData=[]
MCDirectory=[]
DataDirectory=[]
for version in lastVersion:
    try:
        lastVersionInfo=versions['v'+str(version)]
        lastHash.append(lastVersionInfo[0].rstrip())
        isMC.append(lastVersionInfo[1] and lastVersionInfo[2])
        isData.append(lastVersionInfo[3] and lastVersionInfo[4])
        MCDirectory.append(lastVersionInfo[5])
        DataDirectory.append(lastVersionInfo[6])
    except KeyError:
        print "Version \"v%s\" not found in dictionary. Please enter only one number for the first argument of this script, or no argument to resubmit the last submission." % version
        raise SystemExit
if (command=="submit"):
    print 'Do not use this script to submit jobs.'
    print 'Use python submit_interactive.py to submit jobs.'
    print 'Now executing python submit_interactive.py'
    subprocess.Popen("python submit_interactive.py",shell=True)
    raise SystemExit
print "Git hashes of given submits: %s." % lastHash
print "Running command `crab %s%s` on %s." % (command,' '+' '.join(crabCmdOpts) if crabCmdOpts else '',("MC and Data" if (isMC and isData) else ("MC" if isMC else ("Data" if isData else "nothing."))))

directory='./Ntupler/crab_'
version='-v'+str(lastVersion)

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException
    
    def job(directory,command,crabCmdOpts):
        print 'Running command "crab %s%s":' % ((command+" -d "+directory),' '+' '.join(crabCmdOpts) if crabCmdOpts else '')
        try:
            crabCommand(command,d=directory,*crabCmdOpts)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)
    for isMC_,isData_,MCDirectory_,DataDirectory_ in zip(isMC,isData,MCDirectory,DataDirectory):
        if isMC_:
            job(MCDirectory_,command,crabCmdOpts)
        if isData_:
            job(DataDirectory_,command,crabCmdOpts)
