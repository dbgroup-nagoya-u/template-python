# coding=utf-8

import logging
from typing import Final

import sample_module

if __name__ == "__main__":
    # log設定
    LOG_FORMAT: Final = "%(asctime)s [%(name)s:%(levelname)s] %(message)s"
    logging.basicConfig(format=LOG_FORMAT)
    logger = logging.getLogger(__name__)

    # 以下，メイン関数の処理
    logger.debug("debug message")
    logger.info("information message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")

    # log_levelがWARNINGのため下記関数を読んだ際のログは出力されない
    sample_module.sample_func()

    # モジュール単位でlog_levelを下げることでログが出力されるようになる
    sample_module.logger.setLevel("DEBUG")
    sample_instance = sample_module.SampleClass()
    sample_instance.sample_func()
