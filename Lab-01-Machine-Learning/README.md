# Lab 01 – Sentiment Analysis Using Traditional Machine Learning

**Module:** PUSL 3205 – Large Language Models and Generative AI

## 1. Objective

The objective of this laboratory session is to develop practical knowledge of basic Natural Language Processing techniques and traditional machine learning approaches for sentiment classification.

## 2. Tools and Technologies

- Python
- Visual Studio Code
- Jupyter Notebook
- Pandas and NumPy
- Scikit-learn
- Matplotlib and Seaborn
- GitHub

## 3. Dataset

The UCI Sentiment Labelled Sentences dataset contains 3,000 labelled sentences collected from Amazon, IMDb and Yelp.

The dataset includes two sentiment classes:

- 0 – Negative
- 1 – Positive

Dataset source: https://archive.ics.uci.edu/dataset/331/sentiment%2Blabelled%2Bsentences

## 4. Tasks and Implementation

### 4.1 Dataset Loading

The three datasets were loaded using Pandas and combined into a single DataFrame.

### 4.2 Text Preprocessing

Text preprocessing involved converting sentences to lowercase, removing punctuation and unnecessary characters, removing extra whitespace and creating a clean-text column.

Repeated cleaned sentences were excluded before model training to reduce the risk of data leakage.

### 4.3 Exploratory Data Analysis

Positive and negative sentences were examined using sentiment distribution charts, word-frequency analysis and review-length visualizations.

### 4.4 Dataset Splitting

The dataset was divided into 80% training data and 20% testing data using stratified sampling and a random state of 42.

### 4.5 Feature Extraction

Bag of Words and TF-IDF were implemented to convert text into numerical features.

### 4.6 Model Training

Logistic Regression and Support Vector Machine models were trained using both feature extraction methods.

## 5. Results and Evaluation

The models were evaluated using accuracy, precision, recall and F1-score.

| Model | Accuracy | Precision | Recall | F1-score |
|---|---|---|---|---|
| BoW + Logistic Regression | TBD | TBD | TBD | TBD |
| BoW + SVM | TBD | TBD | TBD | TBD |
| TF-IDF + Logistic Regression | TBD | TBD | TBD | TBD |
| TF-IDF + SVM | TBD | TBD | TBD | TBD |

Highest-performing model on the test set: [Insert model name and actual F1-score]

## 6. Supporting Evidence

- [Jupyter Notebook](notebooks/lab01_sentiment.ipynb)
- [Sentiment Distribution](results/sentiment_distribution.png)
- [Frequent Words](results/frequent_words.png)
- [Positive Words](results/positive_words.png)
- [Negative Words](results/negative_words.png)
- [Logistic Regression Confusion Matrix](results/lr_confusion_matrix.png)
- [SVM Confusion Matrix](results/svm_confusion_matrix.png)
- [Model Comparison](results/model_comparison.png)
- [Evaluation Results](results/model_comparison.csv)
- [New Sentence Predictions](results/new_sentence_predictions.csv)

## 7. Observations and Reflection

Explain the actual differences observed between positive and negative reviews.

Compare the performance of Bag of Words and TF-IDF using the measured results.

Discuss incorrect predictions and any challenges encountered during implementation.

Traditional machine learning approaches have limitations when interpreting sarcasm, mixed sentiments, contextual meaning and neutral sentences.

## 8. Learning Outcomes

Through this laboratory session, I developed practical knowledge of:

- Loading and preparing labelled text datasets.
- Performing basic NLP preprocessing techniques.
- Exploring text data using visualizations.
- Creating Bag of Words and TF-IDF representations.
- Training Logistic Regression and SVM classifiers.
- Evaluating classification models using standard performance metrics.
- Predicting sentiment for previously unseen sentences.
- Identifying limitations through error analysis.

## 9. Conclusion

[Summarize the actual experimental findings and explain how the laboratory activity helped develop your understanding of NLP and machine learning.]