 # BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def check(value, limit):
    status = "OVER LIMIT" 
    if value > limit: 
        status = "OVER LIMIT" 
    else:
        status = "OK"

check(87, 100)
print(status)
