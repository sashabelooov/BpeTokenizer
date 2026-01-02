<img width="1357" height="833" alt="image" src="https://github.com/user-attachments/assets/fec1f4f3-bd9d-4c97-9bbe-756d9f9e0a72" />

<img width="423" height="90" alt="image" src="https://github.com/user-attachments/assets/993d374e-ead9-4d31-ace4-2ffb2be8a010" />

```python
text = "<|endoftext|>hello world"

# tiktoken
import tiktoken
enc = tiktoken.get_encoding("cl100k_base")
print(enc.encode(text, allowed_special="all"))
# [100257, 15339, 1917]

# ours
from minbpe import GPT4Tokenizer
tokenizer = GPT4Tokenizer()
print(tokenizer.encode(text, allowed_special="all"))
# [100257, 15339, 1917]


print(f"\n tiktoken encoding:{enc.encode(text, allowed_special="all")}")
print(f"\n our encoding: {tokenizer.encode(text, allowed_special="all")}\n")
```
