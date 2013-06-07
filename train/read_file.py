from sklearn import tree
import numpy as np

import matplotlib.pylab as plt

import re

# Topic extracted from the KiswahiliWiki
k_file = "Topic/Kishanje.txt"

# Topic extracted from the EnglishWiki
e_file = "Amoeboid.txt"

sw_in_data=[]
en_in_data=[]
    
with open(k_file) as infile:
    sw_in_data = infile.read().replace('\n','')

with open(e_file) as infile:
    en_in_data = infile.read().replace('\n','')

# Split the topics into sentences
sw_sentences = re.split('[.]',sw_in_data)
en_sentences = re.split('[.]',en_in_data)

# Find and count occurances of letter 'a' and 'e' in each sentence and store in our training array
# This will be used to train the decision tree classifier
sw_train_array = []
en_train_array = []

for sentence in sw_sentences:
    occurance_a = sentence.count('a')
    occurance_e = sentence.count('e')
    occurance_u = sentence.count('u')
    occurance_p = sentence.count('p')
    #compute the ratio of occurance against length of the string 
    if occurance_a > 0 or occurance_e > 0 or occurance_u > 0 or occurance_p > 0:
        ratio_a = float(occurance_a) / len(sentence)
        ratio_e = float(occurance_e) / len(sentence)
        ratio_u = float(occurance_u) / len(sentence)
        ratio_p = float(occurance_p) / len(sentence)
        sw_train_array.append([ratio_a, ratio_e,ratio_u, ratio_p])

for sentence2 in en_sentences:
    occurance_a2 = sentence2.count('a')
    occurance_e2 = sentence2.count('e')
    occurance_u2 = sentence.count('u')
    occurance_p2 = sentence.count('p')
    #compute the ratio of occurance against length of the string
    if occurance_a2 > 0 or occurance_e2 > 0 or occurance_u2 > 0 or occurance_p2 > 0:
        ratio_a2 = float(occurance_a2) / len(sentence2)
        ratio_e2 = float(occurance_e2) / len(sentence2)
        ratio_u2 = float(occurance_u2) / len(sentence2)
        ratio_p2 = float(occurance_p2) / len(sentence2)
        en_train_array.append([ratio_a2, ratio_e2,ratio_u2, ratio_p2])

# Reduce value of english training data to 17 ratios
en_train_array = en_train_array[:18]

print "Length of Number of Kiswahili sentences", len(sw_sentences)
for line in sw_train_array:
    print line

print "Length of Number of English sentences",  len(en_sentences)
for line in en_train_array:
    print line

# Make the training sample for our dataset
sw_train_array.extend(en_train_array)
training_sampleX = np.array(sw_train_array)

# Make for the Y-axis
training_sampleY = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])

# Create the DT Classifier
dt_classifier = tree.DecisionTreeClassifier()

# Make it learn
dt_classifier = dt_classifier.fit(training_sampleX,training_sampleY)

# Some imaginary testing samples
print dt_classifier.predict([[85.9320,-19.5623,54.8418,62.4199  ],[13.7642,1.3216,11.0690,-8.0736 ]])

# Let's do some plotting
new_training_sampleX = training_sampleX.swapaxes(0,1)
print new_training_sampleX

# Plot the training samples to see how ``different" they are.
plt.figure()
plt.plot(new_training_sampleX[0],new_training_sampleX[1],'o')
plt.xlim(0,8)
plt.ylim(0,8)

plt.figure()
plt.plot(new_training_sampleX[0],new_training_sampleX[2],'o')
plt.xlim(0,8)
plt.ylim(0,8)

plt.figure()
plt.plot(new_training_sampleX[1],new_training_sampleX[2],'o')
plt.xlim(0,8)
plt.ylim(0,8)

plt.figure()
plt.plot(new_training_sampleX[2],new_training_sampleX[3],'o')
plt.xlim(0,8)
plt.ylim(0,8)


plt.show()





