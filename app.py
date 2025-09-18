import requests
import pandas as pd
import matplotlib.pyplot as plt

COUNTRY = "india"
URL = f"https://disease.sh/v3/covid-19/countries/{COUNTRY}"
response = requests.get(URL)
data = response.json()

#Extract relevant data
covid_19 = []

info = {
    "Country": data.get("country"),
    "Total Cases": data.get("cases"),
    "Total Deaths": data.get("deaths"),
    "Total Recovered": data.get("recovered"),
    "Active Cases": data.get("active"),
    "Critical Cases": data.get("critical"),
    "Tests Conducted": data.get("tests"),
    "Population": data.get("population")
}

covid_19.append(info)

df = pd.DataFrame(covid_19)
print(df)

df.to_csv("covid_19_india.csv", index=False)

# Plotting the data
labels = ['Total Cases', 'Total Deaths', 'Total Recovered', 'Active Cases']
sizes = [data.get("cases"), data.get("deaths"), data.get("recovered"), data.get("active")]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
explode = (0.1, 0, 0, 0)  # explode the 1st slice   
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()

plt.savefig("covid_19_india_pie_chart.png")
plt.close()

# Bar chart for tests and population
labels = ['Tests Conducted', 'Population']
sizes = [data.get("tests"), data.get("population")]
colors = ['#ff9999','#66b3ff']
explode = (0.1, 0)  # explode the 1st slice   
plt.bar(labels, sizes, color=colors)
plt.show()

plt.savefig("covid_19_india_bar_chart.png")
plt.close()

print("Data and visualizations saved successfully.")






