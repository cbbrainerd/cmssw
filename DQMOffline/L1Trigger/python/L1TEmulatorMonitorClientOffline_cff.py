import FWCore.ParameterSet.Config as cms

# adapt the L1TEMUMonitorClient_cff configuration to offline DQM

#
# default configuration valid for online DQM
#
# configuration for online DQM
#    process subsystem histograms in endLumi
#    process subsystem histograms in endRun
#
# configuration for offline DQM
#    process subsystem histograms in endRun only
#


# DQM online L1 Trigger emulator client modules 
from Configuration.Eras.Modifier_stage2L1Trigger_cff import stage2L1Trigger
_importModule='DQM.L1TMonitorClient.L1TEMUMonitorClient_cff' #import this for legacy
stage2L1Trigger.toReplaceWith(_importModule,'DQM.L1TMonitorClient.L1TStage2EmulatorMonitorClient_cff') #import this for stage 2
exec('from '+_importModule+' import *')

# perform offline the quality tests in the clients in endRun only
from DQMOffline.L1Trigger.L1EmulatorQualityTestsOffline_cff import *

