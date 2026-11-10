"""Finding: prints strongest category and percentage of unanswered responses."""
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
HERE=Path(__file__).resolve().parent
df=pd.read_csv(HERE.parent/"survey_results.csv")
print(df.head(),df.dtypes,len(df),sep="\n")
missing=len(df[df["answered"]==0])/len(df)*100
clean=df[df["answered"]==1].copy()
means=clean.groupby("category")["score"].mean().sort_values(ascending=False)
print("Unanswered percentage:",missing,"\nMean scores:",means)
print("Strongest category:",means.index[0])
clean["result"]=clean["score"].apply(lambda s:"Pass" if s>=60 else "Fail")
clean["result"].value_counts().plot(kind="bar",title="Survey pass/fail")
plt.tight_layout();plt.savefig(HERE/"survey_pass_fail.png");plt.close()
clean.to_csv(HERE/"survey_results_clean.csv",index=False)
