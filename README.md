# 📞 Phone Management Application

A full-stack Phone Book Management application built using **Flask (Python)** for the backend and **React (Vite)** for the frontend. This app allows users to add, view, edit, and delete contacts with proper validations and API integration.

---

## 🚀 Tech Stack

### Backend

* Python
* Flask
* Flask-CORS
* MongoDB (via PyMongo)

### Frontend

* React (Vite)
* Tailwind CSS
* Lucide React Icons

---

## 📂 Project Structure

```
PhoneManagement/
│
├── Backend/
│   ├── app.py
│   ├── config/
│   │   └── config.py
│   ├── controllers/
│   │   └── contact_controller.py
│   ├── models/
│   │   └── contact_Schema.py
│   └── routes/
│       └── contact_routes.py
│
└── Frontend/
    ├── src/
    │   ├── Component/
    │   │   └── Contacts.jsx
    │   ├── App.jsx
    │   └── main.jsx
    ├── index.html
    └── package.json
```

---

## ⚙️ Backend Setup (Flask)

1️⃣ Navigate to backend folder:

```bash
cd Backend
```

2️⃣ Create virtual environment (optional but recommended):

```bash
python -m venv venv
venv\Scripts\activate
```

3️⃣ Install dependencies:

```bash
pip install flask flask-cors pymongo
```

4️⃣ Start MongoDB (make sure MongoDB is running locally)

5️⃣ Run the Flask server:

```bash
python app.py
```

Server will start on:

```
http://localhost:5000
```

---

## ⚛️ Frontend Setup (React + Vite)

1️⃣ Navigate to frontend folder:

```bash
cd Frontend
```

2️⃣ Install dependencies:

```bash
npm install
```

3️⃣ Start the dev server:

```bash
npm run dev
```

Frontend will run on:

```
http://localhost:5173
```

---

## 🔗 API Endpoints

| Method | Endpoint      | Description      |
| ------ | ------------- | ---------------- |
| GET    | /contacts     | Get all contacts |
| POST   | /contacts     | Add new contact  |
| PUT    | /contacts/:id | Update contact   |
| DELETE | /contacts/:id | Delete contact   |

---

## 📝 Features

* Add new contact
* Edit existing contact
* Delete contact
* View all contacts
* 10-digit contact number validation
* Email validation
* CORS enabled for frontend-backend communication

---

## 📌 Notes

* Make sure MongoDB is running before starting the backend.
* Update API URL in frontend if backend port changes.

```js
const API_URL = 'http://localhost:5000/contacts';
```

---

## 👨‍💻 Author

**Rahul Verma**
GitHub: [https://github.com/RahulVerma799](https://github.com/RahulVerma799)

---

## 📜 License

This project is open-source and free to use.

---

### ⭐ If you like this project, give it a star on GitHub!
