import FWCore.ParameterSet.Config as cms

ntptow=cms.EDProducer("CaloViewNtpProducer",
    src=cms.InputTag("towerMaker"),
    variables=cms.VPSet(
        cms.PSet(tag=cms.untracked.string("caloTowerIeta"),
            quantity=cms.untracked.string("ieta"),
            ctype=cms.untracked.string("int")),
        cms.PSet(tag=cms.untracked.string("caloTowerIphi"),
            quantity=cms.untracked.string("iphi"),
            ctype=cms.untracked.string("int")),
        cms.PSet(tag=cms.untracked.string("caloTowerTheta"),
            quantity=cms.untracked.string("theta"),
            ctype=cms.untracked.string("double")),
        cms.PSet(tag=cms.untracked.string("emEt"),
            quantity=cms.untracked.string("emEt"),
            ctype=cms.untracked.string("double")),
        cms.PSet(tag=cms.untracked.string("hadEt"),
            quantity=cms.untracked.string("hadEt"),
            ctype=cms.untracked.string("double"))
    )
)

ntpmu=cms.EDProducer("MuonViewNtpProducer",
    src=cms.InputTag("muons"),
    variables=cms.VPSet(
        cms.PSet(tag=cms.untracked.string("muonPt"),
            quantity=cms.untracked.string("pt"),
            ctype=cms.untracked.string("double")),
        cms.PSet(tag=cms.untracked.string("muonEta"),
            quantity=cms.untracked.string("eta"),
            ctype=cms.untracked.string("double")),
        cms.PSet(tag=cms.untracked.string("muonPhi"),
            quantity=cms.untracked.string("phi"),
            ctype=cms.untracked.string("double")),
        cms.PSet(tag=cms.untracked.string("muonCharge"),
            quantity=cms.untracked.string("charge"),
            ctype=cms.untracked.string("int")),
        cms.PSet(tag=cms.untracked.string("muonType"),
            quantity=cms.untracked.string("type"),
            ctype=cms.untracked.string("unsigned int"))
    )
)
