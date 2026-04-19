
# 📊 Class Result Analyzer Dashboard

A simple and interactive **Streamlit web application** to analyze student marks from an Excel file.
This project helps visualize performance, identify toppers, and track pass/fail statistics efficiently.

---

## 🚀 Features

* 📂 Upload Excel file with student marks
* 🏆 Top 5 and 📉 Bottom 5 students with ranking
* 📊 Automatic percentage calculation
* ✅ Pass / ❌ Fail classification
* 📈 Bar chart for overall performance
* 🥧 Pie chart for pass vs fail ratio
* 🥇 Subject-wise toppers
* ⚠️ Failed students list
* ⬇️ Download processed report as CSV

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Pandas**
* **Matplotlib**

---

## 📁 Project Structure

```
📦 student-performance-analyzer
 ┣ 📜 web_ui.py
 ┣ 📜 README.md
 ┗ 📊 sample_data.xlsx (optional)
```

---

## ▶️ How to Run

1. Clone the repository:

```
git clone https://github.com/your-username/student-performance-analyzer.git
cd student-performance-analyzer
```

2. Install dependencies:

```
pip install streamlit pandas matplotlib openpyxl
```

3. Run the app:

```
streamlit run web_ui.py
```

---

## 📄 Input Format (Excel File)

Your Excel file should look like this:

| Name | Subject1 | Subject2 | Subject3 | Subject4 | Subject5 |
| ---- | -------- | -------- | -------- | -------- | -------- |
| John | 78       | 85       | 90       | 88       | 76       |

* First column must be **Name**
* Next 5 columns should be **marks**

---

## 🎯 Use Cases

* College mini project
* Academic result analysis
* Teacher performance tracking tool
* Beginner data analytics project

---

## 👨‍💻 Author

**Tejas Sahane**  
**Year: 2025**

---
