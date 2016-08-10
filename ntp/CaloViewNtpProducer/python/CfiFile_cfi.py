import FWCore.ParameterSet.Config as cms

process = cms.Process("ntupler")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring()
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
