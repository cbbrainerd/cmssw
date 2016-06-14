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

#config.Data.outLFNDirBase = '/srm/v2/server?SFN=/eos/uscms/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.outLFNDirBase= '/store/user/%s/' % (getUsernameFromSiteDB())

config.Data.publication = False
config.Data.outputDatasetTag = 'DoubleMuonUnderlyingEvents'

config.Site.storageSite = 'T3_US_FNALLPC'
