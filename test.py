import pandas as pd
import numpy as np

df = pd.DataFrame([('bird', 389.0),
                   ('bird', 24.0),
                   ('mammal', 80.5),
                   ('mammal', np.nan),
                   ('mammal', 10)],
                  
                  columns=('class', 'max_speed'))

df.rename(index={0: 'row', 1: 'row2', 2: 'row3', 3: 'row4', 4: 'row5'})
#df.set_index(['row', 'row2', 'row3', 'row4', 'row5'], inplace=True)                
#df.index = ['row', 'row2', 'row3', 'row4']
#df.set_index(['1', '2', '3', '4'], inplace=True)
print(df)
