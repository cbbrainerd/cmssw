#ifndef UtilAlgos_NtpProducer2_h
#define UtilAlgos_NtpProducer2_h
/** \class NtpProducer2
 *
 * Creates histograms defined in config file
 *
 * \author: Christopher Brainerd, UCD
 *
 * Based off NtpProducer class by Luca Lista, INFN
 *
 * Template parameters:
 * - C : Concrete candidate collection type
 * - types...: types that the ntupler can handle
 * Generates a separate EDProducer for each type, and uses strings sent by python config file to determine what EDProducer to use
 * Example usage: typedef NtpProducer<reco::Muon,std::uint_8,std::vector<double> >("uint8","vectorDouble") MuonNtpProducer; DEFINE_FWK_MODULE(MuonNtpProducer);
 * The string literals correspond to the "nice" python name used in config files
 *
 */
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Provenance/interface/RunLumiEventNumber.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "CommonTools/Utils/interface/StringObjectFunction.h"


template<typename C,typename type,typename... types>
class NtpProducer2 : public edm::EDProducer {
public:
  /// constructor from parameter set
  template<typename... strings>
  NtpProducer2( const edm::ParameterSet& , std::string , strings... );
  /// destructor
  ~NtpProducer2();

protected:
  /// process an event
  virtual void produce( edm::Event&, const edm::EventSetup&) override;

private:
  /// label of the collection to be read in
  edm::EDGetTokenT<C> srcToken_;
  /// variable tags
  std::vector<std::pair<std::string, StringObjectFunction<typename C::value_type> > > tags_;
  bool lazyParser_;
  std::string prefix_;
  bool eventInfo_;
  std::string typeString_;
  NtpProducer2<C,types...> childProducer_;
};

template<template<typename C,typename type,typename... types>,typename... strings...>
NtpProducer2<C,type,types...>::NtpProducer2( const edm::ParameterSet& par , std::string typeName , strings... Strings ) :
  childProducer_(par,Strings...) ,
  srcToken_( consumes<C>( par.template getParameter<edm::InputTag>( "src" ) ) ),
  lazyParser_( par.template getUntrackedParameter<bool>( "lazyParser", false ) ),
  prefix_( par.template getUntrackedParameter<std::string>( "prefix","" ) ),
  eventInfo_( par.template getUntrackedParameter<bool>( "eventInfo",true ) ),
  typeString_(typeName) 
{
  std::vector<edm::ParameterSet> variables =
                                   par.template getParameter<std::vector<edm::ParameterSet> >("variables");
   std::vector<edm::ParameterSet>::const_iterator
     q = variables.begin(), end = variables.end();
   if(eventInfo_){
     produces<edm::EventNumber_t>( prefix_+"EventNumber" ).setBranchAlias( prefix_ + "EventNumber" );
     produces<unsigned int>( prefix_ + "RunNumber" ).setBranchAlias( prefix_ + "RunNumber" );
     produces<unsigned int>( prefix_ + "LumiBlock" ).setBranchAlias( prefix_ + "Lumiblock" );
   }
   for (; q!=end; ++q) {
     if(q->getUntrackedParameter<std::string>("Ctype")!=typeString_)
          continue;
     std::string tag = prefix_ + q->getUntrackedParameter<std::string>("tag");
     StringObjectFunction<typename C::value_type> quantity(q->getUntrackedParameter<std::string>("quantity"), lazyParser_);
     tags_.push_back(std::make_pair(tag, quantity));
     produces<type>(tag).setBranchAlias(tag);

   }
}

template<typename C,typename type>
NtpProducer2<C>::~NtpProducer2() {
}

template<typename C,typename type>
void NtpProducer2<C,type>::produce( edm::Event& iEvent, const edm::EventSetup& iSetup) {
   edm::Handle<C> coll;
   iEvent.getByToken(srcToken_, coll);
   typename std::vector<std::pair<std::string, StringObjectFunction<typename C::value_type> > >::const_iterator
     q = tags_.begin(), end = tags_.end();
   for(;q!=end; ++q) {
     if(q->getUntrackedParameter<std::string>("Ctype")!=typeString_)
          continue;
     std::auto_ptr<std::vector<float> > x(new std::vector<type>);
     x->reserve(coll->size());
     for (typename C::const_iterator elem=coll->begin(); elem!=coll->end(); ++elem ) {
       x->push_back(q->second(*elem));
     }
     iEvent.put(x, q->first);
     childProducer.produce(iEvent,iSetup);
   }
}

template<typename C,typename type> //Specialization for lowest level of ED::Producer. Main difference is that it does have any children, and thus does not call the produce method for its child. Also produces eventInfo, if configured.
class NtpProducer2 : public edm::EDProducer {
public:
  /// constructor from parameter set
  NtpProducer2( const edm::ParameterSet& );
  /// destructor
  ~NtpProducer2();

protected:
  /// process an event
  virtual void produce( edm::Event&, const edm::EventSetup&) override;

private:
  /// label of the collection to be read in
  edm::EDGetTokenT<C> srcToken_;
  /// variable tags
  std::vector<std::pair<std::string, StringObjectFunction<typename C::value_type> > > tags_;
  bool lazyParser_;
  std::string prefix_;
  bool eventInfo_;
  std::string typeString_;
};

template<typename C,typename type> //Specialization for lowest level of ED::Producer. Main difference is that it does have any children, and thus does not call the produce method for its child. Also produces eventInfo, if configured.
NtpProducer2<C>::NtpProducer2( const edm::ParameterSet& par , std::string typeName ) :
  srcToken_( consumes<C>( par.template getParameter<edm::InputTag>( "src" ) ) ),
  lazyParser_( par.template getUntrackedParameter<bool>( "lazyParser", false ) ),
  prefix_( par.template getUntrackedParameter<std::string>( "prefix","" ) ),
  eventInfo_( par.template getUntrackedParameter<bool>( "eventInfo",true ) ),
  typeString_(typeName) 
{
  std::vector<edm::ParameterSet> variables =
                                   par.template getParameter<std::vector<edm::ParameterSet> >("variables");
   std::vector<edm::ParameterSet>::const_iterator
     q = variables.begin(), end = variables.end();
   if(eventInfo_){
     produces<edm::EventNumber_t>( prefix_+"EventNumber" ).setBranchAlias( prefix_ + "EventNumber" );
     produces<unsigned int>( prefix_ + "RunNumber" ).setBranchAlias( prefix_ + "RunNumber" );
     produces<unsigned int>( prefix_ + "LumiBlock" ).setBranchAlias( prefix_ + "Lumiblock" );
   }
   for (; q!=end; ++q) {
     if(q->getUntrackedParameter<std::string>("Ctype")!=typeString_)
          continue;
     std::string tag = prefix_ + q->getUntrackedParameter<std::string>("tag");
     StringObjectFunction<typename C::value_type> quantity(q->getUntrackedParameter<std::string>("quantity"), lazyParser_);
     tags_.push_back(std::make_pair(tag, quantity));
     produces<type>(tag).setBranchAlias(tag);

   }
}

template<typename C,typename type>
NtpProducer2<C>::~NtpProducer2() {
}

template<typename C,typename type>
void NtpProducer2<C>::produce( edm::Event& iEvent, const edm::EventSetup&) {
   edm::Handle<C> coll;
   iEvent.getByToken(srcToken_, coll);
   if(eventInfo_){
     std::auto_ptr<edm::EventNumber_t> event( new edm::EventNumber_t );
     std::auto_ptr<unsigned int> run( new unsigned int );
     std::auto_ptr<unsigned int> lumi( new unsigned int );
     *event = iEvent.id().event();
     *run = iEvent.id().run();
     *lumi = iEvent.luminosityBlock();
     iEvent.put( event, prefix_ + "EventNumber" );
     iEvent.put( run, prefix_ + "RunNumber" );
     iEvent.put( lumi, prefix_ + "LumiBlock" );
   }
   typename std::vector<std::pair<std::string, StringObjectFunction<typename C::value_type> > >::const_iterator
     q = tags_.begin(), end = tags_.end();
   for(;q!=end; ++q) {
     if(q->getUntrackedParameter<std::string>("Ctype")!=typeString_)
          continue;
     std::auto_ptr<std::vector<float> > x(new std::vector<type>);
     x->reserve(coll->size());
     for (typename C::const_iterator elem=coll->begin(); elem!=coll->end(); ++elem ) {
       x->push_back(q->second(*elem));
     }
     iEvent.put(x, q->first);
   }
}

#endif
