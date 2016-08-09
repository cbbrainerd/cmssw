import FWCore.ParameterSet.Config as cms

process = cms.Process("ntupler")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    )
)

l1variables=cms.VPSet(
    cms.PSet(tag=cms.untracked.string("Et"),
    quantity=cms.untracked.string("et")),
    cms.PSet(tag=cms.untracked.string("towerIEta"),
    quantity=cms.untracked.string("ieta")),
    cms.PSet(tag=cms.untracked.string("towerIPhi"),
    quantity=cms.untracked.string("iphi")),
    cms.PSet(tag=cms.untracked.string("rawEt"),
    quantity=cms.untracked.string("rawEt")),
    cms.PSet(tag=cms.untracked.string("isoEt"),
    quantity=cms.untracked.string("isoEt")),
    cms.PSet(tag=cms.untracked.string("shape"),
    quantity=cms.untracked.string("shape")),
    cms.PSet(tag=cms.untracked.string("footprintEt"),
    quantity=cms.untracked.string("footprintEt")),
    cms.PSet(tag=cms.untracked.string("nTT"),
    quantity=cms.untracked.string("nTT")),
    cms.PSet(tag=cms.untracked.string("hwPt"),
    quantity=cms.untracked.string("hwPt")),
    cms.PSet(tag=cms.untracked.string("hwEta"),
    quantity=cms.untracked.string("hwEta")),
    cms.PSet(tag=cms.untracked.string("hwPhi"),
    quantity=cms.untracked.string("hwPhi")),
    cms.PSet(tag=cms.untracked.string("hwQual"),
    quantity=cms.untracked.string("hwQual")),
    cms.PSet(tag=cms.untracked.string("hwIso"),
    quantity=cms.untracked.string("hwIso"))
)

process.ntpl1gamma=cms.EDProducer("L1CandidateNtpProducer",
    src=cms.InputTag("caloStage2Digis","EGamma"),variables=l1variables
)
process.ntpl1jet=cms.EDProducer("L1CandidateNtpProducer",
    src=cms.InputTag("caloStage2Digis","Jet"),variables=l1variables
)
process.ntpl1mu=cms.EDProducer("L1CandidateNtpProducer",
    src=cms.InputTag("gmtStage2Digis","Muon"),variables=l1variables
)
process.ntpl1tau=cms.EDProducer("L1CandidateNtpProducer",
    src=cms.InputTag("caloStage2Digis","Tau"),variables=l1variables
)

process.ntpmu=cms.EDProducer("CandViewNtpProducer",
    src=cms.InputTag("slimmedMuons"),
    variables=cms.VPSet(
        cms.PSet(tag=cms.untracked.string("Pt"),
            quantity=cms.untracked.string("pt")),
        cms.PSet(tag=cms.untracked.string("Eta"),
            quantity=cms.untracked.string("eta")),
        cms.PSet(tag=cms.untracked.string("Phi"),
            quantity=cms.untracked.string("phi"))
    )
)

process.p = cms.Path(process.ntpl1gamma
                    +process.ntpl1jet
                    +process.ntpl1mu
                    +process.ntpl1tau
                    +process.ntpmu
                    )
process.output=cms.OutputModule("PoolOutputModule",fileName=cms.untracked.string("file:test2.root"),SelectEvents=cms.untracked.PSet(SelectEvents=cms.vstring('p')),outputCommands=cms.untracked.vstring('keep *_*_*_ntupler'),dropMetaData=cms.untracked.string('ALL'))
process.out=cms.EndPath(process.output)
