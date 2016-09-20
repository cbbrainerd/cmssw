import FWCore.ParameterSet.Config as cms

process=cms.Process("NtpAnalyzerMC")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

from ntp.NtpAnalyzer.MCFileList import filesList
#from ntp.NtpAnalyzer.GetFiles import query

#q_string="file dataset=/DYToLL_M_1_TuneCUETP8M1_13TeV_pythia8/cbrainer-DYToLLNtuplesRunIISpring2016-v8-fef2920ac3ef3d99cc54880fd410ec3e/USER instance=prod/phys03"
#totalFiles=0 #0 for unlimited
#listOfFiles=cms.untracked.vstring()
#query(listOfFiles,q_string,totalFiles)

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = filesList
)

process.TFileService = cms.Service("TFileService",
    fileName=cms.string("histo_MC.root"),
    closeFileFast=cms.untracked.bool(True)
)

process.analyze = cms.EDAnalyzer('NtpAnalyzer',
    caloTowerTheta=cms.InputTag("ntptow","caloTowerTheta"),
    emEt=cms.InputTag("ntptow","emEt"),
    hadEt=cms.InputTag("ntptow","hadEt"),
    muonEta=cms.InputTag("ntpmu","muonEta"),
    muonPhi=cms.InputTag("ntpmu","muonPhi"),
    muonPt=cms.InputTag("ntpmu","muonPt"),
    caloTowerIeta=cms.InputTag("ntptow","caloTowerIeta"),
    caloTowerIphi=cms.InputTag("ntptow","caloTowerIphi"),
    muonCharge=cms.InputTag("ntpmu","muonCharge"),
    muonType=cms.InputTag("ntpmu","muonType")
)

process.p = cms.Path(process.analyze)
