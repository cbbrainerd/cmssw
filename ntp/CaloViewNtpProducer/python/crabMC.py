from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'DYToLLNtuplerRunIISpring2016'
config.General.workArea='Ntupler'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'ANALYSIS'
config.JobType.psetName = '../python/NtpMC_cfi.py'

config.Data.inputDataset = '/DYToLL_M_1_TuneCUETP8M1_13TeV_pythia8/RunIISpring16DR80-FlatPU8to37HcalNZSRAW_withHLT_80X_mcRun2_asymptotic_v14_ext1-v1/GEN-SIM-RAW'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'

#config.Data.ignoreLocality = True
config.Data.unitsPerJob = 4

#config.Data.outLFNDirBase = '/srm/v2/server?SFN=/eos/uscms/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.outLFNDirBase= '/store/user/%s/' % (getUsernameFromSiteDB())

#For testing purposes:
#config.Data.totalUnits= 10

config.Data.publication = True #Set to false for testing purposes
config.Data.outputDatasetTag = 'DYToLLNtuplesRunIISpring2016'

config.Site.storageSite = 'T3_US_FNALLPC'
config.Site.blacklist = ['T3_US_Rutgers'] #My jobs always seem to fail at these sites
