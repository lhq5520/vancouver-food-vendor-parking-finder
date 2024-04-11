import pandas as pd


def display_all_carparking_table(list_of_dictionaries):
    df = pd.DataFrame(list_of_dictionaries)
    print(df)
