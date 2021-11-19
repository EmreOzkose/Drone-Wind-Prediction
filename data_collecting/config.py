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
    paths.data_folder = "data"
    paths.drone_data_folder = os.path.join(paths.data_folder, "drone")
    paths.wind_data_xls_path = os.path.join(paths.data_folder, "anemometer", "UT363BT_20211114154150_1636893710903.xls")
    
    paths.experiments_path = "training/exp"
    paths.processed_data_save_path = os.path.join(paths.data_folder, "processed/combined_data_normalized.csv")
    paths.figure_folder = os.path.join(paths.experiments_path, "figures")

    flags = Coqpit()
    flags.plot = True
    flags.save = True
