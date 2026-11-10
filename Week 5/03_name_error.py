# FIXED. Original error: NameError - name 'status' is not defined.
# Cause: status() is a method, so it has to be called on an object: r.status().

class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        return "OVER LIMIT" if self.value > self.limit else "OK"

r = Record("R-001", 120.0, 100.0)
print(r.status())    # FIX: called on the object
