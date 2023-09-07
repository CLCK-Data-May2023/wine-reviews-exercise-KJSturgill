import pandas as pd
import zipfile36

reviews = pd.read_csv('C:/Users/bisho/Desktop/CKY DA/tues-data-analysis/wine-reviews-exercise-KJSturgill/data/winemag-data-130k-v2.csv.zip', compression='zip')

wine_by_countries = reviews.groupby('country').agg({'country':'count', 'points': 'mean'}).round(1)

new_reviews = wine_by_countries.rename(columns={'country':'count'}).reset_index()

new_reviews.to_csv('C:/Users/bisho/Desktop/CKY DA/tues-data-analysis/wine-reviews-exercise-KJSturgill/data/reviews-per-country.csv', index=False)