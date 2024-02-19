# [Social Media Platform](https://github.com/mohank6/social-media-platform/tree/dev)
# [Expense Manager](https://github.com/mohank6/expense-manager/tree/dev)

## Function-Based Views 

### Project Setup

**1. Initialize Django Project**
```bash
django-admin startproject <project-name> <path>
```
 **2. Create an App**
```bash
python manage.py startapp <app-name>
```

### Model Definition
Define data models in `models.py` within your app.
```python
from django.db import models

class TestModel(models.Model):
    name = models.CharField(max_length=255)
```

### Create Views
Create views (functions) to handle CRUD operations in `views.py` or `views/` .
```python
from django.http import JsonResponse
from .models import TestModel

def get(request):
    test = TestModel.objects.first().values('name')
    return JsonResponse(test, status=200)

```

### URL Routing
- Register views in `urls.py` within your app.
```python
from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.get , name='get'),
]
```
- Include these app URLs in project's `urls.py`.
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<base-url>', include('<app-name>.urls')),
]
```

