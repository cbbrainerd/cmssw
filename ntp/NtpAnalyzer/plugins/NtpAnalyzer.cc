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
//#include "TFile.h"
//#include <array>
//#include <complex>
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

//#include <boost/math/special_functions/spherical_harmonic.hpp>

//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

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
      TH1D *etSumOppositeSignDimuons_;
      TH1D *etSumSameSignDimuons_;
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
   etSumOppositeSignDimuons_=fs->make<TH1D>("etSumOppositeSignDimuons_","EtSum of Opposite Sign Dimuons",10000,0,1000);
   etSumSameSignDimuons_=fs->make<TH1D>("etSumSameSignDimuons_","EtSum of Same Sign Dimuons",10000,0,1000);
}


NtpAnalyzer::~NtpAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


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
   int numMuons=muonCharge_->size();
   numberMuons_->Fill(numMuons);
   if(numMuons == 2) { //For now look at events with only two muons
        double etSum=0;
        for(auto it=emEt_->begin();it!=emEt_->end();++it) {
            etSum+=(*it);
        }
        if((*muonCharge_)[0]!=(*muonCharge_)[1]) { //Opposite sign dimuon
            etSumOppositeSignDimuons_->Fill(etSum);
        } else { //Same sign dimuon
            etSumSameSignDimuons_->Fill(etSum);
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
