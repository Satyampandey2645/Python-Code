# ------------------------------------------------- Required Arguments --------------------------------------------------

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Ego", "Quill")  # Hello, Peter Ego Quill

# -------------------------------------------------- Default Arguments --------------------------------------------------

def name(fname, mname="John", lname="Watson"):
    print("Hello,", fname, mname, lname)

name("Amy")  # Hello, Amy John Watson

# -------------------------------------------------- Keyword Arguments --------------------------------------------------

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname="Peter", lname="Wesker", fname="Jade")  # Hello, Jade Peter Wesker

# ------------------------------------------ Variable-Length Arguments --------------------------------------------------

# -------------- Arbitrary Arguments (*args) ----------------------------

def name(*names):
    print("Hello,", names[0], names[1], names[2])

name("James", "Buchanan", "Barnes")  # Hello, James Buchanan Barnes


# --------------- Keyword Arbitrary Arguments (**kwargs) ----------------

def name(**data):
    print("Hello,", data["fname"], data["mname"], data["lname"])

name(fname="James", mname="Buchanan", lname="Barnes")  # Hello, James Buchanan Barnes

# -------------------------------------------- return statement ---------------------------------------------------------

def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))  # Hello, James Buchanan Barnes
