# Customer Churn Prediction Using ML models and Django

A Django-based web application that predicts customer churn based on input data. The system utilizes **machine learning models** to analyze customer behavior and provides insights into retention strategies.

---

## 🚀 Project Overview

Customer churn prediction helps businesses retain customers by identifying potential churners and taking proactive measures. This project includes:
- ✔ A **Django** backend for model inference
- ✔ A **form-based UI** for user input
- ✔ Integration of **Machine Learning models** for predictions
- ✔ A **REST API** for external integrations

---

## 🏗 Project Structure

```
📂 churn_project/          # Main Django project folder
│── 📂 churn_app/         # Django application
│── 📂 staticfiles/       # CSS, JS, images, and other static assets
│── 📄 manage.py          # Django management script
│── 📄 requirements.txt   # Required dependencies
│── 📄 db.sqlite3         # SQLite database (avoid using in production)
│── 📄 utils.py           # Helper functions
│── 📄 .gitignore         # Files ignored by Git
```

---

## 🛠 Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/razYousuf/customer-churn-prediction.git
cd customer-churn-prediction
```

### 2️⃣ Create & Activate a Virtual Environment
```bash
python -m venv venv  
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations
```bash
python manage.py migrate
```

### 5️⃣ Run the Server
```bash
python manage.py runserver
```
Visit **http://127.0.0.1:8000/** in your browser.

---

## 🎯 Usage
1. **Enter customer details** in the provided form.
2. **Click ‘Predict’** to get the churn probability.
3. The result will display whether the customer is **likely to churn or stay**.
4. Check logs and API responses for detailed insights.

---

## 🖥 Machine Learning Model Integration
- The model is trained using **Scikit-Learn** and saved as a `.pkl` file.
- The prediction logic is implemented in `utils.py` and integrated into Django views.

---

## 🚀 Deployment

### On Render (Deployment Platform)
1. Create an account at [Render](https://render.com).
2. Create a new Web Service on Render.
3. Connect your GitHub repository containing the Django project.
4. Configure the deployment environment:
   - Set **Build Command**: `pip install -r requirements.txt`
   - Set **Start Command**: `python manage.py runserver 0.0.0.0:8000`
5. Render will automatically deploy your Django application.
6. Once deployed, Render will provide you with a public URL to access your app.
   
---

## 📡 API Endpoints
This app provides a **REST API** for external applications:

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/predict/` | Accepts JSON input and returns churn prediction |
| `GET` | `/api/status/` | Checks API health status |

Example API request using **cURL**:
```bash
curl -X POST http://127.0.0.1:8000/api/predict/ -H "Content-Type: application/json" -d '{"age": 35, "subscription_length": 12}'
```

---

## 🔧 Technologies Used
- **Backend:** Django, Django REST Framework
- **Frontend:** HTML, CSS, Bootstrap
- **Machine Learning:** Scikit-Learn, Pandas, NumPy
- **Database:** SQLite (for development), PostgreSQL (recommended for production)

---

## 👨‍💻 Contributing
We welcome contributions!
1. Fork the repository
2. Create a feature branch (`git checkout -b new-feature`)
3. Commit changes (`git commit -m "Add new feature"`)
4. Push to GitHub (`git push origin new-feature`)
5. Create a Pull Request

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 🤝 Acknowledgements
Special thanks to all contributors and the open-source community. 😊

---

## 📞 Contact
📧 Email: [razyousufi350@gmail.com]  
🔗 GitHub: [https://github.com/razyousuf](https://github.com/razyousuf)
