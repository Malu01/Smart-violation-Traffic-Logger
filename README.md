# 🚦 Smart Traffic Violation Logger (Flask)

A lightweight **Flask-based web application** designed to help traffic authorities digitally manage and track traffic violations. This system replaces manual challan processes with a **smart, QR-enabled digital solution**.

---

## 📌 Project Overview

The **Smart Traffic Violation Logger** allows traffic officers to:

* Record violations easily
* Track payment status (Paid/Unpaid)
* Search and filter violation history
* Generate QR-based challans for public verification

Each violation generates a **unique QR code**, which when scanned displays the violation details and payment status.

---

## 🎯 Objectives

* Digitize traffic violation management
* Reduce paperwork and human errors
* Enable quick access to violation records
* Provide transparency using QR codes
* Build a real-world Flask CRUD application

---

## 🔥 Features

* ➕ Add traffic violation records
* 🔍 Search violations by vehicle number
* 📊 Filter by status (Paid/Unpaid)
* 💰 Update payment status
* 📱 QR code generation for each challan
* 🌐 Public page for QR-based status checking
* 🔐 Admin login system
* 🎨 Clean UI using Bootstrap

---

## 🛠️ Tech Stack

* **Frontend**: HTML, CSS, Bootstrap
* **Backend**: Python (Flask)
* **Database**: SQLite (SQLAlchemy ORM)
* **QR Code**: `qrcode` Python library

---

## 📁 Project Structure

```
smart_traffic_logger/
│
├── app.py              # Main application entry point
├── models.py           # Database models (SQLAlchemy)
├── static/
│   ├── css/            # Custom CSS
│   ├── qrcodes/        # Generated QR code images
│   └── js/             # Frontend scripts
├── templates/
│   ├── base.html       # Parent template (Navigation/Bootstrap)
│   ├── add_violation.html
│   ├── history.html
│   └── status.html     # Public page for QR scan
└── instance/
    └── database.db     # SQLite database file
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/traffic-violation-logger.git
cd traffic-violation-logger
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run Application

```
python app.py
```

### 4️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

## 🔑 Default Login

```
Username: admin
Password: admin
```

---

## 🔄 Workflow

1. Admin logs into the system
2. Adds violation details
3. Data stored in SQLite database
4. QR code generated automatically
5. User scans QR code
6. Public page displays violation + status
7. Admin updates payment status

---

## 📸 Screens 

* Login Page
* Dashboard
* Add Violation Form
* Violation History Table
* QR Code Display
* Public Status Page

---

## 🏆 Key Achievements

* Implemented full **CRUD operations**
* Integrated **QR code system**
* Built **secure login functionality**
* Designed **responsive UI**
* Created **real-world applicable system**

---

## ⚠️ Limitations

* Uses SQLite (not scalable for large systems)
* Basic authentication (no advanced security)
* No online payment integration
* Manual data entry required

---

## 🌟 Future Enhancements

* 💳 Payment gateway integration (Razorpay/Stripe)
* 📍 GPS-based violation tracking
* 📷 Upload violation proof images
* 📱 Mobile app integration
* ☁️ Cloud deployment (Render/AWS)

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---
