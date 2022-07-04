import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('ggplot')
np.random.seed(69)
y = np.random.randint(0, 100, 10_000)
population_std = y.std()
def SE(x, n):
  return population_std / np.sqrt(n)
samples = [np.random.choice(y, size=x, replace=False) for x in range(1, 10000)]
population_av = y.mean()
se = []
for x in samples:
  n = len(x)
  iterable = SE(x, n)
  se.append(iterable)
av = []
for x in samples:
  av.append(x.mean())
se = np.array(se)
x = np.arange(1, len(se)+1)
fig, (ax1, ax2) = plt.subplots(ncols=2, nrows=1, figsize=(20, 10))
ax1.plot(x, se, label='Standard Error')
ax1.set(
    title=" Standard Error in function of Sample Size", 
    xlabel="Sample Size", 
    ylabel="Standard Error"
)
ax1.legend()
ax2.scatter(x, av, s =4, label='Sample\'s Average in function of Samples size')
ax2.axhline(population_av, color='g', label='Population\'s average')
ax2.set(
    title="Averages", 
    xlabel="Sample Size", 
    ylabel="Average"
)
ax2.legend()
#fig.savefig('lln.png')
