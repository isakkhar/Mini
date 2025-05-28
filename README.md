# 📝 Django Blog Project

A full-featured blogging platform built using Django, designed for creating, editing, and managing blog posts with a clean, user-friendly interface.

---

## 🚀 Features

* Create, edit, delete blog posts
* Markdown support for post content
* Comment system
* Categories & tags
* Responsive UI using Bootstrap
* Admin panel for full control
* SEO-friendly URLs
* Pagination for blog posts

---

## 🛠️ Tech Stack

* **Backend:** Django, Python
* **Frontend:** HTML, CSS (Bootstrap), JavaScript
* **Database:** SQLite (default), Dd.Sqlit3 (optional)
* **Other Tools:** Django Admin, Django ORM

---

## 📦 Installation

### Prerequisites

* Python 3.8+
* pip
* virtualenv (optional but recommended)

### Clone the Repository

```bash
git clone https://github.com/isakkhar/mini.git
cd django-blog
```

### Set Up Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create a Superuser

```bash
python manage.py createsuperuser
```

### Run the Development Server

```bash
python manage.py runserver
```

Access the app at [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📁 Project Structure

```
django-blog/
│
├── blog/               # Main blog app
├── users/              # Authentication app
├── templates/          # HTML templates
├── static/             # CSS, JS, images
├── media/              # Uploaded media files
├── manage.py
└── requirements.txt
```

---

## ✅ To-Do

* [ ] Add post likes system
* [ ] Implement search functionality
* [ ] Add user profiles
* [ ] Unit and integration tests

---

## 🙋‍♂️ Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Let me know if you'd like me to update it with your GitHub repo link or any custom features you've added.
