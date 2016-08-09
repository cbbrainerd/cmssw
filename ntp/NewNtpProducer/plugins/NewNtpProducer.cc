#include "FWCore/Framework/interface/MakerMacros.h"
#include "CommonTools/UtilAlgos/interface/NtpProducer.h"

//L1 Candidate
#include "DataFormats/L1Trigger/interface/L1Candidate.h"
//Trigger Specific Classes
#include "DataFormats/L1Trigger/interface/EGamma.h"
#include "DataFormats/L1Trigger/interface/EtSum.h"
#include "DataFormats/L1Trigger/interface/Jet.h"
#include "DataFormats/L1Trigger/interface/Muon.h"
#include "DataFormats/L1Trigger/interface/Tau.h"

typedef NtpProducer<edm::View<l1t::L1Candidate> > L1CandidateNtpProducer;
typedef NtpProducer<edm::View<l1t::EGamma> > L1EGammaNtpProducer;
typedef NtpProducer<edm::View<l1t::EtSum> > L1EtSumNtpProducer;
typedef NtpProducer<edm::View<l1t::Jet> > L1JetNtpProducer;
typedef NtpProducer<edm::View<l1t::Muon> > L1MuonNtpProducer;
typedef NtpProducer<edm::View<l1t::Tau> > L1TauNtpProducer;


DEFINE_FWK_MODULE(L1CandidateNtpProducer);
DEFINE_FWK_MODULE(L1EGammaNtpProducer);
DEFINE_FWK_MODULE(L1EtSumNtpProducer);
DEFINE_FWK_MODULE(L1JetNtpProducer);
DEFINE_FWK_MODULE(L1MuonNtpProducer);
DEFINE_FWK_MODULE(L1TauNtpProducer);
