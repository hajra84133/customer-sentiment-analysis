import pandas as pd

data = pd.read_csv("olist_order_reviews_dataset.csv")

# Keep only useful columns
data = data[['review_comment_message', 'review_score']]

# Remove missing values
data = data.dropna()
data = data[data['review_comment_message'].str.len() > 3]

# Save clean dataset
data.to_csv("clean_reviews.csv", index=False)

print("Dataset exported successfully!")