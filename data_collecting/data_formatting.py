#
#
# Yunusemre Ozkose
# 23.10.21
#

import os
import pandas as pd
import matplotlib.pyplot as plt

from glob import glob
from config import Config
from utils import date2timestamp

from os.path import join as p_join


def drop_some_columns(data):
    data = data.drop(columns="bat")
    data = data.drop(columns="baro")
    data = data.drop(columns="vgx")
    data = data.drop(columns="vgy")
    data = data.drop(columns="vgz")
    data = data.drop(columns="agx")
    data = data.drop(columns="agy")
    data = data.drop(columns="agz")
    return data


def read_data_wind(path):
    xls = pd.ExcelFile(path)
    data_wind = xls.parse(0)

    # Date to Timestamp
    for index, row in data_wind.iterrows():
        data_wind.loc[index, 'Time'] = date2timestamp(str(row["Time"]))

    # Reverse dataframe
    data_wind = data_wind[::-1].reset_index(drop=True)

    # Drop No. column
    data_wind = data_wind.drop(columns="No.")

    # rename
    data_wind = data_wind.rename(columns={'Time': 'timestamp'})

    # set timestamp as index
    # data_wind.set_index('timestamp', inplace=True)

    # set timestamp column as string
    data_wind['timestamp'] = data_wind['timestamp'].astype(str)
    cols = data_wind.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    data_wind = data_wind[cols]

    return data_wind


def read_drone_data(drone_data_folder):
    log_all = None
    for path in sorted(glob(os.path.join(drone_data_folder, "*.txt"))):
        try:
            log = pd.read_table(path, dtype={'timestamp': str})
        except pd.errors.EmptyDataError:
            continue

        # pass empty logs
        if len(log) == 0:
            continue

        # first column is usually empty, hence pass it
        if log_all is None:
            log_all = log
        else:
            log_all = log_all.append(log)

    log_all = log_all.reset_index(drop=True)

    log_all = log_all[log_all['pitch'].notna()]

    # Drop some columns to observe better
    log_all = log_all.drop(columns="time")
    # log_all = log_all.drop(columns="baro")
    log_all = log_all.drop(columns="tof")
    # log_all = log_all.drop(columns="templ")
    log_all = log_all.drop(columns="temph")

    return log_all


def combine_data(data_wind, data_drone) -> pd.DataFrame:
    wind_dict = {int(float(row["timestamp"])): row["Wind Speed"] for index, row in data_wind.iterrows()}

    wind_list = []
    for index, row in data_drone.iterrows():
        ts = int(float(row["timestamp"]))

        if ts in wind_dict.keys():
            wind_list.append(wind_dict[ts])
        else:
            wind_list.append(-1)

    data_drone['wind speed'] = wind_list
    return data_drone


def plot_data(data_wind, data_drone):
    data_wind.plot()
    plt.savefig("plots2/wind.png")
    plt.show()
    plt.close()

    data_drone.plot()
    plt.savefig("plots2/drone.png")
    plt.show()
    plt.close()


def normalize(df):
    for col_name in df.columns:
        if col_name in ["timestamp"]:
            continue
        df[col_name] = df[col_name] / df[col_name].abs().max()
    return df


if __name__ == "__main__":
    config = Config

    data_wind = read_data_wind(config.paths.wind_data_xls_path)
    data_drone = read_drone_data(config.paths.drone_data_folder)
    data = combine_data(data_wind, data_drone)

    data_wind2 = read_data_wind(config.paths.wind_data_xls_path2)
    data_drone2 = read_drone_data(config.paths.drone_data_folder2)
    data2 = combine_data(data_wind2, data_drone2)

    data = pd.concat([data, data2], ignore_index=True)
    data.to_csv(p_join(config.paths.save_folder, "combined.csv"), index=False)
