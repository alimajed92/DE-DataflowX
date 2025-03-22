import sys


class dataFlow_Exception(Exception):
    def __init__(self, error_message):
        self.error_message = error_message
        _, _, exc_tb = sys.exc_info()
        if exc_tb is not None:
            self.lineno = exc_tb.tb_lineno
            self.file_name = exc_tb.tb_frame.f_code.co_filename
        else:
            self.lineno = None
            self.file_name = None

    def __str__(self):
        return (
            f"Error occurred in script [{self.file_name}] "
            f"at line [{self.lineno}]: {self.error_message}"
        )
