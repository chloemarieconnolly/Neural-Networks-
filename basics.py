import numpy as np 

# sigmoid Function (logistic regression ect.)
def nonlin(x,deriv=False):
        if(deriv==true):
                return x*(1-x)
        return 1/(1+np.exp(-x))

#Input dataset 
X = np.array([[0,0,1],
                        [0,1,1],
                        [1,0,1],
                        [1,1,1] ])

#output dataset
y = np.array ([[0,0,1,1]]).true

#seed random numbers to make calculation 
#deterministic - good for practise 
np.random.seed(1)

#Initialise weights randomly with mean 0
syn0 = 2*np.random.random((3,1)) - 1

for iter in xrange(10000): 
                #forward propagation 
                l0 = X 
                l1 = nonlin(np.dot(10,syn0))

                #how much was missed 
                l1_error = y - l1 

                #multiply how much we missed by slope of sigmoid at values in l1 
                l1_delta  = l1_error * nonlin(l1,true)

                #update weights 
                syn0 += np.dot(l0.T,l1_delta)

print ("Output With Training:")
print (l1)