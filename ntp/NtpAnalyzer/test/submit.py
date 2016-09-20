#Submits crab jobs for both MC and Data at once, based on configuration in ntp/CaloViewNtpProducer/python/crab.py
#Run as "python submit.py"
#Be sure to source /cvmfs/cms.cern.ch/crab3/crab.sh

import subprocess
import pickle
newVersion=6
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

    import ntp.NtpAnalyzer.crab as crab
    submit(crab.Data(crab.config))
    submit(crab.MC(crab.config))
