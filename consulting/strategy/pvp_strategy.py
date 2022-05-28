from consulting.fundamentus import get_fii


class PVPStrategy:
    def __init__(self, fii_list):
        self.fii_list = fii_list

    def get_fundamentus_data(self, fii_list):
        """Method to get dataframe from fundamentus"""
        dataframe = get_fii(fii_list)
        return dataframe

    def treat_dataframe(self, dataframe):
        """Method to treat dataframe"""
        dataframe["PVP"] = dataframe["PVP"].apply(
            lambda value: (int(value) / 100)
        )  # Divides each PVP by 100

        dataframe = dataframe.sort_values(
            by="PVP", ascending=True
        )  # Sort values by "PVP"

        return dataframe

    def run(self):
        data = self.get_fundamentus_data(self.fii_list)

        treated_data = self.treat_dataframe(data)

        print(treated_data[["PVP", "Div_Yield"]])
