# TomatoBook.com
# About this project
Project name:
Project type: browser-based productivity app
Programming languages: JS, HTML, CSS, PHP, SQL, Python (with additional APIs)
Version: 1.0

# features
1.Account Access Management
to determine who the users are (admin, employees)

2.Inventory/Product Management
Product data (name, cost, selling price, profit, cash outflow)

3.Point of Sale
Cashier interface and interactive notebook, with semi-real-time transactions

Reporting Program
A program for generating reports, charts, final conclusions, and automatic notes

1.Local Storage in the Browser
Ensures data remains secure even without an internet connection



Translated with DeepL.com (free version)


# structure
# Flask logic
my_productivity_app/
├── manage.py
├── config/
│   ├── settings.py
│   '── urls.py
├── notes/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   '── urls.py
├── finance/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   '── urls.py
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── notes/
│   '── finance/
├── static/
│   |── css/style.js
│   '── js/calculator.py
└── db.sqlite3_integration.py


# Browser strorage eviorement
