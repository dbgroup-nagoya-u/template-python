# coding=utf-8

import logging
from typing import Final

import click

from . import sample_module

LOG_FORMAT: Final = "%(asctime)s [%(name)s:%(levelname)s] %(message)s                                      "





@click.command()
@click.option("--debug", is_flag=True, help="Output debug messages.")
def main(debug):
    # log設定
    logging.basicConfig(format=LOG_FORMAT)
    if debug:
        logging.getLogger().setLevel("DEBUG")
    logger = logging.getLogger(__name__)

    # 以下，メイン関数の処理
    logger.debug("debug message")
    logger.info("information message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")

    # log_levelがWARNINGのため下記関数を呼んだ際のログは出力されない
    sample_module.sample_func()

    # モジュール単位でlog_levelを下げることでログが出力されるようになる
    sample_module.logger.setLevel("DEBUG")
    sample_instance = sample_module.SampleClass()
    sample_instance.sample_func()


if __name__ == "__main__":
    main()
