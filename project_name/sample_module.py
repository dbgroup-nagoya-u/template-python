# coding=utf-8

"""
Sample module for template-python

テンプレート用のサンプルモジュールです．実際の利用時は書き換えるなり削除するなりしてください．
"""

import logging

from project_name import sample_module2

logger = logging.getLogger(__name__)


def sample_func() -> int:
    """Sample function for sample_module

    Returns:
        int: ``1``
    """
    logger.debug("sample function is called.")
    return sample_module2.sample_func()


class SampleClass:
    def __init__(self):
        """Sample class for sample_module
        """
        logger.debug("run constructor for SampleClass.")

    def sample_func(self) -> int:
        """Sample function for SampleClass

        Returns:
            int: ``1``
        """
        logger.debug("sample function in SampleClass is called.")
        return 1
