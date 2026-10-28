import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("SSB_AI_2023-2025.csv")

bransjer = {
    "58-63 Informasjon og kommunikasjon": "IT",
    "46 Agentur- og engroshandel med unntak av motorvogner": "Engroshandel",
    "55-56 Overnattings- og serveringsverksemd": "Overnatting"
}

df = df[df["industry"].isin(bransjer)]

# Gjennomsnitt av de fire bedriftsstørrelsene per bransje
data = df.groupby(["year", "industry"])["ai_any"].mean().unstack()
data = data.rename(columns=bransjer)

# Én linje per bransje
data.plot(marker="o", figsize=(12, 6))

plt.title("KI-bruk per bransje (2023–2025)")
plt.xlabel("År")
plt.ylabel("KI-bruk (%)")
plt.xticks([2023, 2024, 2025])
plt.grid(True)
plt.legend(title="Bransje", bbox_to_anchor=(1.02, 1), loc="upper left")
plt.tight_layout()
plt.show()
