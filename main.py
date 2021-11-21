from consulting.strategy import EYStrategy
from consulting.config import STOCKS_LIST


def main():
    strategy = EYStrategy(STOCKS_LIST)
    strategy.run()


if __name__ == "__main__":
    main()
