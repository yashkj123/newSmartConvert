# 🚀 SmartConvert — AI-Driven Customer Behavioral Analytics

SmartConvert is a full-stack AI-powered web application that helps businesses analyze customer purchasing behavior and predict future buying intent — all through an intuitive dashboard.

---

## 💡 Project Overview

- 🔍 Upload a CSV file with customer interaction data (recency, frequency, monetary)
- 🧠 A Naive Bayes machine learning model predicts which customers are likely to buy
- 📊 A pie chart and table provide real-time visual feedback
- 🌐 Built using Django, Bootstrap, Chart.js, and scikit-learn

---

## 🛠️ Tech Stack

| Layer        | Tools Used                             |
|--------------|-----------------------------------------|
| Backend      | Python, Django, Pandas, Joblib, Scikit-learn |
| Frontend     | Bootstrap, Chart.js, HTML/CSS            |
| ML Model     | Gaussian Naive Bayes                    |
| Deployment   | (Optional) Render / PythonAnywhere      |

---

## 📂 File Structure

```
SmartConvert/
├── model.pkl               # Trained ML model
├── requirements.txt        # Python dependencies
├── smartconvert/           # Django project
│   ├── manage.py
│   └── predictor/
│       ├── views.py
│       ├── forms.py
│       └── templates/
│           ├── upload.html
│           └── result.html
```

---

## 📥 Sample Input Format

Upload a CSV file with the following columns:

| recency | frequency | monetary |
|---------|-----------|----------|
| 10      | 5         | 200      |
| 30      | 2         | 80       |

---

## 📈 Output Example

- Tabular results showing prediction (`1 = likely to buy`)
- Pie chart summarizing predictions
- Interactive dashboard UI

---

## 🧠 ML Model Details

- Trained using `GaussianNB` (Naive Bayes)
- Features used: `recency`, `frequency`, `monetary`
- Predictions saved using `joblib`

---

## ▶️ How to Run

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/SmartConvert.git
cd SmartConvert

# Install dependencies
pip install -r requirements.txt

# Run Django server
python manage.py runserver
```

---

## ✨ Credit
**Yash Kumar Jha**  


---
