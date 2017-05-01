import FWCore.ParameterSet.Config as cms

# L1 Trigger DQM sequence for offline DQM
#
# used by DQM GUI: DQM/Configuration 
#
#
#
# standard RawToDigi sequence and RECO sequence must be run before the L1 Trigger modules, 
# labels from the standard sequence are used as default for the L1 Trigger DQM modules
#
# V.M. Ghete - HEPHY Vienna - 2011-01-02 
#                       
                      

#
# DQM L1 Trigger in offline environment
#

import DQMServices.Components.DQMEnvironment_cfi
dqmEnvL1T = DQMServices.Components.DQMEnvironment_cfi.dqmEnv.clone()
dqmEnvL1T.subSystemFolder = 'L1T'

# DQM online L1 Trigger modules, with offline configuration 
from DQMOffline.L1Trigger.L1TMonitorOffline_cff import *
from DQMOffline.L1Trigger.L1TMonitorClientOffline_cff import *


# DQM offline L1 Trigger versus Reco modules

import DQMServices.Components.DQMEnvironment_cfi
dqmEnvL1TriggerReco = DQMServices.Components.DQMEnvironment_cfi.dqmEnv.clone()
dqmEnvL1TriggerReco.subSystemFolder = 'L1T/L1TriggerVsReco'

#
# DQM L1 Trigger Emulator in offline environment
# Run also the L1HwVal producers (L1 Trigger emulators)
#

import DQMServices.Components.DQMEnvironment_cfi
dqmEnvL1TEMU = DQMServices.Components.DQMEnvironment_cfi.dqmEnv.clone()
dqmEnvL1TEMU.subSystemFolder = 'L1TEMU'

# DQM Offline Step 1 cfi/cff imports
from DQMOffline.L1Trigger.L1TRate_Offline_cfi import *
from DQMOffline.L1Trigger.L1TSync_Offline_cfi import *
from DQMOffline.L1Trigger.L1TEmulatorMonitorOffline_cff import *  

# DQM Offline Step 2 cfi/cff imports
from DQMOffline.L1Trigger.L1TEmulatorMonitorClientOffline_cff import *


# Stage1 customization
RunIl1TdeRCT = l1TdeRCT.clone()
RunIl1TdeRCT.rctSourceData = 'gctDigis'

RunIl1TdeRCTfromRCT = l1TdeRCTfromRCT.clone()
RunIl1TdeRCTfromRCT.rctSourceData = 'gctDigis'

RunIl1tRct = l1tRct.clone()
RunIl1tRct.rctSource = 'gctDigis'

RunIl1tRctfromRCT = l1tRctfromRCT.clone()
RunIl1tRctfromRCT.rctSource = 'gctDigis'

RunIl1tPUM = l1tPUM.clone()
RunIl1tPUM.regionSource = cms.InputTag("gctDigis")

RunIl1tStage1Layer2 = l1tStage1Layer2.clone()
RunIl1tStage1Layer2.gctCentralJetsSource = cms.InputTag("gctDigis","cenJets")
RunIl1tStage1Layer2.gctForwardJetsSource = cms.InputTag("gctDigis","forJets")
RunIl1tStage1Layer2.gctTauJetsSource = cms.InputTag("gctDigis","tauJets")
RunIl1tStage1Layer2.gctIsoTauJetsSource = cms.InputTag("","")       
RunIl1tStage1Layer2.gctEnergySumsSource = cms.InputTag("gctDigis")
RunIl1tStage1Layer2.gctIsoEmSource = cms.InputTag("gctDigis","isoEm")
RunIl1tStage1Layer2.gctNonIsoEmSource = cms.InputTag("gctDigis","nonIsoEm")
RunIl1tStage1Layer2.stage1_layer2_ = cms.bool(False)

RunIdqmL1ExtraParticlesStage1 = dqmL1ExtraParticlesStage1.clone()
RunIdqmL1ExtraParticlesStage1.etTotalSource = 'gctDigis'
RunIdqmL1ExtraParticlesStage1.nonIsolatedEmSource = 'gctDigis:nonIsoEm'
RunIdqmL1ExtraParticlesStage1.etMissSource = 'gctDigis'
RunIdqmL1ExtraParticlesStage1.htMissSource = 'gctDigis'
RunIdqmL1ExtraParticlesStage1.forwardJetSource = 'gctDigis:forJets'
RunIdqmL1ExtraParticlesStage1.centralJetSource = 'gctDigis:cenJets'
RunIdqmL1ExtraParticlesStage1.tauJetSource = 'gctDigis:tauJets'
RunIdqmL1ExtraParticlesStage1.isolatedEmSource = 'gctDigis:isoEm'
RunIdqmL1ExtraParticlesStage1.etHadSource = 'gctDigis'
RunIdqmL1ExtraParticlesStage1.hfRingEtSumsSource = 'gctDigis'
RunIdqmL1ExtraParticlesStage1.hfRingBitCountsSource = 'gctDigis'
RunIl1ExtraDQMStage1 = l1ExtraDQMStage1.clone()
RunIl1ExtraDQMStage1.stage1_layer2_ = cms.bool(False)
RunIl1ExtraDQMStage1.L1ExtraIsoTauJetSource_ = cms.InputTag("fake")

RunIl1compareforstage1 = l1compareforstage1.clone()
RunIl1compareforstage1.GCTsourceData = cms.InputTag("gctDigis")
RunIl1compareforstage1.GCTsourceEmul = cms.InputTag("valGctDigis")
RunIl1compareforstage1.stage1_layer2_ = cms.bool(False)

RunIl1TdeStage1Layer2 = l1TdeStage1Layer2.clone()
RunIl1TdeStage1Layer2.DataEmulCompareSource = cms.InputTag("RunIl1compareforstage1")

RunIvalStage1GtDigis = valStage1GtDigis.clone()
RunIvalStage1GtDigis.GctInputTag = 'gctDigis'

RunIl1Stage1GtHwValidation = l1Stage1GtHwValidation.clone()
RunIl1Stage1GtHwValidation.L1GtEmulDaqInputTag = cms.InputTag("RunIvalStage1GtDigis")
RunIl1Stage1GtHwValidation.L1GtEmulEvmInputTag = cms.InputTag("RunIl1Stage1GtHwValidation")

from Configuration.Eras.Modifier_stage1L1Trigger_cff import stage1L1Trigger
stage1L1Trigger.toModify(RunIl1TdeRCT, rctSourceData = 'caloStage1Digis')
stage1L1Trigger.toModify(RunIl1TdeRCTfromRCT, rctSourceData = 'rctDigis')
stage1L1Trigger.toModify(RunIl1tRct, rctSource = 'caloStage1Digis')
stage1L1Trigger.toModify(RunIl1tRctfromRCT, rctSource = 'rctDigis')
stage1L1Trigger.toModify(RunIl1tPUM, regionSource = cms.InputTag("rctDigis"))

stage1L1Trigger.toModify(RunIl1tStage1Layer2, stage1_layer2_ = cms.bool(True))
stage1L1Trigger.toModify(RunIl1tStage1Layer2, gctCentralJetsSource = cms.InputTag("caloStage1LegacyFormatDigis","cenJets"))
stage1L1Trigger.toModify(RunIl1tStage1Layer2, gctForwardJetsSource = cms.InputTag("caloStage1LegacyFormatDigis","forJets"))
stage1L1Trigger.toModify(RunIl1tStage1Layer2, gctTauJetsSource = cms.InputTag("caloStage1LegacyFormatDigis","tauJets"))
stage1L1Trigger.toModify(RunIl1tStage1Layer2, gctIsoTauJetsSource = cms.InputTag("caloStage1LegacyFormatDigis","isoTauJets"))
stage1L1Trigger.toModify(RunIl1tStage1Layer2, gctEnergySumsSource = cms.InputTag("caloStage1LegacyFormatDigis"))
stage1L1Trigger.toModify(RunIl1tStage1Layer2, gctIsoEmSource = cms.InputTag("caloStage1LegacyFormatDigis","isoEm"))
stage1L1Trigger.toModify(RunIl1tStage1Layer2, gctNonIsoEmSource = cms.InputTag("caloStage1LegacyFormatDigis","nonIsoEm"))

stage1L1Trigger.toModify( RunIdqmL1ExtraParticlesStage1, etTotalSource = cms.InputTag("caloStage1LegacyFormatDigis") )
stage1L1Trigger.toModify( RunIdqmL1ExtraParticlesStage1, nonIsolatedEmSource = cms.InputTag("caloStage1LegacyFormatDigis","nonIsoEm") )
stage1L1Trigger.toModify( RunIdqmL1ExtraParticlesStage1, etMissSource = cms.InputTag("caloStage1LegacyFormatDigis") )
stage1L1Trigger.toModify( RunIdqmL1ExtraParticlesStage1, htMissSource = cms.InputTag("caloStage1LegacyFormatDigis") )
stage1L1Trigger.toModify( RunIdqmL1ExtraParticlesStage1, forwardJetSource = cms.InputTag("caloStage1LegacyFormatDigis","forJets") )
stage1L1Trigger.toModify( RunIdqmL1ExtraParticlesStage1, centralJetSource = cms.InputTag("caloStage1LegacyFormatDigis","cenJets") )
stage1L1Trigger.toModify( RunIdqmL1ExtraParticlesStage1, tauJetSource = cms.InputTag("caloStage1LegacyFormatDigis","tauJets") )
stage1L1Trigger.toModify( RunIdqmL1ExtraParticlesStage1, isoTauJetSource = cms.InputTag("caloStage1LegacyFormatDigis","isoTauJets") )
stage1L1Trigger.toModify( RunIdqmL1ExtraParticlesStage1, isolatedEmSource = cms.InputTag("caloStage1LegacyFormatDigis","isoEm") )
stage1L1Trigger.toModify( RunIdqmL1ExtraParticlesStage1, etHadSource = cms.InputTag("caloStage1LegacyFormatDigis") )
stage1L1Trigger.toModify( RunIdqmL1ExtraParticlesStage1, hfRingEtSumsSource = cms.InputTag("caloStage1LegacyFormatDigis") )
stage1L1Trigger.toModify( RunIdqmL1ExtraParticlesStage1, hfRingBitCountsSource = cms.InputTag("caloStage1LegacyFormatDigis") )
stage1L1Trigger.toModify( RunIl1ExtraDQMStage1, stage1_layer2_ = cms.bool(True))
stage1L1Trigger.toModify( RunIl1ExtraDQMStage1, L1ExtraIsoTauJetSource_ = cms.InputTag("dqmL1ExtraParticlesStage1", "IsoTau"))

stage1L1Trigger.toModify(RunIl1compareforstage1, GCTsourceData = cms.InputTag("caloStage1LegacyFormatDigis"))
stage1L1Trigger.toModify(RunIl1compareforstage1, GCTsourceEmul = cms.InputTag("valCaloStage1LegacyFormatDigis"))
stage1L1Trigger.toModify(RunIl1compareforstage1, stage1_layer2_ = cms.bool(True))

stage1L1Trigger.toModify(RunIvalStage1GtDigis, GctInputTag = 'caloStage1LegacyFormatDigis')

#
# define sequences 
#


l1TriggerOnline = cms.Sequence(
                               l1tMonitorStage1Online
                                * dqmEnvL1T
                               )
l1TriggerOnline.replace(l1tRct,RunIl1tRct)
l1TriggerOnline.replace(l1tRctfromRCT,RunIl1tRctfromRCT)
l1TriggerOnline.replace(l1tPUM,RunIl1tPUM)
l1TriggerOnline.replace(l1tStage1Layer2,RunIl1tStage1Layer2)
l1TriggerOnline.replace(dqmL1ExtraParticlesStage1,RunIdqmL1ExtraParticlesStage1)
l1TriggerOnline.replace(l1ExtraDQMStage1,RunIl1ExtraDQMStage1)
                                    
l1TriggerOffline = cms.Sequence(
                                l1TriggerOnline
                                 * dqmEnvL1TriggerReco
                                )
 
#
l1TriggerEmulatorOnline = cms.Sequence(
                                l1Stage1HwValEmulatorMonitor
                                * dqmEnvL1TEMU
                                )
l1TriggerEmulatorOnline.replace(l1TdeRCT,RunIl1TdeRCT)
l1TriggerEmulatorOnline.replace(l1TdeRCTfromRCT,RunIl1TdeRCTfromRCT)
l1TriggerEmulatorOnline.replace(l1TdeStage1Layer2,RunIl1TdeStage1Layer2)
l1TriggerEmulatorOnline.replace(l1Stage1GtHwValidation,RunIl1Stage1GtHwValidation)

l1TriggerEmulatorOffline = cms.Sequence(
                                l1TriggerEmulatorOnline                                
                                )
#

# DQM Offline Step 1 sequence
l1TriggerDqmOffline = cms.Sequence(
                                l1TriggerOffline
                                * l1tRate_Offline
                                * l1tSync_Offline
                                * l1TriggerEmulatorOffline
                                )                                  

# DQM Offline Step 2 sequence                                 
l1TriggerDqmOfflineClient = cms.Sequence(
                                l1tMonitorStage1Client
                                * l1EmulatorMonitorClient
                                )


#
#   EMERGENCY   removal of modules or full sequences 
# =============
#
# un-comment the module line below to remove the module or the sequence

#
# NOTE: for offline, remove the L1TRate which is reading from cms_orcoff_prod, but also requires 
# a hard-coded lxplus path - FIXME check if one can get rid of hard-coded path
# remove also the corresponding client
#
# L1TSync - FIXME - same problems as L1TRate


#
l1tMonitorStage1Online.remove(bxTiming)
l1TriggerStage1Clients.remove(l1tTestsSummary)
l1EmulatorMonitorClient.remove(l1EmulatorErrorFlagClient)
