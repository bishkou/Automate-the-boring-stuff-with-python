import re

phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')

mo = phoneNumRegex.findall('My number is 445-555-4245 445-555-4245   ')

print(mo)