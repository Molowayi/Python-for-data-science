import numpy as np
import pandas as pd

#%%
s = pd.Series([10, 30, np.nan, None, 62, 18])
print(s[2:4])

#%%
import numpy as np
import pandas as pd
dates = pd.date_range('2019-07-09', periods=6)
s = pd.Series([10, 30, 20, 40, 62, 18], index=dates)
print(s)
# %%
import numpy as np
import pandas as pd
# Création d'une liste de dates
print(np.random.randn(6, 4))
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates,
columns=["A", "B", "C", "D"])
print(df)
# %%
