# mental-health-text-classification
NLP project to classify mental health status using BERT and SVM

## Problem Statement
This project aims to classify mental health conditions (Anxiety, Depression, Normal, Suicidal) from textual data using machine learning and deep learning techniques.

## Dataset Description
- Total samples: 992
- Features: text, status
- Classes: Anxiety, Depression, Normal, Suicidal
- Balanced dataset (248 samples per class)

## Work Completed
- Data collection and dataset selection
- Exploratory Data Analysis (EDA)
- Text preprocessing (cleaning, stopword removal)
- Initial insights and visualization

## Models Used
### 1. TF-IDF + SVM
A traditional machine learning approach was implemented using TF-IDF vectorization combined with a Support Vector Machine (SVM) classifier.
- TF-IDF converts text into numerical feature vectors
- SVM (linear kernel) is used for classification
- N-grams (unigrams + bigrams) were used to capture local patterns

**Performance:**
- Accuracy: ~61%
- Performs well on structured and simple text patterns
- Struggles with contextual understanding and overlapping emotions


### 2. BERT (Bidirectional Encoder Representations from Transformers)
A deep learning approach using a pre-trained BERT model (`bert-base-uncased`) was fine-tuned for this classification task.
- Captures contextual meaning of words
- Handles complex sentence structures
- Uses transformer-based architecture

**Performance:**
- Accuracy: ~75%
- Strong performance across most classes
- Better at understanding emotional context


## Model Comparison
| Model            | Accuracy | Strengths                          | Weaknesses                          |
|------------------|----------|-----------------------------------|-------------------------------------|
| SVM (TF-IDF)     | ~61%     | Fast, lightweight                 | Poor context understanding          |
| BERT             | ~75%     | High accuracy, understands context| Computationally expensive           |

### Key Insights
- BERT significantly outperforms SVM in accuracy and contextual understanding  
- SVM is faster and suitable for simpler or low-resource environments  
- BERT is better suited for real-world applications involving complex text  

Overall, BERT is chosen as the **preferred model** due to its superior performance.

## Live Demo
The application is deployed using Streamlit and can be accessed here:

https://mental-health-text-classification-bmeuwmuhnkgnyeqxmvonwc.streamlit.app/
Users can enter text and get real-time mental health predictions using the trained TF-IDF + SVM model.

