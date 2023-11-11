import numpy as np
rng=np.random.default_rng() 
train_n=100 
test_n=1000 
d=100 
mu=np.zeros(d)

#Generate random dxd covariance matrix 
A=np.random.rand(d,d) 
while np.linalg.matrix_rank(A)!=d: 
    A=np.random.rand(d,d) 
Cov=A.T@A 

sigma_noise=rng.uniform(0.3,0.7)

#Generate training and test data 
X_train=rng.multivariate_normal(mu,Cov,size=train_n) 
a_true=rng.normal(0,1,size=(d,1))
y_train=X_train.dot(a_true)+np.random.normal(0,sigma_noise,size=(train_n,1)) 
X_test=rng.multivariate_normal(mu,Cov,size=test_n) 
y_test=X_test.dot(a_true)+np.random.normal(0,sigma_noise,size=(test_n,1))

