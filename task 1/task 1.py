import collections
import string


text = input('Введите текст: ')
text = text.lower()
spec_chars = string.punctuation + '\n\xa0«»\t—…'
text = "".join([ch for ch in text if ch not in spec_chars])
longest = max(text.split(), key=len)
counter = collections.Counter(text.split())
most_common, occurrences = counter.most_common()[0]
print('Самое длинное слово: ', longest)
print('Самое встречающееся слово: ', most_common)
