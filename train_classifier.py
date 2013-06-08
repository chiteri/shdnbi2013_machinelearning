from sklearn import tree
import numpy as np

import matplotlib.pylab as plt


import sys

MAX_EVENTS = 500
jet_features = []
tt_features = []

def read_jets():
    # Read in the jet info for this event.
    not_at_end = True

    counter = 0
    
    
    f = open('resources/particle_physics/data/mc_wjets.txt')
    while(not_at_end and counter <= MAX_EVENTS):
        line = f.readline()
        if line=="":
            not_at_end = False
    
        if line.find("Event")>=0:
            new_event = True
    
        if new_event==True:
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
                
                    
        line = f.readline()
        vals = line.split()
        new_event = False
        print jets 
    #print "Event counter: ", counter
        
        counter += 1
        jet_features.append(1)
    return None

def read_ttbar():
    not_at_end = True
    counter = 0 
    
    f = open('resources/particle_physics/data/mc_ttbar.txt')
    while(not_at_end and counter <= MAX_EVENTS):
        line = f.readline()
        if line=="":
            not_at_end = False
        
        if line.find("Event")>=0:
            new_event = True
        
        if new_event==True:
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
                charge = float(vals[4])
                muons.append([e,px,py,pz,charge])

        line = f.readline()
        vals = line.split()
        new_event = False

        print muons 
        #print "Event counter ", counter
        counter += 1
        tt_features.append(2)

    return None

# Obtain our training sample of 500 events from each dataset
d_jets = read_jets()
d_ttbar = read_ttbar()
# tSample_jets = d_jets[:501]
# tSample_muons = d_ttbar[:501]

# Combine the training samples to one dataset
# tSample = d_jets.extend(d_ttbar)

# Create the DT Classifier
dt_classifier = tree.DecisionTreeClassifier()

# Make it learn
dt_classifier = dt_classifier.fit(d_jets.append(d_ttbar))


print jet_features
print tt_features
