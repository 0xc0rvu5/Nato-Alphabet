import pandas

#intialize global variables
DATA = pandas.read_csv('phonetic_alphabet.csv')
EXAMPLES = {row.letter: row.code for (index, row) in DATA.iterrows()}


#print each letter and a corrisponding example prior to additional globals for readability
print(f'\n{EXAMPLES}')


#user input used to output a phonetic response
CHOICE = input('\nSupply a word:\n ~ ').upper()
RESPONSE = [EXAMPLES[n] for n in CHOICE]


print(', '.join(RESPONSE))
