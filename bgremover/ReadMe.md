## AI-Powered Background Removal for E-Commerce

Welcome! This project provides an AI-driven solution to automatically remove backgrounds from product images—just 
like remove.bg—and integrate seamlessly with your Django application.

---

### 📖 Introduction

E‑commerce sellers often spend hours manually cleaning and renaming product images.
This tool automates the process, using a machine-learning model to strip backgrounds and output clean PNG files. 
You can access the functionality via:

* **REST API**: Send images to an endpoint and receive processed images.
* **Direct Django Integration**: Embed the background removal logic directly in your web application.


### ⚙️ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/alexvatti/Django-Projects.git
   cd Django-Projects/bgremover
   ```

2. **Create a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Django settings**

   * Add `bgremover` to `INSTALLED_APPS` in `settings.py`.
   * Set up media directories:

     ```python
     MEDIA_URL = '/media/'
     MEDIA_ROOT = BASE_DIR / 'media'
     ```

5. **Migrate database**

   ```bash
   python manage.py migrate
   ```

---

