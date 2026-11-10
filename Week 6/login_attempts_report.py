"""Finding: prints IP with most failed logins and single-session flags."""
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
HERE=Path(__file__).resolve().parent
df=pd.read_csv(HERE.parent/"login_attempts.csv")
print(df.head(),df.dtypes,len(df),sep="\n")
print("Sessions with >=3 failures:",df[df["failed"]>=3])
totals=df.groupby("ip")["failed"].sum().sort_values(ascending=False)
print("Total failures by IP:",totals)
print("Escalate first:",totals.index[0],"because it has the most aggregate failed attempts")
df["suspicious"]=df["failed"].apply(lambda x:x>=3)
totals.plot(kind="bar",title="Failed logins per IP")
plt.tight_layout();plt.savefig(HERE/"failed_logins_per_ip.png");plt.close()
df[df["suspicious"]].to_csv(HERE/"flagged_ips.csv",index=False)
