# Customer Sentiment Analysis using AI & NLP

## Project Overview
This project analyzes customer feedback using Natural Language Processing (NLP) and Machine Learning to identify sentiment patterns in customer reviews. The goal is to transform unstructured text data into meaningful insights that can support data-driven decision-making and improve customer experience.

The project demonstrates the complete data analytics workflow including data preprocessing, sentiment classification, model training, and result evaluation.

---

## Objectives
- Analyze customer reviews to understand sentiment trends.
- Apply NLP techniques to convert text data into machine-readable format.
- Train a machine learning model to classify customer sentiment.
- Generate insights that could help organizations improve services and customer satisfaction.

---

## Dataset
The dataset used in this project contains customer review data including:
- Review text
- Review scores
- Review timestamps

The data was cleaned to remove missing values and irrelevant entries before analysis.

---

## Technologies Used
- Python
- Pandas
- NumPy
- NLTK (Natural Language Processing)
- Scikit-learn
- Matplotlib
- Git & GitHub

---

## Methodology

### 1. Data Preprocessing
- Loaded the dataset using Pandas
- Removed missing review comments
- Cleaned and prepared text data for analysis

### 2. Sentiment Labeling
Customer sentiment was categorized into:
- Positive
- Negative

Labels were derived using review scores.

### 3. Feature Engineering
Text data was transformed into numerical features using:

- **TF-IDF Vectorization**

This allowed machine learning models to process textual data.

### 4. Model Training
A machine learning classification model was trained to predict sentiment based on customer review text.

Model used:
- Logistic Regression

### 5. Model Evaluation
The model was evaluated using:
- Accuracy
- Precision
- Recall
- F1 Score

Model achieved approximately **93% accuracy** on the test dataset.

---

## Project Structure

```
CustomerSentiment
│
├── data
│   ├── clean_reviews.csv
│
├── scripts
│   ├── export_data.py
│   ├── ml_sentiment.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Example Output

Example sentiment prediction:

```
Input: "Great service and fast delivery"
Predicted Sentiment: Positive
```

---

## Key Insights
- Majority of customer feedback shows positive sentiment.
- Negative reviews provide valuable signals for service improvement.
- Sentiment analysis can help organizations identify customer satisfaction trends at scale.

---

## Future Improvements
- Apply advanced NLP models (BERT / Transformers)
- Perform topic modeling on negative reviews
- Deploy model as an API or web application
- Build an interactive analytics dashboard

---

## Author
**Hajra**  
BS Computer & Information Science – PIEAS  

Interested in **AI, Data Analytics, and Machine Learning applications for real-world business problems.**
