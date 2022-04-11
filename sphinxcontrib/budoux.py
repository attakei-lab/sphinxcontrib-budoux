from sphinx.application import Sphinx
from sphinx.util import logging

logger = logging.getLogger(__name__)


def setup(app: Sphinx):
    """
    Setup function for this extension.
    """
    logger.debug(f"Using {__name__}")
