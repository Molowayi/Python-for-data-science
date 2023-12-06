#%%
import matplotlib.pyplot as plt
import numpy as np
plt.plot([1, 3, 2, 4])
plt.ylabel('some numbers')
plt.show()

#%%


x = [1, 5, 6, 10]
y = [n**2 for n in x]
plt.plot(x,y,"0")
plt.show()

#%%
x = np.linspace(-5, 5, 200)
y = np.sin(x) # y = x**2   
plt.plot(x,y,"o")
plt.show()


# %%
