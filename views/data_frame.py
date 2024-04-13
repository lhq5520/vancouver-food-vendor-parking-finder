import pandas as pd


def display_list_of_dictionaries(list_of_dictionaries):
    df = pd.DataFrame(list_of_dictionaries)
    print(df)
