from abc import ABC, abstractmethod

from pyspark.sql import DataFrame, Window
from pyspark.sql.functions import desc, row_number, col

from src.settings import Settings, Constants


def _remove_duplicates(df):
    partition = Window.partitionBy("id").orderBy(desc("timestamp_source"))
    _df = df.withColumn("row_n", row_number().over(partition)).filter(col('row_n') == 1).drop('row_n')
    return df


class AccountContract(ABC):

    def __init__(self, df) -> None:
        self._df = df

    @abstractmethod
    def fill_by(self) -> DataFrame:
        ...

    def __write(self):
        _de_dup = _remove_duplicates(self._df)
        _de_dup.repartition(1).write.mode('append').partitionBy('year', 'month', 'day', 'domain', 'event').parquet(
            Settings.output_paths.get(Constants.OUTPUT_PATH_LAKE))

    def run(self):
        self.fill_by()
        self.__write()
