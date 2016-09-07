from CRABClient.UserUtilities import getUsernameFromSiteDB
from CRABClient.UserUtilities import config as conf

config=conf()

def Data(config):
    config=common(config)
    config.General.requestName = 'DoubleMuon2016BAnalyzer'
    config.JobType.psetName = '../python/NtpAnalyzerData_cfi.py'
    config.Data.inputDataset = '/DoubleMuon/cbrainer-DoubleMuonNtuplerRun2016B-v10-3b7062a859ed6155359a055fc98137d8/USER'
    config.Data.unitsPerJob = 100
    config.Data.outputDatasetTag = 'DoubleMuonRun2016BAnalyzer'
#    config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/Cert_271036-277148_13TeV_PromptReco_Collisions16_JSON.txt'
    return config
def MC(config):
    config=common(config)
    config.General.requestName = 'DYToLLRunIISpring2016Analyzer'
    config.JobType.psetName = '../python/NtpAnalyzerMC_cfi.py'
    config.Data.inputDataset = '/DYToLL_M_1_TuneCUETP8M1_13TeV_pythia8/cbrainer-DYToLLNtuplesRunIISpring2016-v8-fef2920ac3ef3d99cc54880fd410ec3e/USER'
    config.Data.unitsPerJob = 100
    config.Data.outputDatasetTag = 'DYToLLRunIISpring2016Analysis'
    return config
def common(config):
    config=conf()
    config.General.workArea='Ntupler'
    config.General.transferOutputs = True
    config.General.transferLogs = True

    config.JobType.pluginName = 'ANALYSIS'

    config.Data.inputDBS = 'global'
    config.Data.splitting = 'FileBased'
    #config.Data.ignoreLocality = True

    config.Data.outLFNDirBase= '/store/user/%s/' % (getUsernameFromSiteDB())

    config.Data.publication = False #Not EDM files anyway, so CAN'T publish them

    config.Site.storageSite = 'T3_US_FNALLPC'
    config.Site.blacklist = ['T3_US_Rutgers'] #My jobs always seem to fail at these sites
    config.Data.inputDBS='phys03' #User-defined dataset
    return config
def debug(config):
    config.Data.totalUnits = 1
    config.Data.publication = False
    return config
