import FWCore.ParameterSet.Config as cms

process = cms.Process("ntupler")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
#         '/store/data/Run2015E/HighPtLowerPhotons/MINIAOD/PromptReco-v1/000/261/397/00000/56F868BE-378E-E511-A87B-02163E01463E.root'
#        'root://cmsxrootd.fnal.gov//store/data/Run2016B/DoubleMuon/RECO/PromptReco-v2/000/273/150/00000/381332BB-D919-E611-A3DC-02163E0144BF.root'
        'root://cmsxrootd.fnal.gov//store/data/Run2015D/DoubleMuon/RECO/PromptReco-v3/000/256/629/00000/363822F8-F45E-E511-A5B5-02163E01431B.root'
    )
)


process.ntptow=cms.EDProducer("CaloViewNtpProducer",
    src=cms.InputTag("towerMaker"),
    variables=cms.VPSet(
        cms.PSet(tag=cms.untracked.string("Et"),
            quantity=cms.untracked.string("et")),
        cms.PSet(tag=cms.untracked.string("iEta"),
            quantity=cms.untracked.string("ieta")),
        cms.PSet(tag=cms.untracked.string("iPhi"),
            quantity=cms.untracked.string("iphi")),
        cms.PSet(tag=cms.untracked.string("EmEt"),
            quantity=cms.untracked.string("emEt")),
        cms.PSet(tag=cms.untracked.string("HadEt"),
            quantity=cms.untracked.string("hadEt")),
        cms.PSet(tag=cms.untracked.string("OuterEt"),
            quantity=cms.untracked.string("outerEt")),
        cms.PSet(tag=cms.untracked.string("EmLvl1"),
            quantity=cms.untracked.string("emLvl1")),
        cms.PSet(tag=cms.untracked.string("HadLvl1"),
            quantity=cms.untracked.string("hadLv11"))
    )
)

process.ntpmu=cms.EDProducer("CandViewNtpProducer",
    src=cms.InputTag("towerMaker"),
    variables=cms.VPSet(
        cms.PSet(tag=cms.untracked.string("Pt"),
            quantity=cms.untracked.string("pt")),
        cms.PSet(tag=cms.untracked.string("Eta"),
            quantity=cms.untracked.string("eta")),
        cms.PSet(tag=cms.untracked.string("Phi"),
            quantity=cms.untracked.string("phi"))
    )
)

process.p = cms.Path(process.ntpmu*process.ntptow)
process.output=cms.OutputModule("PoolOutputModule",fileName=cms.untracked.string("file:test2.root"),SelectEvents=cms.untracked.PSet(SelectEvents=cms.vstring('p')),outputCommands=cms.untracked.vstring('keep *_*_*_ntupler'),dropMetaData=cms.untracked.string('ALL'))
process.out=cms.EndPath(process.output)
