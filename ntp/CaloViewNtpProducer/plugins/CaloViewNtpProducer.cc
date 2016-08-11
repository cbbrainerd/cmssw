#include "FWCore/Framework/interface/MakerMacros.h"
#include "CommonTools/UtilAlgos/interface/NtpProducer.h"

//CaloTowers
#include "DataFormats/CaloTowers/interface/CaloTower.h"

//Muons
#include "DataFormats/MuonReco/interface/Muon.h"

typedef NtpProducer<edm::View<CaloTower> > CaloViewNtpProducer;
typedef NtpProducer<edm::View<reco::Muon> > MuonViewNtpProducer;

DEFINE_FWK_MODULE(CaloViewNtpProducer);
DEFINE_FWK_MODULE(MuonViewNtpProducer);
