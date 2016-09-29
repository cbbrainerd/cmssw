import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras
process = cms.Process('ntupler',eras.Run2_2016)

import ntp.CaloViewNtpProducer.DumpVariables_cfi as ntp

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
#   'root://cmsxrootd.fnal.gov//store/mc/RunIISpring16MiniAODv2/DYToLL_M_1_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/FlatPU8to37HcalNZSRAW_withHLT_80X_mcRun2_asymptotic_v14_ext1-v1/00000/00B18E03-2933-E611-B8D7-0025905A60DA.root'
#    'root://cmsxrootd.fnal.gov//store/mc/RunIISpring16DR80/DYToLL_M_1_TuneCUETP8M1_13TeV_pythia8/GEN-SIM-RAW/FlatPU8to37HcalNZSRAW_withHLT_80X_mcRun2_asymptotic_v14_ext1-v1/00000/00617C68-3632-E611-B6C5-0CC47A4D7644.root'   
    '/store/mc/RunIISpring16DR80/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RAWAODSIM/PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_v3_ext1-v1/00000/00088582-4239-E611-97B2-0CC47A78A440.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('MC Ntupler'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: v3 $')
)

process.ntptow=ntp.ntptow

process.ntpmu=ntp.ntpmu

# Output definition


#Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_v14', '')
#Use 80X_mcRun2_asymptotic_RealisticBS_25ns_13TeV2016_v0_mc for realistic beamspot?
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)

process.p = cms.Path(process.ntpmu*process.ntptow)
process.output=cms.OutputModule("PoolOutputModule",fileName=cms.untracked.string("file:NtpMC.root"),SelectEvents=cms.untracked.PSet(SelectEvents=cms.vstring('p')),outputCommands=cms.untracked.vstring('keep *_ntpmu_*_ntupler','keep *_ntptow_*_ntupler','keep *_TriggerResults_*_*'),dropMetaData=cms.untracked.string('ALL'))
process.out=cms.EndPath(process.output)

process.schedule=cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.p,process.out)
