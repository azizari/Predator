import json
from dummy_data import myl
import numpy as np
import pandas as pd


#class
#def __init__():
# convert incomming data to nested list
funcs = lambda x: [i.split('\t') for i in x.split('\n')]

# make initial data frame
df = pd.DataFrame(myl, columns = ['ts', 'value']).astype(
    {'ts': 'datetime64', 'value': 'float'}
).sort_values(by='ts', ascending=True)

# params recieved from app
n_lags = 5
n_steps = 5


# def freq_infer():
# infer frequency in seconds
freq = max([df['ts'][i] - df['ts'][i-1] for i in range(1,10)]).total_seconds()
# convert to minutes
freq = str(int(freq/60))+'T'

# def interpolate():
# identify start and end dates
start, end = df.iloc[0,0], df.iloc[-1, 0]
# generate period
dates = pd.DataFrame(pd.date_range(start=start, end=end, freq=freq), columns =['ts'])
# join original data frame and interpolate data
df = pd.merge(dates ,df, 'left', on='ts').interpolate()

# def reshape():
# values as np array
df_arr = df.values[:, [1]]
# add X values to array
xy_arr = np.concatenate(
    tuple(map(lambda x: np.roll(df_arr, x), np.arange(n_lags + 1)[::-1])),
    axis=1
)[n_lags:,:]


# split X/y and differentiate y values
X = xy_arr[:, :-1]
# store final value
y_init = xy_arr[-1, -1]
# differentiate y values
y = np.diff(xy_arr[:, -1:], axis=0)



# do preiction



# take cumulative sum
y = np.cumsum(np.vstack((y_init, y)))[1:]









