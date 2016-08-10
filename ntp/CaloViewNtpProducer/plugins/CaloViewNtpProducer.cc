#include "FWCore/Framework/interface/MakerMacros.h"
#include "CommonTools/UtilAlgos/interface/NtpProducer.h"

//EGamma
#include "DataFormats/L1Trigger/interface/EGamma.h"

//CaloTowers
#include "DataFormats/CaloTowers/interface/CaloTower.h"

typedef NtpProducer<edm::View<CaloTower> > CaloViewNtpProducer;

DEFINE_FWK_MODULE(CaloViewNtpProducer);
