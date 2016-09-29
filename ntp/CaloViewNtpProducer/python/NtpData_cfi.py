import FWCore.ParameterSet.Config as cms

import ntp.CaloViewNtpProducer.DumpVariables_cfi as ntp

process = cms.Process("ntupler")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
#         '/store/data/Run2015E/HighPtLowerPhotons/MINIAOD/PromptReco-v1/000/261/397/00000/56F868BE-378E-E511-A87B-02163E01463E.root'
#        'root://cmsxrootd.fnal.gov//store/data/Run2016B/DoubleMuon/RECO/PromptReco-v2/000/273/150/00000/381332BB-D919-E611-A3DC-02163E0144BF.root'
#        'root://cmsxrootd.fnal.gov//store/data/Run2015D/DoubleMuon/RECO/PromptReco-v3/000/256/629/00000/363822F8-F45E-E511-A5B5-02163E01431B.root'
#        'root://cmsxrootd.fnal.gov//store/mc/RunIISpring16DR80/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/ALCARECO/StreamALCACombined-PUSpring16_ALCA_Peak_TkAlZMuMu_80X_mcRun2_asymptotic_2016_peak_v0-v1/00000/00D55FCC-AF3E-E611-929C-0CC47A78A468.root' 
#        '/DoubleMuon/Run2016E-PromptReco-v2/RECO'
#        '/store/data/Run2016E/DoubleMuon/RECO/PromptReco-v2/000/276/830/00000/0EA25E84-AB4C-E611-B14B-02163E01431D.root'
#         'file://./DataTestFile.root'
    )
)

process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Data Ntupler'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: v3 $')
)

process.ntptow=ntp.ntptow

process.ntpmu=ntp.ntpmu

process.p = cms.Path(process.ntpmu*process.ntptow)
process.output=cms.OutputModule("PoolOutputModule",fileName=cms.untracked.string("file:NtpData.root"),SelectEvents=cms.untracked.PSet(SelectEvents=cms.vstring('p')),outputCommands=cms.untracked.vstring('keep *_*_*_ntupler','keep *_TriggerResults_*_*'),dropMetaData=cms.untracked.string('ALL'))
process.out=cms.EndPath(process.output)
