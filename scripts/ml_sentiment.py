import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load data
data = pd.read_csv("olist_order_reviews_dataset.csv")

# Keep needed columns
data = data[['review_comment_message', 'review_score']]
data = data.dropna()
data = data[data['review_comment_message'].str.len() > 3]

# Create sentiment labels
def label(score):
    return 'Positive' if score >= 4 else 'Negative'

data['sentiment'] = data['review_score'].apply(label)

# Features and labels
X = data['review_comment_message']
y = data['sentiment']

# Vectorization (better features)
vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2))
X = vectorizer.fit_transform(X)

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
print("Accuracy:", model.score(X_test, y_test))

# Visualization
data['sentiment'].value_counts().plot(kind='bar')
plt.title("Customer Sentiment Distribution")
plt.show()