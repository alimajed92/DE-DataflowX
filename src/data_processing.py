import pandas as pd
from logger.logger import dataFlow_logger
from exceptions.exceptions import dataFlow_Exception
from config import Config
import config as cfg


def process_csv_data(
    filepath: str = Config.DATA_FOLDER, file_name: str = "weather_data.csv"
) -> pd.DataFrame:

    df = pd.read_csv(filepath / file_name)
    return df


if __name__ == "main":

    pass
