import FWCore.ParameterSet.Config as cms

process=cms.Process("NtpAnalyzerMC")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring('file:NtpMC_1.root')
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
