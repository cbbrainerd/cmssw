#Queries crab status for both MC and Data for the last run version, or the version chosen as an optional first argument
#Run as python status.py [version]
#Be sure to source /cvmfs/cms.cern.ch/crab3/crab.sh first
import sys
import subprocess
import pickle

f=open("versionControl.p",'r')
versions=pickle.load(f)
f.close()
if(len(sys.argv) > 1):
    lastVersion=sys.argv[1]
else:
    lastVersion=len(versions)
try:
    lastHash=versions['v'+str(lastVersion)]
except KeyError:
    print "Version \"v%s\" not found in dictionary. Please enter only one number for the first argument of this script, or no argument to see the git status of the last submission." % lastVersion
    exit()
print "Git hash of last submit: %s." % lastHash

directory='./Ntupler/crab_'
version='-v'+str(lastVersion)

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException
    
    def status(directory):
        try:
            crabCommand('status',d=directory)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)
    status(directory+'DYToLLNtuplerRunIISpring2016'+version)
    status(directory+'DoubleMuonNtuplerRun2016B'+version)
