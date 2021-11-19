#
#
# Yunusemre Ozkose
# 19.11.21
#

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


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
    x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size=0.1, random_state=1234)

    # Train
    reg = LinearRegression().fit(x_train, y_train)
    score = reg.score(x_train, y_train)
    print(score)
    print(reg.coef_)
    print(reg.intercept_)

    # Test
    y_pred = reg.predict(x_test)
    print(y_test)
    print(y_pred)
    print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))

    print(x_test.shape, y_test.shape)

    # Plot outputs
    id = 8
    plt.scatter(x_test[id, 0], y_test[id],  color="black")
    plt.plot(x_test[id, 0], y_pred[id], 'o' , color="blue")
    plt.show()
