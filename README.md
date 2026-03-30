#  URL Shortener with Analytics 

A full-stack URL shortener web application built using Flask and MySQL. This project allows users to convert long URLs into short, shareable links and track their usage with analytics.

---
## 🧠 Working

First, a POST request is sent using Postman containing the long URL.  
The Flask backend receives the request and stores the URL in a MySQL database, where a unique auto-increment ID is generated.  

This ID is then converted into a short code using Base62 encoding and updated in the database.  

When a user accesses the short URL, the system retrieves the corresponding original URL from the database and redirects the user to it.  
Additionally, each access is recorded to track click analytics.


## 📌 Features

* 🔗 Shorten long URLs into compact links
* 🔁 Redirect short URLs to original URLs
* 📊 Track click analytics for each URL
* 💾 Store URL mappings in MySQL database
* ⚡ Fast and efficient Base62 encoding

---

## 🧠 How It Works

1. User sends a POST request with a long URL
2. Flask backend receives the request
3. URL is stored in MySQL database
4. Unique ID is generated
5. ID is converted to short code using Base62 encoding
6. Short URL is returned to the user
7. When accessed, system fetches original URL and redirects

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Database:** MySQL
* **API Testing:** Postman
* **Encoding:** Base62 Algorithm

---

## 📂 Project Structure

```
URL-Shortener/
│── app.py
│── db.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Rajith-kumar/url-shortener.git
cd url-shortener
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Setup MySQL Database

```sql
CREATE DATABASE url_shortener;

USE url_shortener;

CREATE TABLE urls (
    id INT AUTO_INCREMENT PRIMARY KEY,
    long_url TEXT NOT NULL,
    short_code VARCHAR(10),
    clicks INT DEFAULT 0
);
```

---

### 4. Configure Database in Code

Update your MySQL credentials inside `db.py`

---

### 5. Run the Application

```bash
python app.py
```

Server will start at:

```
http://127.0.0.1:5000
```

---

## 🔌 API Endpoints

### 🔹 Shorten URL

**POST** `/shorten`

Request Body:

```json
{
  "url": "https://example.com"
}
```

Response:

```json
{
  "short_url": "http://127.0.0.1:5000/a"
}
```

---

### 🔹 Redirect URL

**GET** `/<short_code>`

Example:

```
http://127.0.0.1:5000/a
```

---

### 🔹 Analytics

**GET** `/analytics/<short_code>`

Example:

```
http://127.0.0.1:5000/analytics/a
```

---

## 🧪 Testing with Postman

* Open Postman
* Select POST request
* URL: `http://127.0.0.1:5000/shorten`
* Go to Body → raw → JSON
* Paste:

```json
{
  "url": "https://github.com"
}
```

---

## 📸 Screenshots (Add Your Images Here)

### 🔹 Postman Request

![Postman Screenshot](images/postman.png)

### 🔹 Short URL Response

![Response Screenshot](images/response.png)

### 🔹 Analytics Output

![Analytics Screenshot](images/analytics.png)

---

## 🌍 Real-World Concept

Currently, the project runs on localhost. In real-world systems like Bitly:

* Backend is hosted on cloud
* Database is remotely accessible
* URLs are publicly accessible worldwide

---

## 🚀 Future Improvements

* 🌐 Deploy on cloud (Render / AWS)
* 🔐 User authentication
* 📈 Advanced analytics dashboard
* ⏳ URL expiration feature
* 📱 Mobile-friendly UI

---

## 👨‍💻 Author

* Rajith Kumar Mantrabuddi

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
