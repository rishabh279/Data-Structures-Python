from strings.utils import string_to_list


def reverse_string_words(string):
    """Reverses the words in given string"""
    #arr = string_to_list(string)
    arr = string.split(' ')
    string = []
    for word in arr:
        string.insert(0, word)
    return 


if __name__ == '__main__':
    reverse_string_words('I Love Xgboost')