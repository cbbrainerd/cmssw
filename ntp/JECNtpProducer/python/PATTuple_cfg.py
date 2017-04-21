import FWCore.ParameterSet.Config as cms

process = cms.Process("pat_tuple")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

# load the standard PAT config 
process.load("PhysicsTools.PatAlgos.patSequences_cff")

#load the coreTools of PAT
from PhysicsTools.PatAlgos.tools.coreTools import runOnData

runOnData(process,['Jets','METs'])
