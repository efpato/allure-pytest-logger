import logging

import allure

logger = logging.getLogger(__name__)


def test1():
    logger.debug("=== failed 1")

    with allure.step("Check"):
        assert False


def test2():
    logger.debug("=== failed 2")

    with allure.step("Check"):
        assert False
