import enum
import logging
import pathlib


class Constants(enum.Enum):
    INPUT_PATH_LAKE = 1
    INPUT_TYPE_MAPPING = 2
    OUTPUT_PATH_LAKE = 3
    OUTPUT_PATH_LOG = 4


class Settings:
    CONFIGS = [['spark.driver.extraJavaOptions', '-Duser.timezone=GMT'],
               ['spark.executor.extraJavaOptions', '-Duser.timezone=GMT'],
               ["spark.sql.session.timeZone", "UTC"]]

    LOGGER_LEVEL = logging.DEBUG

    __BASE_PATH = pathlib.Path().resolve().parent.__str__()

    input_paths = {
        Constants.INPUT_PATH_LAKE: f"{__BASE_PATH}/data/input/lake/",
    }

    output_paths = {
        Constants.OUTPUT_PATH_LAKE: f"{__BASE_PATH}/data/output/lake",
        Constants.OUTPUT_PATH_LOG: f"{__BASE_PATH}/data/output/logs"
    }
