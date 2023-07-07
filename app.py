import numpy as np
from flask import Flask, jsonify
import pickle
import re
import emoji
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
import gensim.downloader as api

model = api.load('word2vec-google-news-300')
vocab = set(model.key_to_index.keys())

app = Flask(__name__)

with open('classifier-SVM.pkl', 'rb') as file:
    clf = pickle.load(file)

labels_mapping = {0: "fear", 1: "anger", 2: "joy", 3: "sadness"}


def preprocess_text(text):
    string = re.sub(r"@\w+", ' ', text)
    string = re.sub(r' #', ', ', string)
    string = emoji.demojize(string)
    string = simple_preprocess(string)
    return string


def create_features_text(text):
    text = preprocess_text(text)
    X = model.get_mean_vector([word for word in text if word in vocab])
    X = np.vstack(X)
    return X


X_input = create_features_text("Nice weather today loving it  ♥")
X_input = X_input.reshape(-1, 300)


@app.route('/')
def home():
    return labels_mapping[clf.predict(X_input).item()]


if __name__ == "__main__":
    app.run(debug=True)