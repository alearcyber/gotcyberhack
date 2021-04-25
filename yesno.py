import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))



input = ""

for word in sys.argv[1:]:
    input += word

