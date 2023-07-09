import numpy as np
from flask import Flask, render_template, request, url_for
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



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    text = request.form['expression']
    
    # Display the entered text
    #return render_template('display_text.html', text=text)

    #text = request.form.values()
    X_input = create_features_text(text)
    X_input = X_input.reshape(-1, 300)
    label = labels_mapping[clf.predict(X_input).item()]
    # return text
    #return "respose: {0}".format(text)
    return render_template('index.html', label=label)



if __name__ == "__main__":
    app.run(debug=True)