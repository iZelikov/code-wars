import re

def pig_it(text):
    return re.sub(r'(\w)(\w*)(\W)?', r'\2\1ay\3', text)

print(pig_it("Pig latin is cool"))