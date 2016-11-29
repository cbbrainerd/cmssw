import FWCore.ParameterSet.Config as cms

# adapt the L1TEmulatorMonitor_cff configuration to offline DQM

# DQM online L1 Trigger emulator modules 

from Configuration.Eras.Modifier_stage2L1Trigger_cff import stage2L1Trigger
_importModule='DQM.L1TMonitor.L1TEmulatorMonitor_cff' #import this for legacy
stage2L1Trigger.toReplaceWith(_importModule,'DQM.L1TMonitor.L1TStage2Emulator_cff') #import this for stage2
exec('from '+_importModule+' import *')
