from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'DoubleMuonNtuplerRun2016B'
config.General.workArea='Ntupler'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'ANALYSIS'
config.JobType.psetName = '../python/NtpData_cfi.py'

config.Data.inputDataset = '/DoubleMuon/Run2016E-PromptReco-v2/RECO'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
#config.Data.ignoreLocality = True
config.Data.unitsPerJob = 2
config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/Cert_271036-277148_13TeV_PromptReco_Collisions16_JSON.txt' #Update this for later runs of course

#config.Data.outLFNDirBase = '/srm/v2/server?SFN=/eos/uscms/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.outLFNDirBase= '/store/user/%s/' % (getUsernameFromSiteDB())

config.Data.publication = True
config.Data.outputDatasetTag = 'DoubleMuonNtuplerRun2016B'

config.Site.storageSite = 'T3_US_FNALLPC'
config.Site.blacklist = ['T3_US_Rutgers'] #My jobs always seem to fail at these sites
