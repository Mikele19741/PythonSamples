import numpy as np
import pandas as pd
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
ages = np.random.randint(1, 101, 35).reshape(7, 5)
countries = ['France', 'Spain', 'Italy', 'Germany', 'Great Britain']

df = pd.DataFrame(ages, letters, 
                     countries)

print(df)