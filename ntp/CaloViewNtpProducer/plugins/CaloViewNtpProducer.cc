#include "FWCore/Framework/interface/MakerMacros.h"

#include "ntp/CaloViewNtpProducer/interface/NtpProducer.h"

//CaloTowers
#include "DataFormats/CaloTowers/interface/CaloTower.h"

//Muons
#include "DataFormats/MuonReco/interface/Muon.h"

//CaloJets
#include "DataFormats/JetReco/interface/CaloJet.h"

class MuonViewNtpProducer : public NtpProducer2<edm::View<reco::Muon>,std::vector<double>,std::vector<int>,std::vector<unsigned int> > {
public:
    MuonViewNtpProducer(const edm::ParameterSet& par) : NtpProducer2(par,std::string("double"),std::string("int"),std::string("unsignedint")) {}
};

class CaloViewNtpProducer : public NtpProducer2<edm::View<CaloTower>,std::vector<double>,std::vector<int> > {
public:
    CaloViewNtpProducer(const edm::ParameterSet& par) : NtpProducer2(par,std::string("double"),std::string("int")) {}
};

class JetViewNtpProducer : public NtpProducer2<edm::View<reco::CaloJet>,std::vector<double> > {
public: 
    JetViewNtpProducer(const edm::ParameterSet& par) : NtpProducer2(par,std::string("double")) {}
};

DEFINE_FWK_MODULE(MuonViewNtpProducer);
DEFINE_FWK_MODULE(CaloViewNtpProducer);
DEFINE_FWK_MODULE(JetViewNtpProducer);
