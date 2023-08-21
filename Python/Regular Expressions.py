import re

text = "Hello, my email is example@email.com"
pattern = r'[\w\.-]+@[\w\.-]+'
emails = re.findall(pattern, text)
