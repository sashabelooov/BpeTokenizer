with open('Lecture_7/the-verdict.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    
    
print(f"Total number of character: {len(text)}")  # Total number of character: 20479
print(text[:99]) # I HAD always thought Jack Gisburn rather a cheap genius--though a good fellow enough--so it was no


import re

text = "This is the, test, text! for splitting"
result = re.split(r'(\s)', text)  # bo'sh joy bo'yich bo'lish
print(result) # ['This', ' ', 'is', ' ', 'the,', ' ', 'test,', ' ', 'text!', ' ', 'for', ' ', 'splitting']

new_result = re.split(r'([,.]|\s)', text)
print(new_result)
# ['This', ' ', 'is', ' ', 'the', ',', '', ' ', 'test', ',', '', ' ', 'text!', ' ', 'for', ' ', 'splitting']

cleaned_result = [item for item in new_result if item.strip()]
print(cleaned_result) # ['This', 'is', 'the', ',', 'test', ',', 'text!', 'for', 'splitting']