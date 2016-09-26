#Submits crab jobs for both MC and Data at once, based on configuration in ntp/CaloViewNtpProducer/python/crab.py
#Run as "python submit.py"
#Be sure to source /cvmfs/cms.cern.ch/crab3/crab.sh

#Version control not updated. Don't use this yet
raise SystemExit

import subprocess
import pickle
try:
    f=open("versionControl.p",'r')
    versions=pickle.load(f)
    newVersion=len(versions)+1
    f.close()
except IOError:
    versions={}
    newVersion=1

try:
    subprocess.check_call(["git","status","-uno"])
except subprocess.CalledProcessError:
    print "Uncommitted changes to tracked files."
    exit()

newHash=subprocess.check_output(["git","rev-parse","HEAD"])

versions['v'+str(newVersion)]=newHash

f=open("versionControl.p",'w')
pickle.dump(versions,f)

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException
    
    def submit(config):
        config.General.requestName = config.General.requestName+'-v'+str(newVersion)
        config.Data.outputDatasetTag = config.Data.outputDatasetTag+'-v'+str(newVersion)
        try:
            crabCommand('submit',config=config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    import ntp.CaloViewNtpProducer.crab as crab
    submit(crab.Data(crab.config))
    submit(crab.MC(crab.config))
