# Description
This example demonstrates how to handle exceptions in multiprocessing with logging and custom exception handling using the `WrapException` class.

# Code
```
import logging
from multiprocessing import Pool, current_process

logger = logging.getLogger(__name__)

class WrapException(Exception):
    """Exception wrapper for multiprocessing"""
    def __init__(self):
        exc_type, exc_value, exc_tb = sys.exc_info()
        self.exception = exc_value
        self.formatted = ''.join(traceback.format_exception(exc_type, exc_value, exc_tb))

    def __str__(self):

Usage:

import logging
from multiprocessing import Pool, current_process
from indra.util.multiprocessing_traceback import WrapException

logger = logging.getLogger(__name__)


def f_child():
    try:
        # Your code that errors here
        1/0
    except Exception:
        raise WrapException()


def print_err(err):
    logger.error(f'An error occurred in process {current_process().pid}')
    logger.exception(err)


def success_callback(res):
    logger.info(f'A result was received {res}')
    results.append(res)


def main_func():
    with Pool(2) as pool:
        pool.apply_async(func=f_child, callback=success_callback,
                         error_callback=print_err)
        pool.close()
        pool.join()


if __name__ == '__main__':
    results = []

```
