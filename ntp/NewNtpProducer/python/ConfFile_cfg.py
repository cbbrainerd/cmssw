import FWCore.ParameterSet.Config as cms

process = cms.Process("ntupler")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
    #     'root://cmsxrootd.fnal.gov//store/mc/RunIISpring16MiniAODv2/DYToLL_M_1_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/FlatPU8to37HcalNZSRAW_withHLT_80X_mcRun2_asymptotic_v14_ext1-v1/00000/00B18E03-2933-E611-B8D7-0025905A60DA.root'
#        'file://../../../00B18E03-2933-E611-B8D7-0025905A60DA.root'
    )
)

    

l1variables=cms.VPSet(
    cms.PSet(tag=cms.untracked.string("Et"),
    quantity=cms.untracked.string("et")),
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

specific=cms.VPSet(
    cms.PSet(tag=cms.untracked.string("towerIEta"),
    quantity=cms.untracked.string("towerIEta")),
    cms.PSet(tag=cms.untracked.string("towerIPhi"),
    quantity=cms.untracked.string("towerIPhi")),
    cms.PSet(tag=cms.untracked.string("rawEt"),
    quantity=cms.untracked.string("rawEt")),
    cms.PSet(tag=cms.untracked.string("isoEt"),
    quantity=cms.untracked.string("isoEt")),
    cms.PSet(tag=cms.untracked.string("shape"),
    quantity=cms.untracked.string("shape")),
    cms.PSet(tag=cms.untracked.string("footprintEt"),
    quantity=cms.untracked.string("footprintEt")),
    cms.PSet(tag=cms.untracked.string("nTT"),
    quantity=cms.untracked.string("nTT"))
)

process.ntpl1gamma=cms.EDProducer("L1EGammaNtpProducer",
    src=cms.InputTag("caloStage2Digis","EGamma"),variables=l1variables+specific
)
process.ntpl1etsum=cms.EDProducer("L1EtSumNtpProducer",
    src=cms.InputTag("caloStage2Digis","EtSum"),variables=l1variables+cms.VPSet(cms.PSet(tag=cms.untracked.string("Type"),quantity=cms.untracked.string("getType")))
)
#process.ntpl1jet=cms.EDProducer("L1JetNtpProducer",
#    src=cms.InputTag("caloStage2Digis","Jet"),variables=l1variables
#)
process.ntpl1mu=cms.EDProducer("L1MuonNtpProducer",
    src=cms.InputTag("gmtStage2Digis","Muon"),variables=l1variables
)
#process.ntpl1tau=cms.EDProducer("L1TauNtpProducer",
#    src=cms.InputTag("caloStage2Digis","Tau"),variables=l1variables
#)

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
                    +process.ntpl1etsum
#                    +process.ntpl1jet
                    +process.ntpl1mu
#                    +process.ntpl1tau
                    +process.ntpmu
                    )
process.output=cms.OutputModule("PoolOutputModule",fileName=cms.untracked.string("file:test2.root"),SelectEvents=cms.untracked.PSet(SelectEvents=cms.vstring('p')),outputCommands=cms.untracked.vstring('keep *_*_*_ntupler'),dropMetaData=cms.untracked.string('ALL'))
process.out=cms.EndPath(process.output)
