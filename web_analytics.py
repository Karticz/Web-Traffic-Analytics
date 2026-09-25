import pandas as pd


data = {
    'Page': ['Home', 'About Us', 'Products', 'Pricing', 'Checkout'],
    'Page_Views': [1500, 400, 1200, 300, 200],
    'Avg_Session_Duration_sec': [120, 60, 180, 45, 30],
    'Drop_Off_Rate_Percentage': [10, 25, 15, 30, 75]
}

df = pd.DataFrame(data)

print("--- Web Traffic Analytics: Key Metrics ---\n")
print(df)

ం
max_dropoff = df.loc[df['Drop_Off_Rate_Percentage'].idxmax()]
print(f"\n[Insight] Highest Drop-off Point identified at: '{max_dropoff['Page']}' page with a {max_dropoff['Drop_Off_Rate_Percentage']}% drop-off rate.")
