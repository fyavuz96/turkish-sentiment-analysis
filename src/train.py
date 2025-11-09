import torch
from transformers import BertForSequenceClassification, AutoTokenizer, Trainer, TrainingArguments
from utils import ReviewDataset, load_dataset

DATA_PATH = "data/e-ticaret_urun_yorumlari.csv"

def main():
    texts, labels = load_dataset(DATA_PATH, delimiter=";")

    tokenizer = AutoTokenizer.from_pretrained("dbmdz/bert-base-turkish-cased")

    dataset = ReviewDataset(texts, labels, tokenizer)

    model = BertForSequenceClassification.from_pretrained(
        "dbmdz/bert-base-turkish-cased",
        num_labels=3
    )

    training_args = TrainingArguments(
        output_dir="./results",
        evaluation_strategy="no",
        learning_rate=2e-5,
        per_device_train_batch_size=8,
        num_train_epochs=2,
        weight_decay=0.01,
        save_strategy="epoch",
        logging_dir="./logs",
        report_to="none"
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        tokenizer=tokenizer
    )

    trainer.train()
    model.save_pretrained("./model_content")
    tokenizer.save_pretrained("./model_content")

    print("✅ Model eğitimi tamamlandı ve ./model klasörüne kaydedildi.")

if __name__ == "__main__":
    main()
