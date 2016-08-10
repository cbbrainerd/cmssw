import FWCore.ParameterSet.Config as cms

process = cms.Process("ntupler")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
#         '/store/data/Run2015E/HighPtLowerPhotons/MINIAOD/PromptReco-v1/000/261/397/00000/56F868BE-378E-E511-A87B-02163E01463E.root'
#        'root://cmsxrootd.fnal.gov//store/data/Run2016B/DoubleMuon/RECO/PromptReco-v2/000/273/150/00000/381332BB-D919-E611-A3DC-02163E0144BF.root'
#        'root://cmsxrootd.fnal.gov//store/data/Run2015D/DoubleMuon/RECO/PromptReco-v3/000/256/629/00000/363822F8-F45E-E511-A5B5-02163E01431B.root'
#        'root://cmsxrootd.fnal.gov//store/mc/RunIISpring16DR80/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/ALCARECO/StreamALCACombined-PUSpring16_ALCA_Peak_TkAlZMuMu_80X_mcRun2_asymptotic_2016_peak_v0-v1/00000/00D55FCC-AF3E-E611-929C-0CC47A78A468.root' 
#        '/DoubleMuon/Run2016E-PromptReco-v2/RECO'
        '/store/data/Run2016E/DoubleMuon/RECO/PromptReco-v2/000/276/830/00000/0EA25E84-AB4C-E611-B14B-02163E01431D.root'
    )
)


process.ntptow=cms.EDProducer("CaloViewNtpProducer",
    src=cms.InputTag("towerMaker"),
    variables=cms.VPSet(
        cms.PSet(tag=cms.untracked.string("ieta"),
            quantity=cms.untracked.string("ieta")),
        cms.PSet(tag=cms.untracked.string("theta"),
            quantity=cms.untracked.string("theta")),
        cms.PSet(tag=cms.untracked.string("emEt"),
            quantity=cms.untracked.string("emEt")),
        cms.PSet(tag=cms.untracked.string("hadEt"),
            quantity=cms.untracked.string("hadEt"))
    )
)

process.ntpmu=cms.EDProducer("CandViewNtpProducer",
    src=cms.InputTag("towerMaker"),
    variables=cms.VPSet(
        cms.PSet(tag=cms.untracked.string("pt"),
            quantity=cms.untracked.string("pt")),
        cms.PSet(tag=cms.untracked.string("eta"),
            quantity=cms.untracked.string("eta")),
        cms.PSet(tag=cms.untracked.string("phi"),
            quantity=cms.untracked.string("phi"))
    )
)

process.p = cms.Path(process.ntpmu*process.ntptow)
process.output=cms.OutputModule("PoolOutputModule",fileName=cms.untracked.string("file:test2.root"),SelectEvents=cms.untracked.PSet(SelectEvents=cms.vstring('p')),outputCommands=cms.untracked.vstring('keep *_*_*_ntupler'),dropMetaData=cms.untracked.string('ALL'))
process.out=cms.EndPath(process.output)
