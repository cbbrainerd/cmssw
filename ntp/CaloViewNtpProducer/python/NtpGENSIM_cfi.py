# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: NtpGENSIM_cfi.py -s DIGI,L1,DIGI2RAW,HLT,RAW2DIGI,RECO --no_exec --conditions=76X_mcRun2_asymptotic_v12 --era Run2_2016
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras
process = cms.Process('ntupler',eras.Run2_25ns)

import ntp.CaloViewNtpProducer.DumpVariables_cfi as ntp
process.ntptow=ntp.ntptow
process.ntpmu=ntp.ntpmu

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring('/store/mc/RunIISummer15GS/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/GEN-SIM/MCRUN2_71_V1_ext1-v1/00000/00231700-2DC0-E511-A64C-AC162DA6E2F8.root'),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop *_genParticles_*_*', 
        'drop *_genParticlesForJets_*_*', 
        'drop *_kt4GenJets_*_*', 
        'drop *_kt6GenJets_*_*', 
        'drop *_iterativeCone5GenJets_*_*', 
        'drop *_ak4GenJets_*_*', 
        'drop *_ak7GenJets_*_*', 
        'drop *_ak8GenJets_*_*', 
        'drop *_ak4GenJetsNoNu_*_*', 
        'drop *_ak8GenJetsNoNu_*_*', 
        'drop *_genCandidatesForMET_*_*', 
        'drop *_genParticlesForMETAllVisible_*_*', 
        'drop *_genMetCalo_*_*', 
        'drop *_genMetCaloAndNonPrompt_*_*', 
        'drop *_genMetTrue_*_*', 
        'drop *_genMetIC5GenJs_*_*'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('NtpGENSIM_cfi.py nevts:1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.output=cms.OutputModule("PoolOutputModule",fileName=cms.untracked.string("file:NtpMC.root"),SelectEvents=cms.untracked.PSet(SelectEvents=cms.vstring('p')),outputCommands=cms.untracked.vstring('keep *_ntpmu_*_ntupler','keep *_ntptow_*_ntupler','keep *_TriggerResults_*_ntupler'),dropMetaData=cms.untracked.string('ALL'))
process.output_step=cms.EndPath(process.output)
#process.out=cms.EndPath(process.output)
#process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
#    dataset = cms.untracked.PSet(
#        dataTier = cms.untracked.string(''),
#        filterName = cms.untracked.string('')
#    ),
#    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
#    fileName = cms.untracked.string('NtpGENSIM_cfi_py_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_RECO.root'),
#    outputCommands = process.RECOSIMEventContent.outputCommands,
#    splitLevel = cms.untracked.int32(0)
#)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_2016_miniAODv2_v1', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
#process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)
process.p = cms.Path(process.ntpmu*process.ntptow)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.raw2digi_step,process.reconstruction_step,process.p,process.output_step,process.endjob_step])

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforFullSim 

#call to customisation function customizeHLTforFullSim imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforFullSim(process)

# End of customisation functions

