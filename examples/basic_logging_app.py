import logging


def mother():
    logging.error("mother")
    daughter()
    son()


def daughter():
    logging.error("daughter")


def son():
    logging.error("son")


if __name__ == "__main__":
    mother()
