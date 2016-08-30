#Crab wrapper script
#Run as python crab.py crabCommand [version]
#Do not use for crab submissions
#Be sure to source /cvmfs/cms.cern.ch/crab3/crab.sh first
import sys
import subprocess
import pickle

f=open("versionControl.p",'r')
versions=pickle.load(f)
f.close()
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
    lastHash=versions['v'+str(lastVersion)]
except KeyError:
    print "Version \"v%s\" not found in dictionary. Please enter only one number for the first argument of this script, or no argument to resubmit the last submission." % lastVersion
    exit()
if (command=="submit"):
    print 'Do not use this script to submit jobs.'
    print 'Use python submit.py to submit jobs.'
    exit()
print "Git hash of last submit: %s." % lastHash
print "Running command `crab %s` on all jobs." % command

directory='./Ntupler/crab_'
version='-v'+str(lastVersion)

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException
    
    def job(directory,command):
        try:
            crabCommand(command,d=directory)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)
    job(directory+'DYToLLNtuplerRunIISpring2016'+version,command)
    job(directory+'DoubleMuonNtuplerRun2016B'+version,command)
