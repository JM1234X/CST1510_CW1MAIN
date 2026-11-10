# FIXED. Original error: AttributeError - 'Record' object has no attribute 'value'.
# Cause: __init__ stored the number as self.amount, but the last line read r.value.

class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value    # FIX: stored as "value" so r.value works
        self.limit = limit

r = Record("R-001", 87.0, 100.0)
print(r.value)
