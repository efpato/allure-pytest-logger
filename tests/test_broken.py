import logging

import allure

logger = logging.getLogger(__name__)


def test1():
    logger.debug("=== broken 1")

    with allure.step("Check"):
        raise ValueError("")


def test2():
    logger.debug("=== broken 2")

    with allure.step("Check"):
        raise KeyError("")
