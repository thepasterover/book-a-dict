"""
Author: Boobalan Shettiyar
github: github.com/thepasteroevr
twitter:@ paste_the
"""


from PyDictionary import PyDictionary
from PyPdf import list_words
from time import sleep

py_dict = PyDictionary

# Remove the integers from the list.
list_words = [i for i in list_words if not i.isdigit()]

# Open the file for excluded data.
with open('/home/bhuvan/Documents/book-dict/exclude', 'r') as file:
    # Convert the txt file into list
    data = file.readlines()

# Remove the "\n" from the list.
ex_data = [d.replace("\n", "") for d in data if d.endswith("\n")]

excluded_list = set(list_words) - set(ex_data)  # Subtract the main list with ex data.
excluded_list = list(excluded_list)
excluded_list = sorted(excluded_list)

er_list = [",", ".", "™", ";"]


def remove_extras(excluded_list, er_list):
    for er in er_list:
        excluded_list = [i.strip(er) for i in excluded_list]
        excluded_list = [i.replace(er, " ") for i in excluded_list]
        return excluded_list


excluded_list = remove_extras(excluded_list, er_list)


def form_noun(means):
    # Check if the key exists in the dict for every noun.
    if 'Noun' in means:
        print("Noun: ")

        # Print the noun contents of the dict.
        for n in means['Noun']:
            print("\t" + n)


def form_verb(means):
    # Check if the key exists in the dict for every verb.
    if 'Verb' in means:
        print("Verb: ")

        # Print the verb contents of the dict.
        for v in means['Verb']:
            print("\t" + v)


def form_adj(means):
    # Check if the key exists in the dict for every adj.
    if 'Adjective' in means:
        print("Adjective: ")

        # Print the Adj contents of the dict
        for a in means['Adjective']:
            print("\t" + a)


# Format the Nouns, Verb and Adj for readable format.
def format_text(mean_words):

    try:

        # Get meaning of the word
        means = py_dict.meaning(mean_words)

        form_noun(means)
        form_verb(means)
        form_adj(means)

    except TypeError:
        pass
    except IndexError:
        pass


# Print the name of meaning of word requested.
def name_id(mean_words):
    print("\n" + mean_words.upper())
    format_text(mean_words)

try:
    # The main for loop for the script.
    for mean_words in excluded_list:
        name_id(mean_words)
except KeyboardInterrupt:
    sleep(5)
    print("-" * 100)
    print("Thanks for using! The meanings have been printed.")
