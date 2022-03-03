import logging

import allure

logger = logging.getLogger(__name__)


def test1():
    logger.debug("=== passed 1")

    with allure.step("Check"):
        assert True


def test2():
    logger.debug("=== passed 2")

    with allure.step("Check"):
        assert True
