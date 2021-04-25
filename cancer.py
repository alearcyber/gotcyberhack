from textblob.classifiers import NaiveBayesClassifier
import sys
import random

dict = {
    1: 'breast',
    2: 'colon',
    3: 'cervical',
    4: 'lung',
    5: 'kidney',
    6: 'melanoma',
}


#  it's a set of 2-tuples
train = [
    ('breast', 'breast'),
    ('colon', 'colon'),
    ('cervical', 'cervical'),
    ('lung', 'lung'),
    ('kidney', 'kidney'),
    ('melanoma', 'melanoma'),
    ('they had melanoma' , 'melanoma'),
    ('he was diagnosed with kidney cancer', dict[5]),
    ('he had breast cancer', dict[1]),
    ('im pretty sure it was colon cancer', dict[2]),
    ('she got lung cancer at the age of 53', dict[4]),
    ('he had colon cancer', dict[2]),
    ('he had cervical cancer', dict[3]),
    ('he had lung cancer', dict[4]),
    ('he had kidney cancer', dict[5]),

]

test = [
    ("colon cancer at the age of 50", 'colon')
]


def classify_input():
    input = ""

    for word in sys.argv[1:]:
        input += word + " "


    input = input.strip()
    out = ''

    #print(input)

    cl = NaiveBayesClassifier(train)
    out = cl.classify(input)
    return out



cl = NaiveBayesClassifier(train)

print(cl.classify("she had colon cancer at 65"))

cl.show_informative_features()
print(cl.informative_features())

from sklearn.metrics import confusion_matrix

pred = []
actual = []

test = [
    "colon cancer at the age of 50",
    "she had colon cancer at 65",
    'my granda had melanoma',
    'my grandma had cervical cancer',
    'my grandma had breast cancer',
    'they had lung cancer',
    'kidney',
    'what cancer is this',
    "colon cancer at the age of 50",
    "she had colon cancer at 65",
    'my granda had melanoma',
    'my grandma had cervical cancer',
    'my grandma had breast cancer',
    'they had lung cancer',
    'kidney',
    'what cancer is this',
    "colon cancer at the age of 50",
    "she had colon cancer at 65",
    'my granda had melanoma',
    'my grandma had cervical cancer',
    'my grandma had breast cancer',
    'they had lung cancer',
    'kidney',
    'kidney',
    'lung',
    'liver',
    'streamline',
    'melanoma',
    'colon'
]

testx = ['colon',
         'colon',
         'melanoma',
         'cervical',
         'breast',
         'lung',
         'kidney',
         'lung',
         'colon',
         'colon',
         'melanoma',
         'cervical',
         'breast',
         'lung',
         'kidney',
         'cervical',
         'colon',
         'colon'
]

pred = []

for i in range(40):
    num = random.randint(1,6)
    testx.append(dict[num])

    num = random.randint(1,6)
    test.append(dict[num])


for word in test:
    pred.append(cl.classify(word))


import pandas as pd
y_actu = pd.Series(testx, name='Actual')
y_pred = pd.Series(pred, name='Predicted')
df_confusion = pd.crosstab(y_actu, y_pred)



import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn


def plot_confusion_matrix(df_confusion, title='Confusion matrix', cmap=plt.cm.gray_r):
    plt.matshow(df_confusion, cmap=cmap) #imshow
    #plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(df_confusion.columns))
    plt.xticks(tick_marks, df_confusion.columns, rotation=45)
    plt.yticks(tick_marks, df_confusion.index)
    #plt.tight_layout()
    plt.ylabel(df_confusion.index.name)
    plt.xlabel(df_confusion.columns.name)
    sn.heatmap(df_confusion, annot=True)
    plt.show()

plot_confusion_matrix(df_confusion)


