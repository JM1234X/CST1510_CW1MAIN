"""Finding: see printed highest-average region and highest-risk server."""
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
HERE=Path(__file__).resolve().parent
root=HERE.parent
df=pd.read_csv(root / "02 - Selecting and Filtering/examples/servers.csv")
print(df.head(), df.dtypes, len(df), sep="\n")
df["percent"]=df["used"]/df["total"]*100
print("Servers at >=90%:",len(df[df["percent"]>=90]))
print("Average by region:",df.groupby("region")["percent"].mean())
print("Highest risk:",df.sort_values("percent",ascending=False).iloc[0]["hostname"])
df["status"]=df["percent"].apply(lambda p:"OVER LIMIT" if p>=100 else "WARNING" if p>=90 else "OK")
df["status"].value_counts().plot(kind="bar",title="Server statuses")
plt.tight_layout();plt.savefig(HERE/"server_statuses.png");plt.close()
df[df["status"]=="OVER LIMIT"].to_csv(HERE/"servers_at_risk.csv",index=False)
