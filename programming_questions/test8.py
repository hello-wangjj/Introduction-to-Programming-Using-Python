import re

pattern = re.compile(r'[^\d]{2}')
print(pattern.findall('1234abc'))
