import sys
import nltk
import re
import joblib
nltk.download(['punkt', 'wordnet'])
import warnings
warnings.filterwarnings("ignore")
import pandas as pd

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
##from sklearn.externals import joblib
from sklearn.metrics import classification_report, accuracy_score
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC


from sqlalchemy import create_engine

database_filepath = 'data/DisasterResponse.db'

engine = create_engine('sqlite:///'+ database_filepath)
df = pd.read_sql_table('FigureEight', engine)

#df = pd.read_csv('data/figure_eight_data.csv')
X = df.message.values
Y = df[df.columns[4:]].values
category_names = list(df.columns[4:])

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

def tokenize(text):
    text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)
    return clean_tokens

pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(OneVsRestClassifier(LinearSVC(random_state = 0))))
    ])
parameters = {
                'tfidf__smooth_idf':[True, False],
                'clf__estimator__estimator__C': [1, 2, 5]
             }
model = GridSearchCV(pipeline, param_grid=parameters, scoring='precision_samples', cv = 5)

print("Now training the model.")
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)
print(classification_report(Y_test, Y_pred, target_names = category_names))
print('---------------------------------')
for i in range(Y_test.shape[1]):
    print('%25s accuracy : %.2f' %(category_names[i], accuracy_score(Y_test[:,i], Y_pred[:,i])))


print("Now Dumping Model.")
joblib.dump(model, "models/classifier_ea.pkl")