from consulting.strategy import EYStrategy, PVPStrategy
from consulting.config import STOCKS_LIST, FII_LIST


def main():
    # strategy = EYStrategy(STOCKS_LIST)
    strategy = PVPStrategy(FII_LIST)
    strategy.run()


if __name__ == "__main__":
    main()
