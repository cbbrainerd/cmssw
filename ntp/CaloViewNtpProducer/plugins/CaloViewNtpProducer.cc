#include "FWCore/Framework/interface/MakerMacros.h"

#include "ntp/CaloViewNtpProducer/interface/NtpProducer.h"

//CaloTowers
#include "DataFormats/CaloTowers/interface/CaloTower.h"

//Muons
#include "DataFormats/MuonReco/interface/Muon.h"

class MuonViewNtpProducer : public NtpProducer2<edm::View<reco::Muon>,std::vector<double>,std::vector<int>,std::vector<unsigned int> > {
public:
    MuonViewNtpProducer(const edm::ParameterSet& par) : NtpProducer2(par,std::string("double"),std::string("int"),std::string("unsigned int")) {}
};

class CaloViewNtpProducer : public NtpProducer2<edm::View<CaloTower>,std::vector<double>,std::vector<int> > {
public:
    CaloViewNtpProducer(const edm::ParameterSet& par) : NtpProducer2(par,std::string("double"),std::string("int")) {}
};

DEFINE_FWK_MODULE(MuonViewNtpProducer);
DEFINE_FWK_MODULE(CaloViewNtpProducer);
