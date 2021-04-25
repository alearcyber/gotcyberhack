from textblob.classifiers import NaiveBayesClassifier
import sys


#  it's a set of 2-tuples
train = [

    ('latino', 'hispanic'),
    ('latina', 'hispanic'),
    ('latin', 'hispanic'),
    ('hispanic', 'hispanic'),

    ('jew', 'jew'),
    ('jewish', 'jew'),
    ('jewwish', 'jew'),
    ('ashkanazi jew', 'jew'),

    ('white', 'white'),
    ('caucasian', 'white'),
    ('caucasian', 'white'),
    ('american', 'white'),

    ('black', 'black'),
    ('black', 'black'),
    ('African', 'black'),
    ('AfricanAmerican', 'black'),

    ('indian', 'indian'),
    ('hindi', 'indian'),
    ('hindu', 'indian'),

    ('native', 'native american'),
    ('nativeAmerican', 'native american'),

    ('Korean', 'asian'),
    ('chinese', 'asian'),
    ('japanese', 'asian'),
    ('asian', 'asian'),

    ('latino', 'hispanic'),
    ('latina', 'hispanic'),
    ('latin', 'hispanic'),
    ('hispanic', 'hispanic'),

    ('jew', 'jew'),
    ('jewish', 'jew'),
    ('jewwish', 'jew'),
    ('ashkanazi jew', 'jew'),

    ('white', 'white'),
    ('caucasian', 'white'),
    ('caucasian', 'white'),
    ('american', 'white'),

    ('black', 'black'),
    ('black', 'black'),
    ('African', 'black'),
    ('AfricanAmerican', 'black'),

    ('indian', 'indian'),
    ('hindi', 'indian'),
    ('hindu', 'indian'),

    ('native', 'native american'),
    ('nativeAmerican', 'native american'),

    ('Korean', 'asian'),
    ('chinese', 'asian'),
    ('japanese', 'asian'),
    ('asian', 'asian'),

]




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
