#
#
# Yunusemre Ozkose
# 23.10.21
#

import os
import pandas as pd
import matplotlib.pyplot as plt

from glob import glob
from data_collecting.config import Config
from data_collecting.utils import date2timestamp


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
    #data_wind.set_index('timestamp', inplace=True)

    # set timestamp column as string
    data_wind['timestamp'] = data_wind['timestamp'].astype(str)

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
        log = log[1:]

        if log_all is None:
            log_all = log
        else:
            log_all = log_all.append(log)

    log_all = log_all.reset_index(drop=True)

    # Drop some columns to observe better
    log_all = log_all.drop(columns="time")
    # log_all = log_all.drop(columns="baro")
    log_all = log_all.drop(columns="tof")
    log_all = log_all.drop(columns="templ")
    log_all = log_all.drop(columns="temph")
    log_all = log_all.drop(columns="Unnamed: 17")

    return log_all


def combine_data(data_wind, data_drone):
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


if __name__ == "__main__":
    config = Config

    data_wind = read_data_wind(config.paths.wind_data_xls_path)
    data_drone = read_drone_data(config.paths.drone_data_folder)

    print(data_wind.head())
    print(data_drone.head())
    """
    data_wind.plot()
    plt.savefig("plots2/wind.png")
    plt.show()
    plt.close()

    data_drone.plot()
    plt.savefig("plots2/drone.png")
    plt.show()
    plt.close()
    """
    data = combine_data(data_wind, data_drone)

    for col_name in ["pitch", "roll", "yaw", "h", "bat", "vgx", "vgy", "vgz", "agx", "agy", "agz", "wind speed", "baro"]:
        data[col_name] = data[col_name] / data[col_name].abs().max()
    
    data = data.drop(columns="bat")
    data = data.drop(columns="baro")
    data = data.drop(columns="vgx")
    data = data.drop(columns="vgy")
    data = data.drop(columns="vgz")
    data = data.drop(columns="agx")
    data = data.drop(columns="agy")
    data = data.drop(columns="agz")

    data = data[data["wind speed"] > 0]

    if config.flags.plot:
        data.to_csv("combined_data_normalized.csv")
        data.plot()
    
    if config.flags.save:
        plt.savefig("plots2/combined_normalized_selected_wind_not_0.png")
    
    plt.show()
    plt.close()
