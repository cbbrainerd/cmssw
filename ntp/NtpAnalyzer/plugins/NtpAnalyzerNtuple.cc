// -*- C++ -*-
//
// Package:    ntp/NtpAnalyzerNtuple
// Class:      NtpAnalyzerNtuple
// 
/**\class NtpAnalyzerNtuple NtpAnalyzerNtuple.cc ntp/NtpAnalyzerNtuple/plugins/NtpAnalyzerNtuple.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Christopher Brainerd
//         Created:  Fri, 21 Apr 2017 17:12:58 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/StreamID.h"

#include <vector>
#include <utility>
#include "TH1D.h"
#include "TH1I.h"
#include "TH2D.h"

#include <algorithm>
//#include "TFile.h"
//#include <array>
//#include <complex>

#include "DataFormats/Math/interface/LorentzVector.h"

template<typename T>
T abs(const T& a) {
    return(a<0?-a:a);
}

//
// class declaration
//

class NtpAnalyzerNtuple : public edm::stream::EDProducer<> {
   public:
      explicit NtpAnalyzerNtuple(const edm::ParameterSet&);
      ~NtpAnalyzerNtuple();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginStream(edm::StreamID) override;
      virtual void produce(edm::Event&, const edm::EventSetup&) override;
      virtual void endStream() override;

      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

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
      TH1D *numberMuons_;
      TH1D *numberLooseMuons_;
      TH1D *etSumOppositeSignDimuons_;
      TH1D *etSumSameSignDimuons_;
      TH1D *sameSignDimuonInvariantMass_;
      TH1D *oppositeSignDimuonInvariantMass_;
      TH1D *oppositeSignDimuonInvariantMassWithJustTwoMuons_;
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

      TH2D *etSumInvariantMassOS_;
      TH2D *etSumInvariantMassSS_;

};

//
// constants, enums and typedefs
//

bool isPFMuon(const unsigned int& muonType);

bool isGlobalMuon(const unsigned int& muonType);

bool isTrackerMuon(const unsigned int& muonType);

bool isLooseMuon(const unsigned int& muonType);

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

bool operator<(const muon& a,const muon& b) {
    return a.pt < b.pt;
}

//
// static data member definitions
//

//
// constructors and destructor
//
NtpAnalyzerNtuple::NtpAnalyzerNtuple(const edm::ParameterSet& iConfig) :
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
    produces<double>("etSum").setBranchAlias("etSum");
    produces<double>("hadEtSum").setBranchAlias("hadEtSum");
    produces<std::vector<double> >("invariantMass").setBranchAlias("invariantMass");
    produces<std::vector<double> >("deltaPhi").setBranchAlias("deltaPhi");
    produces<std::vector<double> >("deltaEta").setBranchAlias("deltaEta");
    produces<std::vector<float> >("looseMuonPt").setBranchAlias("looseMuonPt");
    produces<std::vector<int> >("looseMuonCharge").setBranchAlias("looseMuonCharge");
   //register your products
/* Examples
   produces<ExampleData2>();

   //if do put with a label
   produces<ExampleData2>("label");
 
   //if you want to put into the Run
   produces<ExampleData2,InRun>();
*/
   //now do what ever other initialization is needed
  
}


NtpAnalyzerNtuple::~NtpAnalyzerNtuple()
{
 
   // do anything here that needs to be done at destruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
NtpAnalyzerNtuple::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
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
   std::unique_ptr<std::vector<float> > looseMuonPt;
   std::unique_ptr<std::vector<int> > looseMuonCharge;
   std::unique_ptr<std::vector<double> > invariantMassV;
   std::unique_ptr<std::vector<double> > deltaPhiV;
   std::unique_ptr<std::vector<double> > deltaEtaV;
   std::unique_ptr<double> etSum;
   std::unique_ptr<double> hadEtSum;
   *etSum=0;
   *hadEtSum=0;
   int i=0;
   for(auto it=muonType_->begin();it!=muonType_->end();++it) {
        if(isLooseMuon(*it)) { //Quality cut 
            if(((*muonPt_)[i] > 10)&&(abs((*muonEta_)[i]) < 2.4)) { //Suggested cuts in SWGuideMuonIdRun2 (What is Loose PF comb. rel. isolation?)
                looseMuons.push_back(muon((*muonPt_)[i],(*muonEta_)[i],(*muonPhi_)[i],(*muonCharge_)[i],(*muonType_)[i]));
            }
        }
        ++i;
   }
   std::sort(looseMuons.rbegin(),looseMuons.rend());
   for(auto it=looseMuons.begin();it!=looseMuons.end();++it) {
       looseMuonPt->push_back(it->pt);
       looseMuonCharge->push_back(it->charge);
   }
   iEvent.put(std::move(looseMuonPt),"looseMuonPt");
   iEvent.put(std::move(looseMuonCharge),"looseMuonCharge");
   int numCaloTowers=emEt_->size();
   for(int i=0;i!=numCaloTowers;++i) {
       (*etSum)+=(*emEt_)[i];
       (*hadEtSum)+=(*hadEt_)[i];
   }
   iEvent.put(std::move(etSum),"etSum");
   iEvent.put(std::move(hadEtSum),"hadEtSum");
   for(auto i=looseMuons.begin();i!=looseMuons.end();++i) {
      for(auto j=looseMuons.begin();j!=i;++j) {
          math::PtEtaPhiMLorentzVectorD p4;
          p4=(*i).p4+(*j).p4;
          double invariantMass=p4.M(); 
          double deltaEta=abs((*i).eta-(*j).eta);
          double deltaPhi=abs((*i).phi-(*j).phi);
          invariantMassV->push_back(invariantMass);
          deltaEtaV->push_back(deltaEta);
          deltaPhiV->push_back(deltaPhi);
      }
   }
   iEvent.put(std::move(invariantMassV),"invariantMass");
   iEvent.put(std::move(deltaEtaV),"deltaEta");
   iEvent.put(std::move(deltaPhiV),"deltaPhi");
/* This is an event example
   //Read 'ExampleData' from the Event
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);

   //Use the ExampleData to create an ExampleData2 which 
   // is put into the Event
   iEvent.put(std::make_unique<ExampleData2>(*pIn));
*/

/* this is an EventSetup example
   //Read SetupData from the SetupRecord in the EventSetup
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
*/
 
}

// ------------ method called once each stream before processing any runs, lumis or events  ------------
void
NtpAnalyzerNtuple::beginStream(edm::StreamID)
{
}

// ------------ method called once each stream after processing all runs, lumis and events  ------------
void
NtpAnalyzerNtuple::endStream() {
}

// ------------ method called when starting to processes a run  ------------
/*
void
NtpAnalyzerNtuple::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when ending the processing of a run  ------------
/*
void
NtpAnalyzerNtuple::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when starting to processes a luminosity block  ------------
/*
void
NtpAnalyzerNtuple::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when ending the processing of a luminosity block  ------------
/*
void
NtpAnalyzerNtuple::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
NtpAnalyzerNtuple::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(NtpAnalyzerNtuple);
