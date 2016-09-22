from CRABClient.UserUtilities import getUsernameFromSiteDB
from CRABClient.UserUtilities import config as conf

import re
datasetPattern=re.compile(r"^(/[-a-zA-Z0-9_]+){3}$") #Sanity check that dataset name is valid for user input

defaultConfig=conf()

class InvalidDatasetException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def Data(config):
    config=common(config)
    config.General.requestName = 'DoubleMuonNtuplerRun2016B'
    config.JobType.psetName = '../python/NtpData_cfi.py'
    config.Data.inputDataset = '/DoubleMuon/Run2016E-PromptReco-v2/RECO'
    config.Data.unitsPerJob = 100
    config.Data.outputDatasetTag = 'DataNtuples1'
    config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/Cert_271036-277148_13TeV_PromptReco_Collisions16_JSON.txt'
    return config
def MC(config):
    config=common(config)
    config.General.requestName = 'DYToLLNtuplerRunIISpring2016'
    config.JobType.psetName = '../python/NtpMC_cfi.py'
    config.Data.inputDataset = '/DYToLL_M_1_TuneCUETP8M1_13TeV_pythia8/RunIISpring16DR80-FlatPU8to37HcalNZSRAW_withHLT_80X_mcRun2_asymptotic_v14_ext1-v1/GEN-SIM-RAW'
    config.Data.unitsPerJob = 100
    config.Data.outputDatasetTag = 'MCNtuples'
    return config
def common(config):
    config=conf()
    config.General.workArea='Ntupler'
    config.General.transferOutputs = True
    config.General.transferLogs = True

    config.JobType.pluginName = 'ANALYSIS'

    config.Data.inputDBS = 'global'
    config.Data.splitting = 'LumiBased'
    #config.Data.ignoreLocality = True

    config.Data.outLFNDirBase= '/store/user/%s/' % (getUsernameFromSiteDB())

    config.Data.publication = True

    config.Site.storageSite = 'T3_US_FNALLPC'
    config.Site.blacklist = ['T3_US_Rutgers'] #My jobs always seem to fail at these sites
    return config
def debug(config):
    config.Data.totalUnits = 1
    config.Data.publication = False
    return config

def changeDataset(config,dataset):
    if(not datasetPattern.match(dataset)):
        print("Dataset ",dataset,r" is invalid. Valid datasets are of the form ^(/[-a-zA-Z0-9_]+")
        raise InvalidDatasetException("Invalid Dataset!")
    else:
        config.Data.inputDataset=dataset
    return config
