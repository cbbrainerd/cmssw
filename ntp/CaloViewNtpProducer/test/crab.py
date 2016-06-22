from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'DoubleMuonNtuplerRun2016B'
config.General.workArea='DoubleMuonNtuplerRun2016B'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'ANALYSIS'
config.JobType.psetName = '../python/CfiFile_cfi.py'

config.Data.inputDataset = '/DoubleMuon/Run2016B-PromptReco-v2/RECO'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.ignoreLocality = True
config.Data.unitsPerJob = 20
config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/Cert_271036-274421_13TeV_PromptReco_Collisions16_JSON_MuonPhys.txt'

#config.Data.outLFNDirBase = '/srm/v2/server?SFN=/eos/uscms/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.outLFNDirBase= '/store/user/%s/' % (getUsernameFromSiteDB())

config.Data.publication = True
config.Data.outputDatasetTag = 'DoubleMuonCaloTower'

config.Site.storageSite = 'T3_US_FNALLPC'
