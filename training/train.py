#
#
# Yunusemre Ozkose
# 19.11.21
#

import os
import sys
import numpy as np
import pandas as pd

from pathlib import Path
from sklearn.linear_model import LinearRegression


def df2numpy(df):
    x = df[["pitch", "roll", "yaw"]].to_numpy()
    y = df["wind speed"].to_numpy()

    return x, y


if __name__ == "__main__":
    sys.path.insert(1, str(Path(os.path.curdir).parent))
    from data_collecting.config import Config

    config = Config()

    data_df = pd.read_csv(config.paths.processed_data_save_path)
    print(data_df)

    data_x, data_y = df2numpy(data_df)

    reg = LinearRegression().fit(data_x, data_y)
    score = reg.score(data_x, data_y)
    print(score)
    print(reg.coef_)
    print(reg.intercept_)
