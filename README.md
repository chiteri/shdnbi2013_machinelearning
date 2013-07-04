SCIENCE HACK DAY, Nairobi - 2013: MACHINE LEARNING FOR PHYSICS
===============================================================

A project based on ideas of Machine Learning _(M.L)_ : We need to train computers to accurately recognize sentences in either Swahili or English out of reading entries from Wikipedia from both languages. We will then use similar rules and techniques to detect the presence of particular sub-atomic particles inside Physics data collected by collaborators at the Compact Muon Solenoid (C.M.S) experiment at CERN.


scikit-learn example and our experiements at Siena. 
======================================================= 
``Hi Morris and Martin,

   It's great to see you've already started looking at the scikit-learn tools! That will probably really help things this weekend. 

  Here at Siena, I've started to look into this stuff as well with a student of mine, Jess Muenkel (cc'ed on this email). I've wanted to look at these python tools for some time, so this is a great excuse for me to dedicate this time!  :)

   I've attached the very first example that Jess and I wrote. All of this is based on the scikit examples. For now, we've chosen to focus on the Decision Tree (DT) algorithm, as I think it's supposed to be relatively easy to use. I should point out, we've not spent any time trying to actually learn what the algorithm does (yet) we've only got it to work. 

http://scikit-learn.org/stable/

http://scikit-learn.org/stable/modules/tree.html

   The example (reasonably commented) walks through the standard procedure for ML (Machine Learning):

  * Choose an algorithm.

  * Give it two (or more) datasets from different populations. These are called TRAINING samples. 

   * Train the algorithm. 

   * Give it another sample of *different* data where you know the answers and see how well the algorithm predicts the dataset. This is called the TESTING sample. 

   If you have scikits and matplotlib installed, you should be able to run this. In fact, I urge you to test it out and hand it out to others as a ``hello world" type example. 

   Once Jess and I had this running, I had Jess pull about 400 sentences (randomly) from the Swahili and English versions of Wikipedia. We then split each of these in half: 200 sentences for training and 200 for testing. 

    Jess then wrote a python program to count the frequency of certain letters in *each sentence*. She created files that have one line per sentence on which is the percentage a letter appears *in that one sentence*. She has one set of files for Swahili and one set for English. So the first few lines look something like this:

0.131868 0.087912 0.098901 0.076923 0.065934
0.153061 0.091837 0.051020 0.081633 0.091837
0.157895 0.073684 0.105263 0.042105 0.115789
0.170213 0.056738 0.127660 0.049645 0.042553
0.212121 0.050505 0.121212 0.020202 0.060606
0.240000 0.053333 0.106667 0.040000 0.066667

   I won't tell you what letters we've chosen (that's for the Hack Day! :)), but with just a few we can tell you whether or not a sentence is in Swahili or English with about 97% accuracy! *Just* from single letter counts! We were quite surprised and impressed with the algorithm!

   We stayed away from letters that might not appear in both languages like ``q". 

   Anyways, this is very analagous to what high-energy particle physicists do with our data. We measure some quantities (letters) in our detector and for each proton-proton collision (sentence) we look for some combination of those measured quantities (frequency of letters, for example) that can help us decide whether or not an event produced a W boson or top-quark (Swahili or English). I think this might be an interesting roadmap for how to approach this type of project for the Hack Day. 

   As always, it's *you guys* that are running the event. I'm only here to help and provide data and ideas. So feel free to come up with your own approach....this is only one suggestion. 

   Tomorrow, Jess and I will prepare some CMS data for you to play with. But even just trying out the language stuff will be challenging. I *think* if you write your code generally to read in data like the above sample, it will be interchangeable between the language and CMS example. At least I think so.  :)    We'll see how it all works out!

* For the hackday itself (or just before?)
========================================= 
Once you understand the code, I would recommend this:

* Grab a few hundred sentences in Swahili and English and put them into separate text files. 
* Write some code to count up the number of times a particular letter appears in each sentence. Maybe start with ``a" and ``e".
* Write to a file the fractional amount that letter appears. For instance, if there are 5 ``e"s in a 100 letter sentence, you would write out 0.05. Write these out as columns. 
* Modify this example to read in those files and put them into the ``X" array. 

   Of course, this can all be done at the Hack Day, but you can help others if you already have some starter code. 

   Also, think about if there's anyway to post these exercises (and the work that the other hackers do) online for others to learn from. Maybe some nice webpage of the work or even making one of Github's pages? I've never done that but maybe one of the other hackers has experience? Just a thought. 

* Notes on the screen-shot attached (Check inside the folder named ``resources") 
=================================================================================
 Also, your screen shots look exactly like what we get. Those ``datasets" are completely arbitrary. You can imagine that they might represent frequency of letters, or energy of particles, or heights of people, but the point is that with the naked eye we can see that there are two distinct populations of whatever they are. It's a 3D dataset (every entry in a dataset is defined by three numbers) so I plotted each 2D relationship: x vs y, x vs z, y vs z. Just to try to give some sense of how different they are.  

 
* Physics quantities and concepts
=======================================

_Charge: (q)_ 
This refers to electrical charge, positive or negative. A proton has a positive charge and an electron has a negative charge. 

If you have a positive and a negative charge in the same system, for example a single electron around a proton in a hydrogen atom, that system is electrically neutral. In a similar fashion, a neutral particle can decay (or break up) into two charged particles: one positive (+) and one negative (-).


_Mass: (m)_
Mass is basically what you think it is. It’s not quite the weight of an object (that’s more related to how much gravity is pulling on it...which is related to mass). Think of it as how much an object resists being pushed on. If an object has large mass and I push on it, it will move very slowly. If an object has small mass and I push on it, it will move faster!


_Energy: (E)_
This general idea of energy includes the kinetic energy (KE = ½ mv^2) that we learned about in school. For our purposes, we can think of the energy of these particles as related to the kinetic energy plus their mass.


_Momentum: (p)_
Momentum is the mass of an object multiplied by its velocity (p=mv) in the simplest definition. You would think that this sounds like the energy....but it’s not quite. In fact, it is the relationship between these quantities that helps us make new discoveries! Momentum is a vector and has an x-component, a y-component, and a z-component.


_Relativistic dynamics:_
Einstein taught us that mass, energy, and momentum are related in a very particular way that is different from what Newton taught us. 


From these relationships we can discover new particles!


_Lifetime:_ 
As far as we know, the proton and electron (as found in atoms) live forever. At least, we have never seen them spontaneously decay or turn into multiple lighter particles. 

However, not all particles are like that. A neutron, if it is not in the nucleus of an atom, will decay into a proton, and electron, and an anti-neutrino, on average in about 10 minutes. We write that reaction down as

     n p e-

Some particles can live for only 10-8 seconds or even only 10-23 seconds! Because of this, we can only infer their existence by looking at the particles to which they decay. 



_Units, constants, and a sense of scale_

The following is a discussion of units and constants commonly used in particle physics. They are not the only units one can use, but they will work for us. 

*c* - _This is the speed of light, 3x108 m/s._ It is often multiplied by other quantities to make the units work out properly. 

*Energy* - _electron volts (eV)._ An electron volt is the energy an electron gains when it is accelerated across a 1 Voltage potential. In particle physics, we tend to use giga electron volts (GeV). 

*Momentum* - _eV/c (or GeV/c)._ Note that dividing by c just makes the units come out right. With the files you will work with, the c is already multiplied by the momentum, which makes doing the calculations much easier. 

*Mass* - _eV/c2 ( or GeV/c2)._ Yes! Mass and energy have effectively the same units and are interchangeable! Hmmmm....where have I heard that before.  :)


For a sense of scale, a proton has a mass of about 1 GeV/c2 (0.938272 to be exact). An electron has a mass of only 0.000511 GeV/c2.  A photon, which is a particle of light, has no mass!!!


At the LHC, the protons are accelerated until they have an energy of 7 TeV or 7000 GeV! This is like taking 7000 protons, converting them to pure energy, and then putting that energy into one proton! 

In the collisions, many, many, many particles are produced that have energies from 1-1000 TeV! But their mass, may only be between 0.1 and 200 GeV/c2. Does that make sense to you? If not, look at the above equations about relativistic kinematics. 


*The particles
=================

While there are many different types of fundamental particles, most of them live for such a short period of time, that they decay before they ever actually hit the detector. There are only a handful of particles that actually strike the detector and leave their signatures. The data files you will work with focus on 3 particles and 1 ``collection” of particles.

*Photons:* 
Photons are particles of light and have no mass. One way that the Higgs boson was discovered was by looking at events that had two-photons and combining them to see what they came from. Photons have no charge. 

*Electrons:*
These are the same electrons that are found in everyday atoms....except that they are much more energetic when they are produced in collisions at the LHC. Electrons are negatively (-) charged, but in the LHC you can also find their antimatter version which is positively (+) charged.

*Muons:*
Muons are in the same family of particles (leptons) as electrons. Like electrons, they are also negatively (-) charged and also have an antimatter version which is positively (+) charged.

*Jets:*
This one is a bit tricky, because it’s just one particle. It’s a spray of many particles. When a single quark is produced at the LHC, it pulls other quarks out of the vacuum and creates a spray of particles (pion and kaons mostly) that all travel in roughly the same direction. However, you can add up all the energy and momentum of those particles to define an energy and momentum for the jet itself! Jets are one way to ``see” the top-quark. 

One quantity in the files is for the jets there is b-tag number. This tells you how likely or unlikely it is that the jet came from the relatively heavy b-quark. 



*Data structure:*

The files you have all have the same format:

_Event #:_
<number of jets>
<jet 0 energy> <jet 0 x-momentum> <jet 0 y-momentum> <jet 0 z-momentum> <b-tag>
<jet 1 energy> <jet 1 x-momentum> <jet 1 y-momentum> <jet 1 z-momentum> <b-tag>
.
.

_<number of muons>_
<muon 0 energy> <muon 0 x-mom> <muon 0 y-mom> <muon 0 z-mom> <charge>
.
.

_<number of electrons>_
<elec 0 energy> <elec 0 x-mom> <elec 0 y-mom> <elec 0 z-mom> <charge>
.
.
.

_<number of photons>_
<phot 0 energy> <phot 0 x-mom> <phot 0 y-mom> <phot 0 z-mom>
.
.

_<missing momentum in the x-direction> <missing momentum in the y-direction>_

Event #:
.
.
.


Here are some ideas for ``hacks” of the CMS data. However, you should use your own imagination and scientific curiosity to motivate your work! However, I encourage you to post your work so that others might see what you have done and be inspired by your projects. 


_In the Dropbox folder are 5 files: 1 data file and 4 Monte Carlo files that simulate particular physics processes._ 


data.txt.  These are real data from the CMS (http://cms.web.cern.ch/) experiment at CERN. Because they’re real data, we don’t actually know what the events are! At least not on an event-by-event basis.

mc_ttbar.txt. This is a simulation of proton-proton collisions that produce a top quark (t) and an anti-top (tbar) quark, along with other random particles. The top quarks decay very quickly though, so they must be reconstructed. 

mc_wjets.txt. This is a simulation of proton-proton collisions that produce a W boson some jets, along with other random particles. The W bosons decay very quickly though, so they must be reconstructed. 

mc_dy.txt. This is a simulation of proton-proton collisions where a quark and an antiquark hit each other and annihilate, producing a virtual photon. This leads to a production of a particle called a Z boson. One ``hack” would be to find these particles in the data.

mc_qcd.txt. This is a simulation of proton-proton collisions where many quarks and gluons interact producing many random particles and jets. This is a major background of many analyses.


The format of these files is described in the previous document, ``Explanation of CMS data”. Here are some suggestions for possible hacks, in order of increasing challenge. 


*Hack #1. Look at the data!*

In the githib repository is a python script called read_HEPTutorial_data.py. If you run this on any of the files, it will find the muons and calculate their mass, according the physics of Einstein, Special Relativity. This will produce a histogram of each muon’s mass and should be centered around 0.105 GeV/c2. You can run this in the terminal as

python read_HEPTutorial_data.py  mc_dy.txt

Though you can run this on any of the files. Great! You’ve started to hack the CMS data!


*Hack #2. Improve the code.*

If you are looking for a coding challenge, check out this read_HEPTutorial_data.py script. Now that you know what it is doing and what the data look like, can you make any improvements to it? Either the script or the data structure? 


*Hack #3. Find the Z-boson in the simulation.*

Modify the code (or make a new copy to modify) so that it looks for events with 2 or more muons. If the muons are opposite charges, then add the two muons energy, px, py, and pz together. When they are added, calculate the mass and make a histogram. You should see a large peak at about 91 GeV/c2. Make sure the range on your histogram is set wide enough!

If you find the Z-boson, set the scale to look at masses less than 15 GeV/c2. Are there any other particles/bumps down here? What are they?


*Hack #4. Find the top-quark in the simulation.*

Modify the code (or make a new copy to modify) so that it looks for events with 3 or more jets, where one of the jets is a b-jet (make sure the b-quark jet tag is greater than 0) . Add the three jets’ energy, px, py, and pz together. When they are added, calculate the mass and make a histogram. You might see a peak around 170 GeV/c2. (I’ve actually not done this yet, so I hope it works!)


*Hack #5. Find the top-quark in the data using Machine Learning.*

Try to take the ML code you used to disentangle languages and apply it to the physics data. For example, ttbar and qcd or ttbar and wjets. To do this, you will need to run over each event and dump some information to files about each event. You can use this to ``train” the ML code to recognize different events. If you ``test” that this works, then apply it to the data to select out ttbar events. Then, run the previous code to see if you can plot the top-quark in the data!

The challenging part will be figuring out what values to calculate for different events. Some suggestions might be: momentum of highest momentum jet and/or muon and/or electron, Number of photons, number of jets, MET_tot (sqrt(MET_px*MET_px + MET_py*MET_py)), total energy of all the jets, etc. I actually don’t know what the answers are, so it will be interesting to find out!



Good luck! And let me know what you find!	


-- 
-- 
----------------------------
Matt Bellis
Siena College
mbellis@siena.edu
http://www.mattbellis.com
----------------------------

" 


More links: 
____________ 
* SciKit Learn: http://scikit-learn.org/stable/

* Decision trees using SciKit Learn: http://scikit-learn.org/stable/modules/tree.html 

* C.M.S (Compact muon solenoid's) experiment's event viewer: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookFireworks 

* Genism, for collecting a bag of words from Wikipedia dumps: http://radimrehurek.com/gensim/index.html

* Science hack day, Nairobi - 2013: Ideas Wiki => http://shdnairobi.pbworks.com/w/page/66494507/SHD%20Nairobi%202013%2C%20Hack%20ideas 

