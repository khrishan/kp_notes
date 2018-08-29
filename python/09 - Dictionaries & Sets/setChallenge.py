# Creare a program that takes some text and returns a set of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
# 
# You can either enter the text from the keyboard or
# initalise a string variable with the string.

vowels = frozenset('aeiou')

text_input = input('Please enter some text : ')

print(sorted(set(text_input).difference(vowels)))
