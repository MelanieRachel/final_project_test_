

import pandas as pd

def bin_age(df, column_name, bin_edges, bin_labels):
    """
    Bin a specified column in a DataFrame into discrete intervals.

    Parameters:
    - df: The DataFrame containing the data.
    - column_name: The name of the column to bin.
    - bin_edges: A list specifying the bin edges (boundaries).
    - bin_labels: A list specifying the labels for each bin.

    Returns:
    - df: The DataFrame with the binned column added as a new column.
    """

    # Use pd.cut to bin the specified column
    df['Binned_' + column_name] = pd.cut(df[column_name], bins=bin_edges, labels=bin_labels, include_lowest=True)

    return df

# Example usage
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 18, 22, 35]}
df = pd.DataFrame(data)

# Define bin edges and labels
age_bins = [0, 18, 30, 100]
age_labels = ['Under 18', '18-30', 'Over 30']

# Call the bin_age function to create a new binned column 'Binned_Age'
df = bin_age(df, 'Age', age_bins, age_labels)

# Display the DataFrame with the binned column
print(df)