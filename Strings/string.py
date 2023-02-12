# strings : Ordered, imuatable, text representation

my_string = "Hello world"
print(my_string)

my_string_2 = "I'm a programmer"
print(my_string_2)

my_string = """Hello /
world"""
print(my_string)

char = my_string[0]
print(char)

substring = my_string[1:5]
print(substring)

greeting = "Hello"
name = "Tom"

sentence = greeting+" "+name
print(sentence)

for i in greeting:
    print(i)
    
if 'e' in greeting:
    print('yes')
else:
    print('No')
    
my_string ="     Hello  world  "
my_string.strip()
print(my_string)

print(my_string.upper())
print(my_string.lower())

print(my_string.startswith("world"))
print(my_string.endswith("Hello"))

print(my_string.find('o'))
print(my_string.count('o'))

print(my_string.replace("world","Universe"))


my_string = 'how are you doing'
my_list = my_string.split()
print(my_list)

new_string = "".join(my_list)
print(new_string)

my_list = ['a'] * 6
print(my_list)

my_string = ''.join(my_list)
print(my_string)

# %,.formate(), f-strings

var = "Tom"
my_string="the variable is %s"% var
print(my_string)


my_string="the variable is {}".format(var)
print(my_string)