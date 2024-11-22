# `Wagtail Dashboard`

**Wagtail** is completely **free and open source**. It is released under the **BSD license**, which means you can use, modify, and distribute it for free, even in commercial projects.

---

### **Why is Wagtail Free?**
Wagtail is supported by a global community of developers and organizations that contribute to its development. The open-source nature of Wagtail ensures:
1. **No Licensing Fees**: There are no costs associated with using Wagtail.
2. **Community Support**: You get access to a large community and open-source plugins.
3. **Customizability**: You can freely modify Wagtail to fit your needs.

---

### **Key Features of Wagtail**
1. **Content Management**:
   - Built-in page editor with drag-and-drop blocks.
   - Image management and rich text editing.

2. **Modern and Extensible**:
   - Designed for developers to create custom functionality easily.
   - Works seamlessly with Django.

3. **Open-Source Ecosystem**:
   - Active community contributing plugins and tools.
   - Free support via forums and GitHub issues.

---

### **Where Wagtail is Used**
Wagtail is used by small businesses, large corporations, and organizations such as:
- NASA
- Google
- Mozilla
- The Royal College of Art

---

Creating a blog website in Django with **Wagtail CMS** is an excellent choice because Wagtail provides a modern, flexible admin UI and powerful tools for managing content. Below is a step-by-step guide to create a **Django blog website** using Wagtail.

---

### **Step 1: Install Django and Wagtail**

1. Create a virtual environment (if not already done):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install Django and Wagtail:
   ```bash
   pip install wagtail
   ```

---

### **Step 2: Start a New Wagtail Project**

1. Create a new Wagtail project:
   ```bash
   wagtail start myblog
   ```

   This will generate a Django project structure preconfigured with Wagtail.

2. Navigate to the project directory:
   ```bash
   cd myblog
   ```

3. Apply migrations and create a superuser:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/admin/` to access the Wagtail admin interface. Log in using the superuser credentials.

---

### **Step 3: Configure Your Blog App**

1. Create a new app for your blog:
   ```bash
   python manage.py startapp blog
   ```

2. Add the app to your `INSTALLED_APPS` in `settings.py`:
   ```python
   INSTALLED_APPS += [
       'blog',
   ]
   ```

---

### **Step 4: Define Blog Models**

Edit `blog/models.py` to define your blog page model:

```python
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel

class BlogIndexPage(Page):
    """A page to list all blog posts."""
    introduction = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduction'),
    ]


class BlogPostPage(Page):
    """A page representing a single blog post."""
    date = models.DateField("Post date")
    body = RichTextField(blank=True)
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body'),
        ImageChooserPanel('featured_image'),
    ]
```

---

### **Step 5: Register the Models**

Edit `blog/wagtail_hooks.py` (create this file if it doesn’t exist):

```python
from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register
from .models import BlogIndexPage, BlogPostPage

class BlogPostAdmin(ModelAdmin):
    model = BlogPostPage
    menu_label = "Blog Posts"
    menu_icon = "doc-full"
    list_display = ("title", "date")
    search_fields = ("title", "body")

class BlogAdminGroup(ModelAdminGroup):
    menu_label = "Blog"
    menu_icon = "folder-open-inverse"
    items = (BlogPostAdmin,)

modeladmin_register(BlogAdminGroup)
```

---

### **Step 6: Create Templates**

Create `blog/templates/blog/blog_index_page.html` for the blog index page:

```html
{% extends "base.html" %}
{% block content %}
  <h1>{{ page.title }}</h1>
  <div>{{ page.introduction|richtext }}</div>
  <ul>
    {% for post in page.get_children.live %}
      <li>
        <a href="{{ post.url }}">{{ post.title }}</a>
      </li>
    {% endfor %}
  </ul>
{% endblock %}
```

Create `blog/templates/blog/blog_post_page.html` for individual blog posts:

```html
{% extends "base.html" %}
{% block content %}
  <h1>{{ page.title }}</h1>
  <p>{{ page.date }}</p>
  {% if page.featured_image %}
    <img src="{{ page.featured_image.get_rendition('fill-800x400').url }}" alt="{{ page.featured_image.title }}">
  {% endif %}
  <div>{{ page.body|richtext }}</div>
{% endblock %}
```

---

### **Step 7: Configure URL Routing**

Wagtail handles most of the routing for pages automatically. However, ensure your main `urls.py` includes Wagtail's URL handling:

Edit `myblog/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail import urls as wagtail_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cms/', include(wagtailadmin_urls)),  # Wagtail admin interface
    path('documents/', include(wagtaildocs_urls)),
    path('', include(wagtail_urls)),  # Wagtail front-end routing
]
```

---

### **Step 8: Add Pages in Wagtail Admin**

1. Log in to the Wagtail admin (`http://127.0.0.1:8000/cms/`).
2. Create a new **Blog Index Page** under the home page.
3. Add some **Blog Post Pages** under the Blog Index Page.
4. Publish the pages.

---

### **Step 9: View the Blog**

Visit the blog index page URL (e.g., `http://127.0.0.1:8000/blog/`) to see your blog posts listed. Click on any post to view its content.

---

### **Key Features of Wagtail for Blogging**

1. **Rich Text Editor**: Wagtail's built-in editor lets you add rich content (images, links, etc.).
2. **Drag-and-Drop Images**: Easily add images to your blog posts.
3. **SEO and Metadata**: Wagtail allows editing SEO settings for every page.
4. **Preview Before Publishing**: You can preview your blog posts before they go live.
5. **Customizable Admin Interface**: Modify the Wagtail admin to suit your needs.
