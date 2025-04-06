import pandas

data = pandas.read_csv("nato-keys.csv")

final_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(final_dict)


def i():
    name = input("Enter a word: ").upper()
    try:  # If numbers or symbols are entered
        output = [final_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, please enter only letters in alphabet")
        i()
    else:
        print(output)


i()
