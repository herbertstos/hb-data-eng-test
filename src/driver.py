from src.domain.account.created_user import CreatedUser
from src.domain.account.status_change import StatusChange
from src.domain.domains import Account
from src.helper.custom_logger import Logger
from src.helper.custom_session_spark import SparkCustomInstance
from src.settings import Settings, Constants


class Driver:

    def __init__(self) -> None:
        self.logger = Logger.get_logger(log_level=Settings.LOGGER_LEVEL,
                                        path_str=Settings.output_paths.get(Constants.OUTPUT_PATH_LOG))
        self.spark = SparkCustomInstance.instance(configs=Settings.CONFIGS)

    def run(self):
        df = self.spark.read.json(Settings.input_paths.get(Constants.INPUT_PATH_LAKE))

        domains_event = df.select('domain', 'event_type').distinct().toPandas().T.to_dict('list')

        for index, _list in domains_event.items():
            domain = _list[0]
            event = _list[1]
            self.logger.warning(f'started processing for domain: {domain} and event: {event} ')
            if domain == Account.__name__.lower():
                if event == Account.STATUS_CHANGE.value:
                    StatusChange(df).run()
                elif event == Account.CREATED_USER.value:
                    CreatedUser(df).run()
                else:
                    self.logger.warning(f'the feature for ingesting the event: {event} has not been implemented yet')
            else:
                self.logger.warning(f'the feature for ingesting the domain: {domain} has not been implemented yet')


if __name__ == '__main__':
    Driver().run()
