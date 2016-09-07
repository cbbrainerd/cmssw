import FWCore.ParameterSet.Config as cms

process=cms.Process("NtpAnalyzerData")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

#from ntp.NtpAnalyzer.DataFileList import filesList
from ntp.NtpAnalyzer.GetFiles import query

q_string="file dataset=/DoubleMuon/cbrainer-DoubleMuonNtuplerRun2016B-v10-3b7062a859ed6155359a055fc98137d8/USER instance=prod/phys03"
totalFiles=0 #0 for unlimited
listOfFiles=cms.untracked.vstring()
query(listOfFiles,q_string,totalFiles)

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = listOfFiles
)

process.TFileService = cms.Service("TFileService",
    fileName=cms.string("histo_Data.root"),
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
