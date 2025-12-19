import re

with open('Lecture_7/the-verdict.txt', 'r', encoding='utf-8') as f:
    raw_text = f.read()
    
    
print(f"Total number of character: {len(raw_text)}")  # Total number of character: 20479
print(raw_text[:99]) # I HAD always thought Jack Gisburn rather a cheap genius--though a good fellow enough--so it was no



# text = "This is the, test, text! for splitting"
# result = re.split(r'(\s)', text)  # bo'sh joy bo'yich bo'lish
# print(result) # ['This', ' ', 'is', ' ', 'the,', ' ', 'test,', ' ', 'text!', ' ', 'for', ' ', 'splitting']

# new_result = re.split(r'([,.]|\s)', text)
# print(new_result)
# # ['This', ' ', 'is', ' ', 'the', ',', '', ' ', 'test', ',', '', ' ', 'text!', ' ', 'for', ' ', 'splitting']

# cleaned_result = [item for item in new_result if item.strip()]
# print(cleaned_result) # ['This', 'is', 'the', ',', 'test', ',', 'text!', 'for', 'splitting']


# text = "Hello, world. Is this-- a test?"
# result = re.split(r'([,.:;?_!"()\']|--|\s)', text)
# result = [item.strip() for item in result if item.strip()]
# print(result)


# # Strip whitespace from each item and then filter out any empty strings.
# result = [item for item in result if item.strip()]
# print(result)



# text = "Hello, world. Is this-- a test?"

# result = re.split(r'([,.:;?_!"()\']|--|\s)', text)
# result = [item.strip() for item in result if item.strip()]
# print(result)


preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(preprocessed[:30])


print(len(preprocessed))