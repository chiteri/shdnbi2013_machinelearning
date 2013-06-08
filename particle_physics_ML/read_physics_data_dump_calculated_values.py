import numpy as np
import matplotlib.pylab as plt

#import ROOT

import sys

f = open(sys.argv[1])

outfilename = "calc_vals_%s.dat" % (sys.argv[1].split('/')[-1].split('.')[0])
outfile = open(outfilename,'w')

not_at_end = True

masses_muons = []

event_count = 0
output = ""
out_f = open('testing.dat','w')

while ( not_at_end ):

    ############################################################################
    # Read in one event
    ############################################################################
    line = f.readline()

    if event_count%1000==0:
        print "Event count: ",event_count

    if line=="":
        not_at_end = False

    if line.find("Event")>=0:
        new_event = True

    if new_event==True:

        # Read in the jet info for this event.
        jets = []
        line = f.readline()
        njets = int(line)
        for i in xrange(njets):
            line = f.readline()
            vals = line.split()
            e = float(vals[0])
            px = float(vals[1])
            py = float(vals[2])
            pz = float(vals[3])
            bquark_jet_tag = float(vals[4])
            jets.append([e,px,py,pz,bquark_jet_tag])
            out_f.write("%f %f %f %d %f\n" % (e,px,py,pz,bquark_jet_tag))# Write our testing data for the ML algo -- added by @daaj

        # Read in the muon info for this event.
        muons = []
        line = f.readline()
        nmuons = int(line)
        for i in xrange(nmuons):
            line = f.readline()
            vals = line.split()
            e = float(vals[0])
            px = float(vals[1])
            py = float(vals[2])
            pz = float(vals[3])
            charge = int(vals[4])
            muons.append([e,px,py,pz,charge])

        # Read in the electron info for this event.
        electrons = []
        line = f.readline()
        nelectrons = int(line)
        for i in xrange(nelectrons):
            line = f.readline()
            vals = line.split()
            e = float(vals[0])
            px = float(vals[1])
            py = float(vals[2])
            pz = float(vals[3])
            charge = int(vals[4])
            electrons.append([e,px,py,pz,charge])

        # Read in the photon info for this event.
        photons = []
        line = f.readline()
        nphotons = int(line)
        for i in xrange(nphotons):
            line = f.readline()
            vals = line.split()
            e = float(vals[0])
            px = float(vals[1])
            py = float(vals[2])
            pz = float(vals[3])
            photons.append([e,px,py,pz])


        # Read in the information about the missing transverse energy (MET) in the event.
        # This is really the x and y direction for the missing momentum.
        line = f.readline()
        vals = line.split()
        met_px = float(vals[0])
        met_py = float(vals[1])

        new_event = False
        event_count += 1

        ########################################################################
        # Now that you've read in the information for *one* event, 
        # do a calculation!
        ########################################################################

        # 1
        max_muon_pt = 0.0
        for muon in muons:
            e0 = muon[0]
            px0 = muon[1]
            py0= muon[2]
            pz0= muon[3]

            pt = np.sqrt(px0**2 + py0**2)
            if pt>max_muon_pt:
                max_muon_pt = pt

            #mass = np.sqrt(e0**2 - ( px0**2 + py0**2 + pz0**2 ))
            #masses_muons.append(mass)


        # 2
        met = np.sqrt(met_px**2 + met_py**2)

        # 3
        max_jet_pt = 0.0
        for jet in jets:
            e0 = jet[0]
            px0 = jet[1]
            py0= jet[2]
            pz0= jet[3]

            pt = np.sqrt(px0**2 + py0**2)
            if pt>max_jet_pt:
                max_jet_pt = pt

            #mass = np.sqrt(e0**2 - ( px0**2 + py0**2 + pz0**2 ))
            #masses_muons.append(mass)

        # 4
        njets = len(jets)

        # 5
        max_bjet_tag = -5
        for jet in jets:
            bjet_tag= jet[4]

            if bjet_tag>max_bjet_tag:
                max_bjet_tag = bjet_tag

        output = "%f %f %f %d %f\n" % (max_muon_pt, met, max_jet_pt, njets, max_bjet_tag)
        outfile.write(output)

outfile.close()

#plt.hist(masses_muons,range=(0,1),bins=100)
#plt.show()


    



