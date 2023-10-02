"""
Script adaptado de:
https://github.com/FilipeWilliam/TCC/blob/master/nn/train_question_classifiers.py
"""

from transformers import BertTokenizer, BertForSequenceClassification
from django.conf import settings

def classify_question(question) -> str:

    # Carregar o modelo treinado a partir do diretório onde você o salvou
    model = BertForSequenceClassification.from_pretrained(settings.MODEL_DIR)

    # Carregar o tokenizador correspondente
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

    # Pergunta que você deseja classificar
    input_text = question

    # Tokenizar a pergunta
    tokens = tokenizer(input_text, truncation=True, padding=True, return_tensors="pt")

    # Realizar a classificação
    predictions = model(**tokens) # type: ignore
    predicted_label = predictions.logits.argmax().item()

    # Mapear o rótulo de volta para a categoria de dificuldade
    categories = ["fácil", "médio", "difícil"]
    predicted_category = categories[predicted_label]

    return predicted_category