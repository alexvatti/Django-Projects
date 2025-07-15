# Django-Projects


Here are the **Django project setup steps** written clearly and concisely:

---

````markdown
# ✅ Steps to Start a Django Project

1. **Install Django**
   ```bash
   pip install django
````

2. **Create a New Project**

   ```bash
   django-admin startproject myproject
   ```

3. **Navigate to Project Directory**

   ```bash
   cd myproject
   ```

4. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

   > Open browser: `http://127.0.0.1:8000/`

5. **Create an App**

   ```bash
   python manage.py startapp myapp
   ```

6. **Add App to `settings.py`**

   * Open `myproject/settings.py`
   * Add `'myapp'` to `INSTALLED_APPS` list.

7. **Create a View in `myapp/views.py`**

   ```python
   from django.http import HttpResponse

   def home(request):
       return HttpResponse("Hello, Django!")
   ```

8. **Create `myapp/urls.py`**

   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('', views.home, name='home'),
   ]
   ```

9. **Update `myproject/urls.py` to include app URLs**

   ```python
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('myapp.urls')),
   ]
   ```

10. **Run the Server Again**

    ```bash
    python manage.py runserver
    ```

    > Visit `http://127.0.0.1:8000/` to see "Hello, Django!"

```





