import pickle
import tensorflow as tf
import numpy as np
from keras.preprocessing.sequence import pad_sequences

model = tf.keras.models.load_model('Model/sentiment_model.keras')

with open("Model/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

def clean_text(text):
    output = " ".join(text.split())
    return output

maxlen = 100

def predict_sentiment(sample: str):
    clean_sample = [clean_text(sample)]
    clean_sample_tokenised = tokenizer.texts_to_sequences(clean_sample)
    clean_sample_padded = pad_sequences(clean_sample_tokenised, padding='post', maxlen=maxlen)
    prediction = model.predict(clean_sample_padded)[0][0]*10

    prediction = float(prediction)
    return {"prediction": prediction}


