from pathlib import Path
from random import randint
# import random => random.randint(1, 10)

def my_dice(faces = 6):
    # return randint(1,6)
    print("faces : " + str(faces))
    result = randint(1, faces)
    return result

# print(my_dice())
#for _ in range(10):
#    my_dice()

dice1 = my_dice()
dice2 = my_dice(20)
value = dice1 + dice2

msg = f"{dice1: .2f} + {dice2} = {dice2 + dice1}"

print(msg)


# Attention à l'échapement des cartactères

import pandas as pd
import matplotlib.pyplot as plt

folder = Path(__file__).parent
# print(folder / "2018_sac_gas.csv")
df = pd.read_csv(folder / 'social_network_data.csv')
df_filtered = df[df["friends"] < 27]

#%%
vc = df["friends"].value_counts()
print("vc : \n", vc)
print("vc index : \n", vc.index)

plt.bar(vc.index, vc)
plt.show()