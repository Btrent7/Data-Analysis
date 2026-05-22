import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def gov_asst(pop):
    if pop > 2000000:
        return pop * 0.22
    elif pop > 1500000:
        return pop * 0.52
    elif pop > 1000000:
        return pop * 0.78
    else:
        return pop * 0.98

state_pop = {
    "Texas": 2250000,
    "California": 3100000,
    "Oklahoma": 900500,
    "Arkansas": 1000050,
    "Florida": 1990000,
    "New Mexico": 1860000,
    "Minnesota": 1790000,
    "New York": 2500000,
    "Washington": 2005000,
    "Idaho": 320000,
    "Nebraska": 410000
    }

# Covert dict to DataFrame, Drop duplicate column, Melt to normalized table
df_state = pd.DataFrame(state_pop, index=["state", "pop"]).drop(index="state")
df_state_melt = df_state.melt()


# Rename Columns
state = df_state_melt.rename(columns={"variable": "State", "value": "Population"})


# Apply Gov Asst Column
state["Gov Asst"] = state["Population"].apply(gov_asst)
print(state)


# Set positions
x = np.arange(len(state)) 
width = 0.35 


plt.figure(figsize=(12, 6))
plt.bar(x - width/2, state["Population"], width, label='Population', color='skyblue')
plt.bar(x + width/2, state["Gov Asst"], width, label='Gov Assistance', color='lightgreen')


# Labels and title
plt.xticks(x, state["State"], rotation=45)
plt.xlabel("State")
plt.ylabel("Amount ($)")
plt.title("Population vs. Government Assistance per State")
plt.legend()
plt.tight_layout()
plt.show()