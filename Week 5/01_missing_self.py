# FIXED. Original error: TypeError - status() takes 1 positional argument but 2 were given.
# Cause: a method's first parameter must be self; Python passes the object in
# automatically, so "percent" was receiving the object and 95 had nowhere to go.

class Record:
    def status(self, percent):    # FIX: added self as the first parameter
        return percent

r = Record()
print(r.status(95))
