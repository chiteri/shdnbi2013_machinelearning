import argparse
import numpy as np 
import matplotlib.pylab as plt 
from event import Jet, Lepton, Particle, MET 

def HEP_tutorial(data_file): 
    MAX_EVENTS = 200000 # A symbollic constant to determine the upper limit of events to process
    muons_masses = [ ] # Collect all the masses for our parent particles 
    events_encountered = 0 # Starting with the first one
    
    # Open the first file and read its content
    # With statement makes sure to close the file after you are done
    with open(data_file, 'r') as file:
        # while(True and events_encountered < MAX_EVENTS): 
        while(True): # Loop forever 
            # Read the data obtained row by row 
            row = file.readline() 
        
            if row == '': break # Stop execution, no more items to read
 
            if row.find('Event:') >= 0: events_encountered += 1 
            print 'Event count: {}'.format(events_encountered)

            # From the format given, the next item to expect is the number of jets in the event 
            jets = [] 
            no_of_jets = int(file.readline()) 

            for i in xrange(no_of_jets): 
                jet_info = file.readline().split()  
                jets.append( Jet (float(jet_info[0]), float(jet_info[1]), float(jet_info[2]),\
                float(jet_info[3]), float(jet_info[4]) ) ) 

            # print jets 

            # Next we get information on muons for this event 
            muons = [] 
            no_of_muons = int(file.readline())

            for i in xrange(no_of_muons): 
                muon_info = file.readline().split() 
                muons.append( Lepton( 'Muon',  float(muon_info[0]), float(muon_info[1]), \
                float(muon_info[2]),float(muon_info[3]), int(muon_info[4]) ) )

            # print muons

            # After that electrons follow 
            electrons = [] 
            no_of_electrons = int (file.readline())

            for i in xrange(no_of_electrons):
                electron_info = file.readline().split() 
                electrons.append(Lepton('Electron', float(electron_info[0]), float(electron_info[1]),\
                float(electron_info[2]), float(electron_info[3]), int(electron_info[4]) ))

            # print electrons

            # Second to last we inspect the photons 
            photons = [] 
            no_of_photons = int (file.readline())

            for i in xrange(no_of_photons): 
                photon_info = file.readline().split() 
                photons.append(Particle( float(photon_info[0]), float(photon_info[1]), float(photon_info[2]),\
                float(photon_info[3]) ))

            # print photons

            # Finally we get to the Missing transverse energy 
            met_values = file.readline().split()
            met_info = MET(float(met_values[0]), float(met_values[1])) 
 
            # print met_info  

            # Once we are done with getting information for each event, 
            # we can do a calculation of their masses accumulated so far 
            for muon in muons: 
                # print muon 
                mass = np.sqrt(muon.energy**2 - ( muon.x_coord**2 + muon.y_coord**2 + muon.z_coord**2 ) )
                muons_masses.append(mass)

                # print 'The invariant mass of the muon is {}'.format(mass) 
            # break 

    # Plot the data on a histogram 
    plt.hist(muons_masses, range=(0, 1), bins=100)
    plt.show()


if __name__ == '__main__': 
    # Get the parameters with the file name passed from the command line
    parser = argparse.ArgumentParser(description='Show the accumulation of masses for different particles in C.M.S data.')
    parser.add_argument('-f', '--file', type=str, nargs='+', help='The paths to the file(s) holding the input data.') 

    args = parser.parse_args() 

    HEP_tutorial(args.file[0]) 
