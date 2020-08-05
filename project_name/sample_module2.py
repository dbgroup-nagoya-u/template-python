# coding=utf-8

"""
Sample module for template-python

テンプレート用のサンプルモジュールです．実際の利用時は書き換えるなり削除するなりしてください．
"""

import logging

logger = logging.getLogger(__name__)


def sample_func() -> int:
    """Sample function for sample_module2

    Returns:
        int: ``1``
    """
    logger.debug("sample function is called.")
    return 1
