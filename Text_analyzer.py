import math

'''
author = 
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

user = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}

print('-' * 40)
print('Welcome to the app. Please log in:')

username = input('USERNAME: ')
password = input('PASSWORD: ')

print('-' * 40)

if user.get(username) == password:
    print('Welcome to the text analyzer!')
else:
    print('Username or password is wrong!')
    quit()

print('We have', len(TEXTS), 'to be analyzed')
number = int(input('Enter a number btw. 1 and 3 to select: '))
text = (TEXTS.pop(number - 1))

print('-' * 40)


text_str = str(text)
text_spl = text_str.split()
# Pocet slov
print('There are', len(text_spl), 'words in the selected text.')

title = 0
upper = 0
lower = 0
numeric = 0
result = 0

for word in text_spl:
    if word.istitle():
        title = title + 1
    elif word.isupper():
        upper = upper + 1
    elif word.islower():
        lower = lower + 1
    elif word.isdigit():
        numeric = numeric + 1
        result = result + int(word)

print('There are', title, 'titlecase words')
print('There are', upper, 'uppercase words')
print('There are', lower, 'lowercase words')
print('There are', numeric, 'numeric strings')

print('-' * 40)

star = []

while text_spl:
    klic = text_spl.pop()
    value = len(klic)
    star.append(value)


top = max(star)
i = min(star)


while star:
    if i in star:
        pocet = star.count(i)
        print(i, pocet *'*')
        i = i + 1
    else:
        break


print('-' * 40)

print('If we summed all the numbers in this text we would get:', float(result))










