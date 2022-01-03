#
#
# Yunusemre Ozkose
# 19.11.21

import os
from coqpit import Coqpit
from dataclasses import dataclass


@dataclass
class Config(Coqpit):

    paths = Coqpit()
    paths.data_folder = "/home/emre/workspace/master/cmp713/project/Drone-Wind-Prediction/data/1"
    paths.drone_data_folder = os.path.join(paths.data_folder, "drone")
    paths.wind_data_xls_path = os.path.join(paths.data_folder, "anemometer", "UT363BT_20211023143144_1634988704266_formatted.xls")

    paths.data_folder2 = "/home/emre/workspace/master/cmp713/project/Drone-Wind-Prediction/data/2"
    paths.drone_data_folder2 = os.path.join(paths.data_folder2, "drone")
    paths.wind_data_xls_path2 = os.path.join(paths.data_folder2, "anemometer", "UT363BT_20211114154150_1636893710903.xls")

    paths.save_folder = "/home/emre/workspace/master/cmp713/project/Drone-Wind-Prediction/data/processed"

    paths.experiments_path = "training/exp"
    paths.processed_data_save_path = os.path.join(paths.data_folder, "processed/combined_data_normalized.csv")
    paths.figure_folder = os.path.join(paths.experiments_path, "figures")

    flags = Coqpit()
    flags.plot = False
    flags.save = False
