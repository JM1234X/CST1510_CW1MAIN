"""
RECORD CHECK  -  my version
===========================

Name  :  (your name here)
Lane  :  IT
Date  :  (today's date)

Run it:   python template.py

Excellent version: a Record class (with status() and a class-level over-limit
counter), records loaded from servers.txt by load_records(), and a bordered
report for each one.
"""

# ====================================================================== CLASS

class Record:
    """One server: hostname (label), GB used (value) and GB total (limit)."""

    over_limit_count = 0     # class-level running total, shared by every Record

    def __init__(self, label, value, limit):
        """Store the hostname, GB used and GB total on this object."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return OVER LIMIT (100%+), WARNING (90%+) or OK, from self.value and self.limit."""
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        return "OK"


# ==================================================================== RECORDS

def load_records(path):
    """Read label,value,limit lines from a file and return a list of Records."""
    records = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records


records = load_records("servers.txt")


# ==================================================================== OUTPUT

for record in records:
    status = record.status()          # called once, then the variable is reused
    if status == "OVER LIMIT":
        Record.over_limit_count += 1  # update the class attribute via the class name

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"  Used (GB)   : {record.value:>10.1f}")
    print(f"  Total (GB)  : {record.limit:>10.1f}")
    print(f"  Status      : {status:>10}")
    print("=" * 34)

print()
print(f"{Record.over_limit_count} of {len(records)} servers were OVER LIMIT")
