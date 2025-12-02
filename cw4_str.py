# str
name = "Djon"
print("name: ", name)
print(type(name))

str1 = "hello 123 привіт"
encodestr1 = str1.encode(encoding='utf-8')
print(encodestr1.decode('utf-8'))

newStr = 'someTEXT'
print(newStr[0])
print(newStr[5])
word1 = newStr[0:4]
print(newStr[-1])
print(newStr[-5:])

print(newStr.upper())
print(newStr.lower())
print(newStr.swapcase())

print(newStr.find("T"))
print(newStr.rfind('T'))

print(newStr.count('t'))

newStr = newStr.replace('!', ' ')

print(newStr.isalpha())

print(newStr.isupper())
print(newStr.startswith('some'))

print(newStr.strip())

password = "qwerty123ABC"
countCheck = False
upperCheck = False
lowerCheck = False
digitCheck = False

if len(password) < 6:
    print("Error length < 6")
else:
    countCheck = True

for s in password:
    if s.isdigit() and not digitCheck:
        digitCheck = True
    elif s.islower() and not lowerCheck:
        lowerCheck = True
    elif s.isupper() and not upperCheck:
        upperCheck = True

if digitCheck and lowerCheck and upperCheck:
    print("Password is okey!")
else:
    print("Error password !")
