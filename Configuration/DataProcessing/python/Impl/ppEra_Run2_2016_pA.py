#!/usr/bin/env python
"""
_ppEra_Run2_2016_pA_

Scenario supporting proton collisions

"""

import os
import sys

from Configuration.DataProcessing.Reco import Reco
import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Era_Run2_2016_pA_cff import Run2_2016_pA

from Configuration.DataProcessing.Impl.pp import pp

class ppEra_Run2_2016_pA(pp):
    def __init__(self):
        pp.__init__(self)
        self.recoSeq=''
        self.cbSc='pp'
        self.eras=Run2_2016_pA
        self.promptCustoms += [ 'Configuration/DataProcessing/RecoTLR.customisePostEra_Run2_2016' ]
        self.expressCustoms += [ 'Configuration/DataProcessing/RecoTLR.customisePostEra_Run2_2016' ]
        self.visCustoms += [ 'Configuration/DataProcessing/RecoTLR.customisePostEra_Run2_2016' ]
    """
    _ppEra_Run2_2016_pA_

    Implement configuration building for data processing for proton
    collision data taking for Run2

    """
