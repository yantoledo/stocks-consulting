import fundamentus


class EYStrategy:
    def __init__(self, stocks_list):
        self.stocks_list = stocks_list

    def get_fundamentus_data(self, stocks_list):
        """Method to get dataframe from fundamentus"""
        dataframe = fundamentus.get_papel(stocks_list)
        return dataframe

    def treat_dataframe(self, dataframe):
        """Method to treat dataframe"""
        dataframe["PL"] = dataframe["PL"].apply(
            lambda value: (float(value) / 100)
        )  # Divides each PL by 100
        dataframe["EY (%)"] = dataframe["PL"].apply(
            lambda value: 100 / float(value)
        )  # Calculates Earning Yield Index for each stocks (100/PL)

        dataframe["ROIC"] = dataframe["ROIC"].replace(
            {"%": ""}, regex=True
        )  # Removes % from ROIC Data
        dataframe["ROIC"] = dataframe["ROIC"].replace(
            {"-": "0"}, regex=True
        )  # Set ROIC "-" as 0
        dataframe["ROIC (%)"] = dataframe["ROIC"].apply(
            lambda value: float(value)
        )  # Set ROIC data to float

        dataframe["EY + ROIC"] = (
            dataframe["EY (%)"] + dataframe["ROIC (%)"]
        )  # Sums EY and ROIC treated
        dataframe = dataframe.sort_values(
            by="EY + ROIC", ascending=False
        )  # Sort values by "EY + ROIC"

        return dataframe

    def run(self):
        data = self.get_fundamentus_data(self.stocks_list)
        treated_data = self.treat_dataframe(data)

        print(treated_data[["PL", "ROIC (%)", "EY (%)", "EY + ROIC"]])
