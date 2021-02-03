import pandas as pd
import json

from dummy_data import myl

# convert incomming data to nested list
funcs = lambda x: [i.split('\t') for i in x.split('\n')]

df = pd.DataFrame(myl, columns = ['ts', 'value']).astype(
    {'ts': 'datetime64', 'value': 'float'}
)


print(df.dtypes)
#print(pd.api.types.infer_dtype(df))