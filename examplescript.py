def currencyfill(df):
    # Fill missing values in 'Currency Unit' column with "Dollar"
    df['Currency Unit'] = df['Currency Unit'].fillna("Dollar")
    return df
