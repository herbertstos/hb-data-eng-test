from pyspark import SparkConf
from pyspark.sql import SparkSession


class SparkCustomInstance:
    __session = None

    @property
    def session(self):
        return self.__session

    @session.setter
    def session(self, value):
        self.__session = value

    @staticmethod
    def instance(app_name=None, configs: list = None) -> SparkSession:
        if SparkCustomInstance.session.fdel:
            return SparkCustomInstance.session

        SparkCustomInstance.session = SparkCustomInstance._make_spark_session(app_name, configs)
        return SparkCustomInstance.session

    @staticmethod
    def _make_spark_session(app_name, configs):

        conf = SparkConf()

        if app_name:
            conf.setAppName(app_name)

        builder = SparkSession.builder

        if len(configs):
            for row in configs:
                conf.set(row[0], row[1])

        return builder.config(conf=conf).getOrCreate()
