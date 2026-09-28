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

reg1 = re.compile(r'.*tina$')
reg1number = reg1.findall("tina are you good tina")
print(reg1number)

# The ? matches zero or one of the preceding group.
# The * matches zero or more of the preceding group.
# The + matches one or more of the preceding group.
# The {n} matches exactly n of the preceding group.
# The {n,} matches n or more of the preceding group.
# The {,m} matches 0 to m of the preceding group.
# The {n,m} matches at least n and at most m of the preceding group.
# {n,m}? or *? or +? performs a nongreedy match of the preceding group.
# ^spam means the string must begin with spam.
# spam$ means the string must end with spam.
# The . matches any character, except newline characters.
# \d, \w, and \s match a digit, word, or space character, respectively.
# \D, \W, and \S match anything except a digit, word, or space character,
# spectively.
# [abc] matches any character between the brackets (such as a, b, or c).
# [^abc] matches any character that isn’t between the brackets.

subRegex = re.compile(r'agent \w+', re.IGNORECASE)
newSubRegex = subRegex.sub('Censored', 'Agent Carter gave docs to Agent Ashsih')
print(newSubRegex)

emailRegex = re.compile(r'[a-zA-Z_\-0-9\.]+@[a-zA-Z\-_0-9]+\.[a-zA-Z]+', re.VERBOSE | re.DOTALL)
emailsList = emailRegex.findall('''
Contact Us
Reach Us by Email - email is the best way to reach us
General inquiries and order questions: info@nostarch.com
Discount codes and promotions: We offer promo codes periodically via our newsletter. Sign up here to get notified. We are unable to issue individual coupon codes by request.
Wholesale, bookstore, and bulk orders (20+ copies): sales@nostarch.com
Academic requests: academic@nostarch.com (Further information)
Conference and event inquiries: conferences@nostarch.com
Errata - please send any errata reports to: errata@nostarch.com
Media requests: media@nostarch.com
Proposals or editorial inquiries: editors@nostarch.com
Rights inquiries: rights@nostarch.com (Further information)
Interested in working with us? 
View our current job openings
Physical Address
No Starch Press Inc
245 8th Street
San Francisco, CA 94103
USA
Mailing Address
No Starch Press Inc
329 Primrose Road,  #42
Burlingame, CA 94010-4093
USA

Phone: 800.420.7240 or +1 415.863.9900
Fax: +1 415.863.9950

Reach Us on Social Media
Twitter Facebook Instagram Linkedin Pinterest
''')
emailsList.sort()
for i in range(len(emailsList)):

    print(emailsList[i]+"\n")