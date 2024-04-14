import pandas as pd


def display_list_of_dictionaries(list_of_dictionaries):
    df = pd.DataFrame(list_of_dictionaries)
    print(df)


def get_unique_values_from_column(data_frame, column_name):
    """
    Removes duplicate rows based on a specified column and returns a list of unique values from that column.

    Args:
    data_frame (pd.DataFrame): The DataFrame to process.
    column_name (str): The name of the column to check for unique values.

    Returns:
    list: A list containing unique values from the specified column.
    """
    if column_name in data_frame.columns:
        drop_duplicate_column = data_frame.drop_duplicates(subset=[column_name])
        unique_values_list = drop_duplicate_column[column_name].tolist()
        return unique_values_list
    else:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")