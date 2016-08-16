import FWCore.ParameterSet.Config as cms

ntptow=cms.EDProducer("CaloViewNtpProducer",
    src=cms.InputTag("towerMaker"),
    variables=cms.VPSet(
#        cms.PSet(tag=cms.untracked.string("caloTowerIeta"),
#            quantity=cms.untracked.string("ieta"),
#            Ctype=cms.untracked.string("int")),
#        cms.PSet(tag=cms.untracked.string("caloTowerIphi"),
#            quantity=cms.untracked.string("iphi"),
#            Ctype=cms.untracked.string("int")),
        cms.PSet(tag=cms.untracked.string("caloTowerTheta"),
            quantity=cms.untracked.string("theta"),
            Ctype=cms.untracked.string("double")),
        cms.PSet(tag=cms.untracked.string("emEt"),
            quantity=cms.untracked.string("emEt"),
            Ctype=cms.untracked.string("double")),
        cms.PSet(tag=cms.untracked.string("hadEt"),
            quantity=cms.untracked.string("hadEt"),
            Ctype=cms.untracked.string("double"))
    )
)

ntpmu=cms.EDProducer("MuonViewNtpProducer",
    src=cms.InputTag("muons"),
    variables=cms.VPSet(
        cms.PSet(tag=cms.untracked.string("muonPt"),
            quantity=cms.untracked.string("pt"),
            Ctype=cms.untracked.string("double")),
        cms.PSet(tag=cms.untracked.string("muonEta"),
            quantity=cms.untracked.string("eta"),
            Ctype=cms.untracked.string("double")),
        cms.PSet(tag=cms.untracked.string("muonPhi"),
            quantity=cms.untracked.string("phi"),
            Ctype=cms.untracked.string("double")),
#        cms.PSet(tag=cms.untracked.string("muonCharge"),
#            quantity=cms.untracked.string("charge"),
#            Ctype=cms.untracked.string("int")),
        cms.PSet(tag=cms.untracked.string("muonType"),
            quantity=cms.untracked.string("type"),
            Ctype=cms.untracked.string("unsignedint"))
    )
)
