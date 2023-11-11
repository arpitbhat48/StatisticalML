import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

n = 1000
Z = np.random.randn(n)
plt.step(sorted(Z), np.arange(1,n+1)/float(n), label = "Gaussian")
# plt.hist(Z,250)

li = [1, 8, 64, 512]

for k in li:
    sums = np.sum(np.sign(np.random.randn(n, k))*np.sqrt(1./k), axis=1)
    plt.step(sorted(sums), np.arange(1,n+1)/float(n), label = k)
    
plt.step(sorted(Z), np.arange(n)/float(n), label = "Gaussian")
# sns.kdeplot(np.arange(n), cumulative = True)
plt.legend()
plt.title("Cumulative Distribution")
plt.xlabel("Observations")
plt.ylabel("Probability")
plt.show()
