from loguru import logger

from .Application import FC_Application as __FC_without_remote_layer__
from .Remote import FC_Client, FC_Server


class FC_Controller(__FC_without_remote_layer__):
    """
    本地飞控
    """

    pass  # 只是个别名


__all__ = ["FC_Controller", "FC_Client", "FC_Server", "logger"]

logger.add("fc_log/{time}.log", retention=10, level="DEBUG", backtrace=True, diagnose=True)
