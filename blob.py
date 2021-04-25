from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import keyboard
import time
import random

# dictionary relating the number to the appropriate ethnicity token
number_tags = {
    '1': 'black',
    '2': 'white',
    '3': 'jew',
    '4': 'hispanic',
    '5': 'native american',
    '6': 'asian',
    '7': 'indian',
    '0': 'none'
}


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
test = [
    ('I\'m black', 'black'),
    ('caucasian', 'white'),
    ('black', 'black'),
    ('I am jewish', 'jew')

]

#cl = NaiveBayesClassifier(train)

"""
# Classify some text
print(cl.classify("Their burgers are amazing."))  # "pos"
print(cl.classify("I don't like their pizza."))   # "neg"

# Classify a TextBlob
blob = TextBlob("The beer was amazing. But the hangover was horrible. " "My boss was not pleased.", classifier=cl)

print(blob)
print(blob.classify())

for sentence in blob.sentences:
    print(sentence)
    print(sentence.classify())
    
"""

# Compute accuracy
#print("Accuracy: {0}".format(cl.accuracy(test)))
# print(cl.classify("latino"))

# Show 7 most informative features
#cl.show_informative_features(7)


def get_ethnicity_dataset():
    # set where we store all the ethnicity inputs from the table
    set_of_raw_inputs = set()

    # setup column names
    f = open("/Users/aidanlear/PycharmProjects/voice/data.txt", encoding="utf16", errors='ignore')
    first_line = f.readline()
    columns = first_line.strip().split()  # array of the column names in correct order
    index_of_ethnicity = columns.index("ETHNICITY")  # int where the column ethnicity is from zero

    for line in f:
        line_as_array = line.strip().split()  # the line as an array split on spaces
        ethnicity_raw = line_as_array[index_of_ethnicity]
        set_of_raw_inputs.add(ethnicity_raw)

    return set_of_raw_inputs


"""
this function will assign the category to the raw input

steps:
grab an instance of raw input,
ask for what category
    throwout raw input that can't be categorized
    make it so I can just press 1,2,3,4.. etc and those correspond to categories
send to a dictionary where keys are the raw input and values are categories
right to a file each line is an input, space seperates raw and category, raw comes first


ethnicity tags

1 black
2 white
3 jew
4 hispanic
5 native american
6 asian
7 indian
0 none

"""
def make_training_model():
    # grab instance of raw input
    raw_input_set = get_ethnicity_dataset()

    # write the tags to a file
    ethnicity_file = open("/Users/aidanlear/PycharmProjects/voice/ethnicity.txt", 'a')  # open the file in append mode
    as_a_list = list(raw_input_set)
    random.shuffle(as_a_list)
    for some_raw_input in as_a_list:
        print(some_raw_input)
        key = keyboard.read_key(suppress=False)  # letter pressed on the keyboard
        time.sleep(.5)
        print()
        assigned_token = number_tags[key]
        ethnicity_file.write(some_raw_input + ' ' + assigned_token + '\n')

    ethnicity_file.close()


"""
get rid of the nones
"""
def get_ethnicity_training_set():
    ethnicity_train = set()
    f1 = open("/Users/aidanlear/PycharmProjects/voice/ethnicity.txt")

    for line in f1:
        line_as_array = line.split()

        if(line_as_array[1] == number_tags['0']):
            pass
        else:
            ethnicity_train.add((line_as_array[0],line_as_array[1]))

    return ethnicity_train


def classify():
    cl = NaiveBayesClassifier(train)
    print("Accuracy: {0}".format(cl.accuracy(test)))
    cl.show_informative_features(7)
    print(cl.informative_features())

classify()
