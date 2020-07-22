# coding=utf-8

"""
Sample module for template-python

テンプレート用のサンプルモジュールです．実際の利用時は書き換えるなり削除するなりしてください．
"""

import logging

logger = logging.getLogger(__name__)


def sample_func() -> int:
    """Sample function for sample_module

    Args:
        None

    Returns:
        常に``1``を返す．
    """
    logger.debug("sample function is called.")
    return 1


class SampleClass:
    """Sample class for sample_module

    Args:
        None
    """

    def __init__(self):
        logger.debug("run constructor for SampleClass.")

    def sample_func(self) -> int:
        """Sample function for SampleClass

        Args:
            None

        Returns:
            常に``1``を返す．
        """
        logger.debug("sample function in SampleClass is called.")
        return 1
