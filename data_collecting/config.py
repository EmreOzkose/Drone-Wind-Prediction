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
    paths.data_folder = "../data"
    paths.drone_data_folder = os.path.join(paths.data_folder, "drone")
    paths.wind_data_xls_path = os.path.join(paths.data_folder, "anemometer", "UT363BT_20211023143144_1634988704266_formatted.xls")
    paths.figure_folder = "plots"

    flags = Coqpit()
    flags.plot = True
    flags.save = True


class Config2(Config):
    paths = Coqpit()
    paths.data_folder = "../data_2"
    paths.drone_data_folder = os.path.join(paths.data_folder, "drone")
    paths.wind_data_xls_path = os.path.join(paths.data_folder, "anemometer", "UT363BT_20211114154150_1636893710903.xls")
