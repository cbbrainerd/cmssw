import FWCore.ParameterSet.Config as cms

ntptow=cms.EDProducer("CaloViewNtpProducer",
    src=cms.InputTag("towerMaker"),
    variables=cms.VPSet(
        cms.PSet(tag=cms.untracked.string("caloTowerIeta"),
            quantity=cms.untracked.string("ieta")),
        cms.PSet(tag=cms.untracked.string("caloTowerIphi"),
            quantity=cms.untracked.string("iphi")),
        cms.PSet(tag=cms.untracked.string("caloTowerTheta"),
            quantity=cms.untracked.string("theta")),
        cms.PSet(tag=cms.untracked.string("emEt"),
            quantity=cms.untracked.string("emEt")),
        cms.PSet(tag=cms.untracked.string("hadEt"),
            quantity=cms.untracked.string("hadEt"))
    )
)

ntpmu=cms.EDProducer("MuonViewNtpProducer",
    src=cms.InputTag("muons"),
    variables=cms.VPSet(
        cms.PSet(tag=cms.untracked.string("pt"),
            quantity=cms.untracked.string("pt")),
        cms.PSet(tag=cms.untracked.string("eta"),
            quantity=cms.untracked.string("eta")),
        cms.PSet(tag=cms.untracked.string("phi"),
            quantity=cms.untracked.string("phi")),
        cms.PSet(tag=cms.untracked.string("muonCharge"),
            quantity=cms.untracked.string("charge")),
        cms.PSet(tag=cms.untracked.string("muonType"),
            quantity=cms.untracked.string("type"))
    )
)
