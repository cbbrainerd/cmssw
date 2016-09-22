#Submits crab jobs
#Run as "python submit.py"
#Be sure to source /cvmfs/cms.cern.ch/crab3/crab.sh

import subprocess
import pickle
import re

import sys

skipGitStatusCheck=True #Hard-coded in for now
peeked=False

def parse(argument,nextArgument):
    return False
for index,argument in enumerate(sys.argv):
    if peeked:
        peeked=False
        continue
    if(index < len(sys.argv)-1):
        peeked=parse(argument,sys.argv[index+1])
    else:
        parse(argument,'')

    
class GenericSubmissionException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    f=open("versionControl.p",'r')
    versions=pickle.load(f)
    newVersion=len(versions)+1
    f.close()
except (EOFError,IOError):
    versions={}
    newVersion=1

if not skipGitStatusCheck:
    try:
        subprocess.check_call(["git","status","-uno"])
    except subprocess.CalledProcessError:
        print "Uncommitted changes to tracked files."
        exit()

def interactiveOptionsSubmit(config,runType):
    allGood=True
    dataset=raw_input("Type the dataset to run over if it is not default for the "+runType+" run.\n")
    if(dataset!=''):
        try:
            crab.changeDataset(config,dataset)
        except InvalidDatasetException:
            allGood=False
    if allGood:
        print "Submitting",runType,"crab job..."
        try:
            submit(config)
        except GenericSubmissionException:
            print runType,"submission failed."
            allGood=False
    return allGood

newHash=subprocess.check_output(["git","rev-parse","HEAD"])

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
            raise GenericSubmissionException
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)
            raise GenericSubmissionException

    import ntp.CaloViewNtpProducer.crab as crab
    submitType=raw_input("MC, Data, or Both?\n")
    isMC=(submitType=="MC" or submitType=="Both")
    isData=(submitType=="Data" or submitType=="Both")

    mcSubmit=False
    dataSubmit=False  

    if isMC:
        mcSubmit=interactiveOptionsSubmit(crab.MC(crab.defaultConfig),"MC")

    if isData:
        dataSubmit=interactiveOptionsSubmit(crab.Data(crab.defaultConfig),"Data")
    metaData=(newHash,isMC,mcSubmit,isData,dataSubmit)
    versions['v'+str(newVersion)]=metaData
    f=open("versionControl.p",'w')
    pickle.dump(versions,f)
