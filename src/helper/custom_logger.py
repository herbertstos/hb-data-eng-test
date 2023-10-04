import logging
import os
import pathlib
from datetime import datetime


class Logger:

    @staticmethod
    def get_logger(log_level=logging.DEBUG, path_str=None) -> logging:
        file = f'exec_log_{datetime.now()}.log'
        path = path_str if path_str else f''

        if not os.path.isdir(path) and path != '':
            os.mkdir(path)

        logger = logging.getLogger(Logger.__name__)
        logger.setLevel(log_level)

        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(f'{path}/{file}')

        formatter = '%(asctime)s.%(msecs)03d %(levelname)s::: %(message)s'

        console_handler.setFormatter(logging.Formatter(formatter))
        file_handler.setFormatter(logging.Formatter(formatter))

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        return logger
