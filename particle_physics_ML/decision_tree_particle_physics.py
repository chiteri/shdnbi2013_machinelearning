from sklearn import tree
import numpy as np

import sys

import matplotlib.pylab as plt

infilename0 = sys.argv[1]
infilename1 = sys.argv[2]
infilename2 = sys.argv[3]

infile0 = open(infilename0,'r')
infile1 = open(infilename1,'r')
infile2 = open(infilename2,'r')

#Xtrain = np.array([])
#Ytrain = np.array([])
#Xtest = np.array([])

Xtrain = -999*np.ones(2500000).reshape(500000,5)
Ytrain = -999*np.ones(2500000)
Xtest = -999*np.ones(2500000).reshape(500000,5)


nlines = 0
for i,line in enumerate(infile0):
    #Xtrain = np.append(Xtrain,np.array(line.split()).astype('float'))
    #Ytrain = np.append(Ytrain,0)
    Xtrain[nlines] = np.array(line.split()).astype('float')
    Ytrain[nlines] = 0
    nlines += 1

print "Read in the first training file...."

for line in infile1:
    #Xtrain = np.append(Xtrain,np.array(line.split()).astype('float'))
    #Ytrain = np.append(Ytrain,1)
    Xtrain[nlines] = np.array(line.split()).astype('float')
    Ytrain[nlines] = 1
    nlines += 1

print "Read in the second training file...."

# Trim off the excess entries.
Xtrain = Xtrain[Ytrain>-999]
Ytrain = Ytrain[Ytrain>-999]

#Xtrain = Xtrain.reshape(nlines,5)
print Xtrain

#nlines = 0
    #for line in infile2:
    #Xtest[nlines] = np.array(line.split()).astype('float')
    #Xtest = np.append(Xtest,np.array(line.split()).astype('float'))
#nlines += 1

#Xtest = Xtest.reshape(nlines,5)

##########################################################
# Our testing data for the ML algo -- added by @daaj
##########################################################
testing_file = open('testing.dat')
for line in testing_file:
    Xtest[nlines] = np.array(line.split()).astype('float')
    nlines += 1


# Make it so we can plot these variables
newXtrain = Xtrain.swapaxes(0,1)
newXest = Xtrain.swapaxes(0,1)

print newXtrain

for i in range(0,5):
    plt.figure()
    lo = min(newXtrain[i][Ytrain==0])
    hi = max(newXtrain[i][Ytrain==0])
    plt.hist(newXtrain[i][Ytrain==0],50,alpha=0.5,color='r',normed=1, histtype='stepfilled',range=(lo,hi))
    plt.hist(newXtrain[i][Ytrain==1],50,alpha=0.5,color='b',normed=1, histtype='stepfilled',range=(lo,hi))
    name = "wjets_ttbar_values_%d.png" % (i)
    plt.savefig(name)


clf = tree.DecisionTreeClassifier()
clf = clf.fit(Xtrain, Ytrain)

# Run your predictions on the test file.
predictions = clf.predict(Xtest)

print predictions
tot_pred = float(len(predictions))
print "npredictions==0: ",len(predictions[predictions==0])/tot_pred
print "npredictions==1: ",len(predictions[predictions==1])/tot_pred


plt.show()
