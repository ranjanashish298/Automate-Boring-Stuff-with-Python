#Do the same thing as the previous example, but this time using the re module.

import re 

phoneNumberRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
number = phoneNumberRegex.search("My phone number is 415-344-3222. This is also my number: 416-345-3223")
print(number.group())

heroRegex = re.compile(r'Batman | Tina Fey')
m1 = heroRegex.search("Batman and Tina Fey")
print(m1.group())

batRegex = re.compile(r'Bat(wo)+man')
m2 = batRegex.search("The Adventures of Batwoman")
print(m2.group())

phoneNumberRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
number = phoneNumberRegex.findall("My phone number is 415-344-3222. This is also my number: 416-345-3223")
print(" ".join(number))
