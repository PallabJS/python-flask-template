import logging
import os


class AppLogger:
    def __init__(self, file_loc=f"{os.getcwd()}/log.log") -> None:
        self._log = logging
        self._log.basicConfig(format='%(asctime)s %(message)s',
                              datefmt='%m/%d/%Y %I:%M:%S %p',
                              level=logging.DEBUG,
                              filemode="a",
                              filename=file_loc)

    def info(self, msg):
        self._log.info(msg=msg)

    def debug(self, msg):
        self._log.debug(msg=msg)

    def exception(self, exception):
        self._log.exception(msg=exception)

    def error(self, msg):
        self._log.error(msg=msg)


log = AppLogger()
