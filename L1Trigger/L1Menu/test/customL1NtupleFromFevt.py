import FWCore.ParameterSet.Config as cms

from L1Trigger.L1Menu.customL1Ntuple_cfg import *

# process.p.remove(process.l1RecoTreeProducer)
#process.p.remove(process.l1MuonRecoTreeProducer)
process.p.remove(process.l1MenuTreeProducer)

process.p.remove(process.gtEvmDigis)

process.l1MuonRecoTreeProducer.runOnPostLS1 = True # CB hack for now so that pre and post LS1 have same muon config
process.l1MuonRecoTreeProducer.triggerMatching = True

# edit here
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

readFiles.extend( [ 
        "/store/express/Run2015A/ExpressPhysics/FEVT/Express-v1/000/246/908/00000/D0E84633-D709-E511-92D8-02163E014374.root"
        ] )

process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.MessageLogger.cerr.threshold = 'ERROR'

