import json
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from dummy_data import myl


class Predator:

    def __init__(self):
        
        """ """

    def crunch(self, df, n_lags=5, n_steps=5):

        # params recieved from app
        self.n_lags = n_lags       
        self.n_steps = n_steps
        
        # function to convert incomming data to nested list
        string_tolist = lambda x: [i.split('\t') for i in x.split('\n')]
        df = string_tolist(df)
        
        # make initial data frame
        df = pd.DataFrame(df, columns = ['ts', 'value']).astype(
            {'ts': 'datetime64', 'value': 'float'}
        ).sort_values(by='ts', ascending=True)

        # data frame frequency
        self.freq = __freq_infer(df)

        # final data frame after interpolation
        self.df = __interpolate(df)


    

    def __freq_infer(df):

        """ function infers frequency of time seris """
        
        # infer frequency in seconds
        freq = max([df['ts'][i] - df['ts'][i - 1] for i in range(1, 10)]).total_seconds()
        # convert to minutes
        freq = str(int(freq / 60)) + 'T'

        return freq

    def __interpolate(df):

        """ function interpolates data if gaps exits"""
        
        # identify start and end dates
        start, end = df.iloc[0,0], df.iloc[-1, 0]
        # generate period
        dates = pd.DataFrame(pd.date_range(start=start, end=end, freq=freq), columns =['ts'])
        # join original data frame and interpolate data
        df = pd.merge(dates ,df, 'left', on='ts').interpolate()

        return df

    def __reshape():
        # values as np array
        df_arr = df.values[:, [1]]
        # add X values to array
        xy_arr = np.concatenate(
            tuple(map(lambda x: np.roll(df_arr, x), np.arange(n_lags + 1)[::-1])),
            axis=1
        )[n_lags:,:]

        # initial X row
        X_sample = xy_arr[-1:, 1:]
        # inital convertion row for y
        y_pred_init = xy_arr[-1:, -1:]

        # train sets
        X_train = xy_arr[1:, :-1]
        y_train = np.diff(xy_arr[:, -1:], axis=0)

        # train
        model = RandomForestRegressor()
        model.fit(X_train, y_train)


        # predict
        # instantiate empty prediction array
        preds = np.array([])
        for i in range(n_steps):
            # predict sample
            y_pred = model.predict(X_sample)
            # roll and add final prediction
            X_sample = np.roll(X_sample, -1)
            X_sample[:, -1] = y_pred + X_sample[:, -2]
            # update prediction array
            preds = np.append(preds, X_sample[:, -1])


