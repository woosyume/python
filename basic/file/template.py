import string

s = """\
Hi $name.

$contents

Have a nice day
"""

# s를 직접 망가뜨리는 일이 없도록...
t = string.Template(s)
contents = t.substitute(name='Woosyume', contents='How are you?')
print(contents)

# Practice
with open('basic/file/template/email.txt') as f:
    f = string.Template(f.read())

# t를 그대로 쓸 수 있구나
contents = t.substitute(name='Woosyume', contents='How are you?')
print(contents)