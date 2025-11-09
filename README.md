# Turkish Sentiment Analysis

This project is a BERT-based sentiment analysis model developed to classify Turkish product reviews as Negative (0), Positive (1), or Neutral (2). The model is built on top of **dbmdz/bert-base-turkish-cased** and optimized using a dataset containing e-commerce reviews.

## 🚀 Features

* BERT-based sentiment analysis for Turkish text
* Multi-class classification (NEG, POS, NEUTRAL)
* Modular and easy-to-train structure
* Ready-to-use inference script
* Suitable for GitHub and Kaggle portfolio projects

## 📁 Project Structure

```
turkish-sentiment-analysis/
│
├── data/
│   └── e-ticaret_urun_yorumlari.csv     # Product review dataset
│
├── model/                               # Saved model weights
├── results/                             # Training outputs (epoch logs)
├── logs/                                # Log files
│
├── train.py                             # Training script
├── predict.py                           # Inference script
├── utils.py                             # Dataset and helper functions
│
├── requirements.txt                      # Project dependencies
└── README.md                             # Project description
```

## 📦 Installation

```
pip install -r requirements.txt
```

## 🧠 Training the Model

Run the following command to start training:

```
python train.py
```

After training, the model will be saved here:

```
./model/model_Content
```

## 🔍 Making Predictions

Example usage:

```python
from predict import predict

text = "Ürün kalitesi beklediğimden çok daha iyiydi."
print(predict(text))
```

Sample output:

```
Positive
```

## 📊 Model Information

| Feature          | Value                         |
| ---------------- | ----------------------------- |
| Model            | dbmdz/bert-base-turkish-cased |
| Training Epochs  | 2                             |
| Learning Rate    | 2e-5                          |
| Max Token Length | 256                           |
| Data Type        | Turkish e-commerce reviews    |

| Text                                          | Prediction |
| --------------------------------------------- | ---------- |
| "Kargo çok yavaş geldi, ürün hasarlıydı."     | Negative   |
| "Tam göründüğü gibi, kaliteli ve kullanışlı." | Positive   |
| "Fena değil, idare eder."                     | Neutral    |

## 🤖 Technologies Used

* PyTorch
* HuggingFace Transformers
* BERT
* Python 3.10+

This project is designed as a practical example in the field of Turkish NLP, to strengthen portfolio/project showcases and demonstrate how to develop sentiment models with different datasets.
