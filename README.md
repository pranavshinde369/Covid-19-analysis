# 🦠 COVID-19 Data Analysis (India)

This project fetches live COVID-19 data for **India** using the [disease.sh API](https://disease.sh/) and generates insights with visualizations.  
The data is stored in a CSV file, and results are displayed through pie and bar charts for better understanding.

---

## 📌 Features

- ✅ Fetches **real-time COVID-19 data** from the disease.sh API  
- ✅ Extracts and structures key statistics:
  - Country  
  - Total Cases  
  - Total Deaths  
  - Total Recovered  
  - Active Cases  
  - Critical Cases  
  - Tests Conducted  
  - Population  
- ✅ Saves the data to `covid_19_india.csv`  
- ✅ Generates visualizations:
  - **Pie Chart** → Case distribution (Total, Deaths, Recovered, Active)  
  - **Bar Chart** → Tests conducted vs. Population  
- ✅ Saves charts as PNG files for reporting  

---

## 📂 Output Files

- `covid_19_india.csv` → Tabular dataset of India’s COVID-19 stats  
- `covid_19_india_pie_chart.png` → Pie chart of case distribution  
- `covid_19_india_bar_chart.png` → Bar chart comparing tests and population  

---

## 📦 Installation

Install the required dependencies:

```bash
pip install requests pandas matplotlib
```

---

## ▶️ Usage

Run the script in your terminal:

```bash
python main.py
```

After execution:
- Data will be displayed in the console.  
- A CSV file and PNG charts will be saved in the project directory.  

---

## 📊 Example Console Output

```
  Country  Total Cases  Total Deaths  Total Recovered  Active Cases  Critical Cases  Tests Conducted  Population
0   India     45000000        530000         44000000       2000000          15000      1000000000  1380000000
```

---

## 🌍 API Reference

This project uses:  
👉 [disease.sh - Open Disease Data API](https://disease.sh/v3/covid-19/countries/india)

---

## 🔧 Customization

You can fetch data for **any country** by updating the `COUNTRY` variable in the script:

```python
COUNTRY = "usa"   # Fetch COVID-19 data for the United States
```
