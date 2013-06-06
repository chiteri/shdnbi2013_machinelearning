from sklearn import tree
import numpy as np

import matplotlib.pylab as plt

################################################################################
# Make some fake datasets with 3 variables.
# The first four entries are dataset 1 and the second 4 are dataset 2.
#
# These are referred to as TRAINING samples.
################################################################################
X = np.array([[1, 1, 2], \
              [1, 2, 1], \
              [2, 1, 2], \
              [2, 2, 1], \
              [6,6, 5], \
              [6,7, 5], \
              [7,6, 6], \
              [7,7, 6]])

# We need this to show that the first 4 are dataset 1 and the second 4 are 
# dataset 2.
Y = np.array([1, 1, 1, 1, 2, 2, 2, 2])

# Create the Decision Tree Classifier. This class will ``learn" to distinquish
# between the different datasets.
clf = tree.DecisionTreeClassifier()

# This is where the class actually ``learns".
clf = clf.fit(X, Y)

# Now that it has been ``taught", we use it to make a prediction as to what
# dataset these two data points are from. 
#
# These are referred to as TESTING samples.
print clf.predict([[5,5,5],[1,2,1]])

################################################################################
# We need to do this to can plot these variables
################################################################################
newX = X.swapaxes(0,1)
print newX

# Plot the training samples to see how ``different" they are. 
plt.figure()
plt.plot(newX[0],newX[1],'o')
plt.xlim(0,8)
plt.ylim(0,8)

plt.figure()
plt.plot(newX[0],newX[2],'o')
plt.xlim(0,8)
plt.ylim(0,8)

plt.figure()
plt.plot(newX[1],newX[2],'o')
plt.xlim(0,8)
plt.ylim(0,8)

plt.show()
