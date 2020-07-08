import logging
import dependency


def mother():
    logging.error("mother")
    daughter("cyber")
    # raise ValueError
    son()


def daughter(a, b="he"):
    a = 0
    for i in range(10):
        a += i
        logging.error("daughter")

    dependency.dependency()


def son():
    logging.error("son")


if __name__ == "__main__":
    mother()
