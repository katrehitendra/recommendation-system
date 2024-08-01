import pandas as pd

def preprocess_data(data):
    df = pd.DataFrame(data)
    df.drop('unixReviewTime', axis=1, inplace=True)
    df.rename(columns={'asin': 'product_id', 'overall': 'rating'}, inplace=True)
    df['tag'] = df.apply(lambda row: ', '.join(row.astype(str)), axis=1)
    return df['tag'].sample(1000)