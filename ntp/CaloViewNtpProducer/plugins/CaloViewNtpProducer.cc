#include "FWCore/Framework/interface/MakerMacros.h"
#include "CommonTools/UtilAlgos/interface/NtpProducer.h"

#include "ntp/CaloViewNtpProducer/interface/NtpProducer.h"

//CaloTowers
#include "DataFormats/CaloTowers/interface/CaloTower.h"

//Muons
#include "DataFormats/MuonReco/interface/Muon.h"

typedef NtpProducer<edm::View<CaloTower> > CaloViewNtpProducer;
typedef NtpProducer<edm::View<reco::Muon> > MuonViewNtpProducer;
//typedef NtpProducer2<edm::View<reco::Muon>,std::vector<float>,std::vector<double> > MuonViewNtpProducer2;

class MuonViewNtpProducer2 : public NtpProducer2<edm::View<reco::Muon>,std::vector<double> > {
public:
    MuonViewNtpProducer2(const edm::ParameterSet& par) : NtpProducer2(par,std::string("doubleVector")) {}
};


DEFINE_FWK_MODULE(CaloViewNtpProducer);
DEFINE_FWK_MODULE(MuonViewNtpProducer);
DEFINE_FWK_MODULE(MuonViewNtpProducer2);

