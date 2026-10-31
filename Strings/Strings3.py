# Strings are immutable
a = "Satyam"
print(len(a))  # 6
print(a.upper())  # SATYAM
print(a.lower())  # satyam
print(a)  # Satyam

# ------------------------------------------------------ strip() -------------------------------------------------------

strr = "    Silver Spoon   "
print(strr.strip())  # Silver Spoon

# ------------------------------------------------------ rstrip() ------------------------------------------------------

b = "Goodbye!!!!!!"
print(b.rstrip('!'))  # Goodbye

# rstrip() removes only trailing characters(that appear at the end) not leading or in middle
c = "!!!Goodbye!!!!"
print(c.rstrip('!'))  # !!!Goodbye

# ------------------------------------------------------ replace() ------------------------------------------------------

d = "!!!Harry!!!Harry!!!Harry"
print(d.replace('Harry', 'John'))  # !!!John!!!John!!!John

# ------------------------------------------------------- split() -------------------------------------------------------

e = "!!Harry !!John !!Roman"
print(e.split(' '))  # ['!!Harry', '!!John', '!!Roman']

# ---------------------------------------------------- capitalize() -----------------------------------------------------

blogHeading = "introduction To Js"
print(blogHeading.capitalize())  # Introduction to js

# ------------------------------------------------------ center() -------------------------------------------------------

str1 = "Welcome to the Console!!!"
print(len(str1))  # 25
print(str1.center(50))  #              Welcome to the Console!!!
print(len(str1.center(50)))  # 50
print(str1.center(50, '.'))  # ............Welcome to the Console!!!.............

# ------------------------------------------------------ count() --------------------------------------------------------

f = "!!!Harry!!!Harry!!!Harry"
print(f.count('Harry'))  # 3

# ----------------------------------------------------- endswith() ------------------------------------------------------

g = "Welcome to the console !!!"
print(g.endswith("!"))  # True
print(g.endswith("!!!"))  # True
print(g.endswith('to', 4, 10))  # True

h = "Hi There! This is me"
print(h.endswith("e"))  # True
print(h.endswith("me"))  # True
print(h.endswith("re", 3, 8))  # True
print(h.endswith("re", 3, 9))  # False

# ------------------------------------------------------- find() --------------------------------------------------------

i = "He is Dan. He is an honest man."
print(i.find('is'))  # 3
print(i.find('the'))  # -1

# ------------------------------------------------------- index() -------------------------------------------------------
# find() & index() is same but only differece is that, in false case find() returns -1 and index() throws an error

j = "He is Dan. He is an honest man."
print(j.index('is'))  # 3
#print(j.index('the'))  # error

# ------------------------------------------------------- isalnum() -----------------------------------------------------

k = "WelcomeToTheConsole"
print(k.isalnum())  # True

l = "Welcome To The Console"
print(l.isalnum())  # False

m = "123Welcome123To123TheConsole123"
print(m.isalnum())  # True

# ------------------------------------------------------- isalpha() -----------------------------------------------------

n = "Welcome"
print(n.isalpha())  # True

o = "Welcome There"
print(o.isalpha())  # False

p = "12Welcome00"
print(p.isalpha())  # False

# ------------------------------------------------------- islower() -----------------------------------------------------

q = "hello world"
print(q.islower())  # True

r = "Hello world"
print(r.islower())  # False

# ----------------------------------------------------- isprintable() ---------------------------------------------------

s = "Hello World"
print(s.isprintable())  # True

t = "Hello\nWorld"
print(t.isprintable())  # False

u = "Hello\"World"
print(u.isprintable())  # True

# ------------------------------------------------------- isspace() -----------------------------------------------------

v1 = " "
print(v1.isspace())  # True

v2 = "   "
print(v2.isspace())  # True

v3 = ""
print(v3.isspace())  # False

v4 = "Hello World "
print(v4.isspace())  # False

# ------------------------------------------------------- istitle() -----------------------------------------------------

w1 = "World Health Organization"
print(w1.istitle())  # True

w2 = "To kill a Mocking bird"
print(w2.istitle())  # False

# ------------------------------------------------------- isupper() -----------------------------------------------------

x1 = "WORLD HEALTH ORGANIZATION"
print(x1.isupper())  # True

x2 = "World Health Organization"
print(x2.isupper())  # False

# ----------------------------------------------------- startswith() ---------------------------------------------------

y1 = "Python is an interpreted language"
print(y1.startswith('Python'))  # True
print(y1.startswith('Py'))  # True

# ------------------------------------------------------ swapcase() ----------------------------------------------------

z1 = "Python is An Interpreted language"
print(z1.swapcase())  # pYTHON IS aN iNTERPRETED LANGUAGE

# -------------------------------------------------------- title() -----------------------------------------------------

str2 = "His nam is Dan. Dan is an honest man"
print(str2.title())  # His Nam Is Dan. Dan Is An Honest Man


