# Turkish Sentiment Analysis with BERT

Bu proje, Türkçe ürün yorumlarını **Olumsuz (0), Olumlu (1), Nötr (2)** olarak sınıflandırmak için geliştirilmiş bir BERT tabanlı duygu analizi modelidir. Model, `dbmdz/bert-base-turkish-cased` üzerinde eğitilmiştir ve e-ticaret yorumları içeren bir veri setiyle optimize edilmiştir.

---

## 🚀 Özellikler
- Türkçe metinler için BERT tabanlı duygu analizi  
- Çok sınıflı sınıflandırma (NEG - POS - NEUTRAL)  
- Kolay eğitilebilir modüler yapı  
- Hazır tahmin (inference) betiği  
- GitHub ve Kaggle portföyü için uygun  

---

## 📁 Proje Klasör Yapısı

turkish-sentiment-analysis/
│
├── data/
│ └── e-ticaret_urun_yorumlari.csv # Ürün yorumları veri seti
│
├── model/ # Eğitilmiş model ağırlıkları
│
├── results/ # Training output (epoch kayıtları)
│
├── logs/ # Log dosyaları
│
├── train.py # Model eğitim dosyası
├── predict.py # Tahmin dosyası
├── utils.py # Dataset ve yardımcı fonksiyonlar
├── requirements.txt # Proje bağımlılıkları
└── README.md # Proje açıklaması

## 📦 Kurulum
pip install -r requirements.txt

## 🧠 Modeli Eğitme

Aşağıdaki komut doğrudan modeli eğitir:
python train.py

Eğitim tamamlandıktan sonra model şu dizine kaydedilir:
./model/model_Content

## 🔍 Tahmin Alma (Prediction)

Örnek kullanım:

```python
from predict import predict

text = "Ürün kalitesi beklediğimden çok daha iyiydi."
print(predict(text))

Çıktı örneği:
Olumlu

| Özellik              | Değer                         |
| -------------------- | ----------------------------- |
| Model                | dbmdz/bert-base-turkish-cased |
| Eğitim Epoch         | 2                             |
| Öğrenme Oranı        | 2e-5                          |
| Maks. Token Uzunluğu | 256                           |
| Veri Tipi            | Türkçe e-ticaret yorumları    |

| Metin                                         | Tahmin  |
| --------------------------------------------- | ------- |
| "Kargo çok yavaş geldi, ürün hasarlıydı."     | Olumsuz |
| "Tam göründüğü gibi, kaliteli ve kullanışlı." | Olumlu  |
| "Fena değil, idare eder."                     | Nötr    |


🤖 Kullanılan Teknolojiler

PyTorch

HuggingFace Transformers

BERT

Python 3.10+

Bu proje, Türkçe NLP alanında pratik bir örnek oluşturmak, portföy/proje dosyalarını güçlendirmek ve farklı veri setleriyle model geliştirmeyi öğretmek için tasarlanmıştır.