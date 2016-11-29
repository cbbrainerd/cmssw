from Configuration.Eras.Modifier_stage1L1Trigger_cff import stage1L1Trigger
from Configuration.Eras.Modifier_stage2L1Trigger_cff import stage2L1Trigger

_importModule='DQMOffline.L1Trigger.LegacyL1TriggerDqmOffline_cff' #import this for legacy
stage1L1Trigger.toReplaceWith(_importModule,'DQMOffline.L1Trigger.Stage2L1TriggerDqmOffline_cff')
stage2L1Trigger.toReplaceWith(_importModule,'DQMOffline.L1Trigger.Stage2L1TriggerDqmOffline_cff') #import this for upgrade
exec('from '+_importModule+' import *')
