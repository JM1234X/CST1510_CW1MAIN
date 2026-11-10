"""Week 6 Record Check — Cyber Security lane, Excellent tier.
Run from this directory: python template.py
Synthetic login records for coursework practice.
"""
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

HERE = Path(__file__).resolve().parent
df = pd.read_csv(HERE / "cyber_login_records.csv")
# For this demonstration, percent means failed logins relative to total attempts.
df["percent"] = df["failed_logins"] / df["total_attempts"] * 100
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)
print("All login records:")
print(df.to_string(index=False))
print("\nNon-OK records:")
print(df[df["status"] != "OK"].to_string(index=False))
counts = df.groupby("status").size()
print("\nCounts by status:")
print(counts)
df.to_csv(HERE / "cyber_record_report.csv", index=False)
counts.plot(kind="bar", title="Login records by status")
plt.ylabel("Records")
plt.tight_layout()
plt.savefig(HERE / "cyber_status_counts.png")
plt.close()
