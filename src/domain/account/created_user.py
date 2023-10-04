from pyspark.sql.functions import col, current_timestamp, input_file_name, year, month, dayofmonth

from src.domain.domain_contract import AccountContract
from src.domain.domains import Account


class CreatedUser(AccountContract):

    def __init__(self, df) -> None:
        super().__init__(df)

    def fill_by(self) -> None:

        self._df = self._df.filter(col('event_type') == Account.CREATED_USER.value)

        self._df = self._df.select(col('data.id'),
                                   col('data.new_status'),
                                   col('data.old_status'),
                                   col('data.reason'),
                                   col('domain'),
                                   col('event_type').alias('event'),
                                   col('event_id'),
                                   year(col('timestamp')).alias('year'),
                                   month(col('timestamp')).alias('month'),
                                   dayofmonth(col('timestamp')).alias('day'),
                                   col('timestamp').alias('timestamp_source'),
                                   input_file_name().alias('file_source'),
                                   current_timestamp().alias('datetime_load'))
