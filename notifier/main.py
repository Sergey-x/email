from log import get_logger
from queue_service import queue_handler


logger = get_logger(__name__)


def main():
    queue_handler()


if __name__ == '__main__':
    logger.info("Email service start up!")
    main()
