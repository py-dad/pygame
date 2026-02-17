import re


with open('post-e.txt', encoding="utf-8") as file:
    txt = file.read()

print(txt)

matches = []

dateRegex = re.compile(r'\d{1,2}-\d{1,2}-\d{2}')
match = dateRegex.findall(txt)
for m in match:
    print(m)

def wordReg(pattern, data):
    kwRegex = re.compile(pattern)
    kw = kwRegex.findall(data)
    print(len(kw))
    for k in kw:
        print(k)

patternD = r'\d{1,2}-\d{1,2}-\d{2}:.*'
pattern = re.compile('good'|'better')

wordReg(pattern, txt)