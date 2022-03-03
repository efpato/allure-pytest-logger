import logging

import pytest

logger = logging.getLogger(__name__)


@pytest.fixture(autouse=True)
def fix(request):
    logger.debug("==> setup")

    def fin():
        logger.debug("<== teardown")

    request.addfinalizer(fin)
