from DataFormats.FWLite import Handle, Events
Et = Handle('std::vector<float>')
import ROOT

import os
import sys

directory = sys.argv[1]
subdir=os.listdir(directory)
c=ROOT.TCanvas("c","c",800,800)
EtSum_TH1F = ROOT.TH1F("a","a",100,0,1000)

def allTheCode():
    global c
    numberOfFiles=0
    for direct in subdir:
        for fil in os.listdir(directory+direct):
            if os.path.isdir(directory+direct+"/"+fil):
                continue
            numberOfFiles=numberOfFiles+1
            print "Opening file %s, file number %s..."  % (fil,numberOfFiles)
            events=Events(directory+direct+"/"+fil)
            numevents=0
            for event in events:
                numevents=numevents+1
                event.getByLabel("ntptow","emEt","ntupler",Et)
                numberTowers=Et.product().size()
                EtSum=0
                for i in range(0,numberTowers):
                    EtSum=EtSum+Et.product()[i]
                EtSum_TH1F.Fill(EtSum)
                if not (numevents % 100):
                    print "%s events processed." % numevents
            c.cd()
            EtSum_TH1F.Draw()
            c.SaveAs("EtSum.png")

allTheCode()

