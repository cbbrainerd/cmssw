// -*- C++ -*-
//
// Package:    ntp/NtpAnalyzer
// Class:      NtpAnalyzer
// 
/**\class NtpAnalyzer NtpAnalyzer.cc ntp/NtpAnalyzer/plugins/NtpAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Christopher Brainerd
//         Created:  Thu, 25 Aug 2016 16:14:00 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include <vector>
#include "TH1D.h"
#include "TH2D.h"
//#include "TFile.h"
//#include <array>
//#include <complex>
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/Math/interface/LorentzVector.h"

//#include <boost/math/special_functions/spherical_harmonic.hpp>

//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

template<typename T>
T abs(const T& a) {
    return(a<0?-a:a);
}

class NtpAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit NtpAnalyzer(const edm::ParameterSet&);
      ~NtpAnalyzer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      // ----------member data ---------------------------
      edm::EDGetTokenT<std::vector<double> > caloTowerThetaToken_;
      edm::EDGetTokenT<std::vector<double> > emEtToken_;
      edm::EDGetTokenT<std::vector<double> > hadEtToken_;
      edm::EDGetTokenT<std::vector<double> > muonEtaToken_;
      edm::EDGetTokenT<std::vector<double> > muonPhiToken_;
      edm::EDGetTokenT<std::vector<double> > muonPtToken_;
      edm::EDGetTokenT<std::vector<int> > caloTowerIetaToken_;
      edm::EDGetTokenT<std::vector<int> > caloTowerIphiToken_;
      edm::EDGetTokenT<std::vector<int> > muonChargeToken_;
      edm::EDGetTokenT<std::vector<unsigned int> > muonTypeToken_;
      edm::Handle<std::vector<double> > caloTowerTheta_;
      edm::Handle<std::vector<double> > emEt_;
      edm::Handle<std::vector<double> > hadEt_;
      edm::Handle<std::vector<double> > muonEta_;
      edm::Handle<std::vector<double> > muonPhi_;
      edm::Handle<std::vector<double> > muonPt_;
      edm::Handle<std::vector<int> > caloTowerIeta_;
      edm::Handle<std::vector<int> > caloTowerIphi_;
      edm::Handle<std::vector<int> > muonCharge_;
      edm::Handle<std::vector<unsigned int> > muonType_;
//      TFile *tfile_;
      TH1D *numberMuons_;
      TH1D *numberLooseMuons_;
      TH1D *etSumOppositeSignDimuons_;
      TH1D *etSumSameSignDimuons_;
      TH1D *sameSignDimuonInvariantMass_;
      TH1D *oppositeSignDimuonInvariantMass_;
      TH1D *positiveSignDimuonInvariantMass_;
      TH1D *negativeSignDimuonInvariantMass_;
      TH1D *muonPtH_;
      TH1D *looseMuonPt_;
      TH1D *muonEtaH_;
      TH1D *muonPhiH_;
      TH1D *muonTypeH_;
      TH1D *deltaEta_;
      TH1D *deltaPhi_;

      TH1D *caloTowerIetaH_;
      TH1D *caloTowerIphiH_;
      TH2D *caloTowerGrid_;
      TH1D *caloTowerThetaH_;
      TH1D *emEtH_;
      TH1D *hadEtH_;
      TH1D *numberCaloTowers_;

      TObjString *information_;
//      std::array<std::array<std::complex,howManyCaloTowers>,N> multipoleMoments;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
NtpAnalyzer::NtpAnalyzer(const edm::ParameterSet& iConfig) :
    caloTowerThetaToken_(consumes<std::vector<double> >(iConfig.getParameter<edm::InputTag>("caloTowerTheta"))),
    emEtToken_(consumes<std::vector<double> >(iConfig.getParameter<edm::InputTag>("emEt"))),
    hadEtToken_(consumes<std::vector<double> >(iConfig.getParameter<edm::InputTag>("hadEt"))),
    muonEtaToken_(consumes<std::vector<double> >(iConfig.getParameter<edm::InputTag>("muonEta"))),
    muonPhiToken_(consumes<std::vector<double> >(iConfig.getParameter<edm::InputTag>("muonPhi"))),
    muonPtToken_(consumes<std::vector<double> >(iConfig.getParameter<edm::InputTag>("muonPt"))),
    caloTowerIetaToken_(consumes<std::vector<int> >(iConfig.getParameter<edm::InputTag>("caloTowerIeta"))),
    caloTowerIphiToken_(consumes<std::vector<int> >(iConfig.getParameter<edm::InputTag>("caloTowerIphi"))),
    muonChargeToken_(consumes<std::vector<int> >(iConfig.getParameter<edm::InputTag>("muonCharge"))),
    muonTypeToken_(consumes<std::vector<unsigned int> >(iConfig.getParameter<edm::InputTag>("muonType")))
{
   //now do what ever initialization is needed
   usesResource("TFileService");
   edm::Service<TFileService> fs;
//   tfile_=new TFile("Histograms.root","UPDATE");
   numberMuons_=fs->make<TH1D>("numberMuons_","Number of Muons per Event",11,-.5,10.5);
   numberLooseMuons_=fs->make<TH1D>("numberLooseMuons_","Number of Loose Muons per Event",11,-.5,10.5);
   etSumOppositeSignDimuons_=fs->make<TH1D>("etSumOppositeSignDimuons_","EtSum of Opposite Sign Dimuons",1000,0,1000);
   etSumSameSignDimuons_=fs->make<TH1D>("etSumSameSignDimuons_","EtSum of Same Sign Dimuons",1000,0,1000);
   sameSignDimuonInvariantMass_=fs->make<TH1D>("sameSignDimuonInvariantMass_","Invariant Mass for Same Sign Dimuons",2000,0,2000);
   oppositeSignDimuonInvariantMass_=fs->make<TH1D>("oppositeSignDimuonInvariantMass_","Invariant Mass for Opposite Sign Dimuons",2000,0,2000);
   positiveSignDimuonInvariantMass_=fs->make<TH1D>("positiveSignDimuonInvariantMass_","Invariant Mass for Positive Sign Dimuons",2000,0,2000);
   negativeSignDimuonInvariantMass_=fs->make<TH1D>("negativeSignDimuonInvariantMass_","Invariant Mass for Negative Sign Dimuons",2000,0,2000);
   muonPtH_=fs->make<TH1D>("muonPtH_","Muon Pt",1000,0,1000);
   looseMuonPt_=fs->make<TH1D>("looseMuonPt_","Loose Muon Pt",1000,0,1000);
   muonEtaH_=fs->make<TH1D>("muonEtaH_","Loose Muon Eta",200,-3.2,3.2);
   muonPhiH_=fs->make<TH1D>("muonPhiH_","Loose Muon Phi",200,-3.2,3.2);
   muonTypeH_=fs->make<TH1D>("muonTypeH_","Muon Type",128,-.5,127.5);
   deltaEta_=fs->make<TH1D>("deltaEta_","Dimuon Delta Eta",200,0,6.4);
   deltaPhi_=fs->make<TH1D>("deltaPhi_","Dimuon Delta Phi",200,0,6.4);
   caloTowerIetaH_=fs->make<TH1D>("caloTowerIetaH_","Calo Tower iEta",57,-28.5,28.5);
   caloTowerIphiH_=fs->make<TH1D>("caloTowerIphiH_","Calo Tower iPhi",72,.5,72.5);
   caloTowerGrid_=fs->make<TH2D>("caloTowerGrid_","Calo Tower iEta and iPhi",57,-28.5,28.5,72,.5,72.5);
   caloTowerThetaH_=fs->make<TH1D>("caloTowerThetaH_","Calo Tower Theta",1000,0,3.14);
   emEtH_=fs->make<TH1D>("emEtH_","emEt Of Each Tower",1000,0,100);
   hadEtH_=fs->make<TH1D>("hadEtH_","hadEt Of Each Tower",1000,0,100);
   numberCaloTowers_=fs->make<TH1D>("numberCaloTowers_","Number of Calo Towers per Event",5001,-.5,5000.5);
//   information_=fs->make<TObjString>("Cuts: Both muons loose, >= 1GeV pT, at least one muon >= 10GeV pT. Both muon eta < 2.4. Exactly two muons pass cuts. Version 6.");
    information_=fs->make<TObjString>("v8. Cuts: Both muons loose, no pT/eta cuts. At least two muons- fill invariant mass for EVERY COMBINATION. No further cuts.");
}


NtpAnalyzer::~NtpAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}

bool isPFMuon(const unsigned int& muonType) {
    static constexpr unsigned int PFMuon = 1u<<5;
    return PFMuon & muonType;
}

bool isGlobalMuon(const unsigned int& muonType) {
    static constexpr unsigned int GlobalMuon = 1u<<1;
    return GlobalMuon & muonType;
}

bool isTrackerMuon(const unsigned int& muonType) {
    static constexpr unsigned int TrackerMuon = 1u<<2;
    return TrackerMuon & muonType;
}

bool isLooseMuon(const unsigned int& muonType) {
    return isPFMuon(muonType) && (isGlobalMuon(muonType) || isTrackerMuon(muonType));
}


struct muon {
    static constexpr double muon_mass=.1056583;
    double pt;
    double eta;
    double phi;
    int charge;
    unsigned int type;
    math::PtEtaPhiMLorentzVectorD p4;
    muon(double pt_,double eta_,double phi_,int charge_,unsigned int type_) :
    pt(pt_),eta(eta_),phi(phi_),charge(charge_),type(type_),p4(pt_,eta_,phi_,muon_mass) {}
};

//
// member functions
//

// ------------ method called for each event  ------------
void
NtpAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   iEvent.getByToken(caloTowerThetaToken_,caloTowerTheta_);
   iEvent.getByToken(emEtToken_,emEt_);
   iEvent.getByToken(hadEtToken_,hadEt_);
   iEvent.getByToken(muonEtaToken_,muonEta_);
   iEvent.getByToken(muonPhiToken_,muonPhi_);
   iEvent.getByToken(muonPtToken_,muonPt_);
   iEvent.getByToken(caloTowerIetaToken_,caloTowerIeta_);
   iEvent.getByToken(caloTowerIphiToken_,caloTowerIphi_);
   iEvent.getByToken(muonChargeToken_,muonCharge_);
   iEvent.getByToken(muonTypeToken_,muonType_);
   std::vector<muon> looseMuons;
   int i=0;
   for(auto it=muonType_->begin();it!=muonType_->end();++it) {
        muonPtH_->Fill((*muonPt_)[i]);
        muonTypeH_->Fill(*it);
        if(isLooseMuon(*it)) { //Quality cut 
            if(/*((*muonPt_)[i] > 1)&&((*muonEta_)[i] < 2.4)*/true) { //Suggested cuts in SWGuideMuonIdRun2 (What is Loose PF comb. rel. isolation?)
                looseMuons.push_back(muon((*muonPt_)[i],(*muonEta_)[i],(*muonPhi_)[i],(*muonCharge_)[i],(*muonType_)[i]));
                looseMuonPt_->Fill((*muonPt_)[i]);
                muonEtaH_->Fill((*muonEta_)[i]);
                muonPhiH_->Fill((*muonPhi_)[i]);
            }
        }
        ++i;
   }
   int numMuons=muonCharge_->size();
   int numLooseMuons=looseMuons.size();
   int numCaloTowers=emEt_->size();
   numberCaloTowers_->Fill(numCaloTowers);
   numberMuons_->Fill(numMuons);
   numberLooseMuons_->Fill(numLooseMuons);
   if(numLooseMuons >= 2) { //Events with AT LEAST 2 muons
/*        if(looseMuons[0].pt < 10 && looseMuons[1].pt < 10)
            return; */
        double etSum=0;
        for(int i=0;i!=numCaloTowers;++i) {
            etSum+=(*emEt_)[i];
            caloTowerIetaH_->Fill((*caloTowerIeta_)[i]);
            caloTowerIphiH_->Fill((*caloTowerIphi_)[i]);
            caloTowerGrid_->Fill((*caloTowerIeta_)[i],(*caloTowerIphi_)[i]);
            caloTowerThetaH_->Fill((*caloTowerTheta_)[i]);
            emEtH_->Fill((*emEt_)[i]);
            hadEtH_->Fill((*hadEt_)[i]);
        }
        etSumOppositeSignDimuons_->Fill(etSum); //NB: This is for all dimuons now, just too lazy to change the name
        for(int i=1;i<numLooseMuons;++i) {
            for(int j=0;j<i;++i) {
                math::PtEtaPhiMLorentzVectorD p4;
                p4=(looseMuons[i]).p4+(looseMuons[j]).p4;
                double invariantMass=p4.M2(); 
    //        if(invariantMass<80 || invariantMass>100)
    //            return;
                double deltaEta=abs((looseMuons[i]).eta-(looseMuons[j]).eta);
                double deltaPhi=abs((looseMuons[i]).phi-(looseMuons[j]).phi);
                deltaEta_->Fill(deltaEta);
                deltaPhi_->Fill(deltaPhi);
                double etSum=0;
    //        for(auto it=emEt_->begin();it!=emEt_->end();++it) {
                if((looseMuons[i]).charge!=(looseMuons[j]).charge) { //Opposite sign dimuon
        //            etSumOppositeSignDimuons_->Fill(etSum);
                    oppositeSignDimuonInvariantMass_->Fill(invariantMass);
                
                } else { //Same sign dimuon
        //            etSumSameSignDimuons_->Fill(etSum);
                    if(looseMuons[i].charge > 0) {
                        positiveSignDimuonInvariantMass_->Fill(invariantMass);
                    } else {
                        negativeSignDimuonInvariantMass_->Fill(invariantMass);
                    }
                    sameSignDimuonInvariantMass_->Fill(invariantMass);
                }
            }
        }
    }
}

// ------------ method called once each job just before starting event loop  ------------
void 
NtpAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
NtpAnalyzer::endJob() 
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
NtpAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(NtpAnalyzer);
