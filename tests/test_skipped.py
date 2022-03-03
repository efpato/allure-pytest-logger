import logging

import allure
import pytest

logger = logging.getLogger(__name__)


@pytest.mark.skip
def test1():
    logger.debug("=== skipped 1")

    with allure.step("Check"):
        assert False


@pytest.mark.skip
def test2():
    logger.debug("=== skipped 2")

    with allure.step("Check"):
        assert False
