#include "FWCore/Framework/interface/MakerMacros.h"
#include "CommonTools/UtilAlgos/interface/NtpProducer.h"

//Muons
#include "DataFormats/MuonReco/interface/Muon.h"

//CaloTowers
#include "DataFormats/CaloTowers/interface/CaloTower.h"

typedef NtpProducer<edm::View<CaloTower> > CaloViewNtpProducer;

DEFINE_FWK_MODULE(CaloViewNtpProducer);
