# csv_saver.py
def save_to_csv(df, filepath):
    df.to_csv(filepath, index=False)
