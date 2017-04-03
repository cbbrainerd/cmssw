#ifndef DataFormats_L1Trigger_L1DataEmulResult_h
#define DataFormats_L1Trigger_L1DataEmulResult_h

#include "DataFormats/L1Trigger/interface/BXVector.h"

namespace l1t {
  class L1DataEmulResult;
  typedef BXVector<L1DataEmulResult> L1DataEmulResultBxCollection;

  class L1DataEmulResult {

  public:

    L1DataEmulResult();
    L1DataEmulResult(bool event_match, std::string collname);
    L1DataEmulResult(bool event_match, int pt_mismatch, int etaphi_mismatch, int n_mismatch, int n_dataonly, int n_emulonly, int add1, int add2, std::string collname);
    ~L1DataEmulResult();

  public:

    bool Event_match() const;
    std::string Collname() const;
    int PT_mismatch() const;
    int ETAPHI_mismatch() const;
    int N_mismatch() const;
    int N_dataonly() const;
    int N_emulonly() const;
    int Add1() const;
    int Add2() const;

  private:

    bool event_match_;
    std::string collname_;
    int pt_mismatch_;
    int etaphi_mismatch_;
    int n_mismatch_;
    int n_dataonly_;
    int n_emulonly_;
    int add1_;
    int add2_;
  };
};

#endif

    

    
   
