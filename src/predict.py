import torch
from transformers import BertForSequenceClassification, AutoTokenizer

MODEL_PATH = "/content/drive/MyDrive/AI_engineer_IBM/model_content/checkpoint-759"

label_map = {
    0: "Olumsuz",
    1: "Olumlu",
    2: "Nötr"
}

def predict(text):
    device = "cuda" if torch.cuda.is_available() else "cpu"

    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = BertForSequenceClassification.from_pretrained(MODEL_PATH)
    model = model.to(device)
    model.eval()

    inputs = tokenizer(
        text,
        return_tensors="pt",
        padding=True,
        truncation=True
    )
    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)
        pred = outputs.logits.argmax(dim=1).item()

    return label_map[pred]


if __name__ == "__main__":
    sample = "Ürün görsel ile hiç aynı değildi, berbat geldi."
    print("Metin:", sample)
    print("Tahmin:", predict(sample))
