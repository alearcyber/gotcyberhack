from textblob.classifiers import NaiveBayesClassifier
import sys




# vhl, rad50, brca1, brca2, atm

#  it's a set of 2-tuples
train = [
    ('brca1', 'brca1'),
    ('rad50', 'rad50'),
    ('vh1', 'vh1'),
    ('brca2', 'brca2'),
    ('atm', 'atm'),

    ('brca1', 'brca1'),
    ('rad50', 'rad50'),
    ('vh1', 'vh1'),
    ('brca2', 'brca2'),
    ('atm', 'atm')

]
test = [
    ('i have a change in brca2', 'brca2'),
    ('a mutation in rad50', 'rad50')
]



def classify():
    cl = NaiveBayesClassifier(train)
    print("Accuracy: {0}".format(cl.accuracy(test)))
    cl.show_informative_features(7)
    print(cl.informative_features())


def classify_input():
    input = ""


    for word in sys.argv[1:]:
        input += word + " "

    input = input.strip()
    out = ''

    print(input)

    cl = NaiveBayesClassifier(train)
    out = cl.classify(input)
    return out



print(classify_input())
