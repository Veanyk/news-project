# Django News Feed Application

A robust and user-friendly web application for creating and displaying a paginated news feed. This project was developed as a technical assessment for Sibers, demonstrating core Django skills, rich text content management, and modern deployment practices using containerization.

## Features
- **Paginated News Feed**: The main page displays a clean, responsive, and paginated list of all news articles.
- **Adjustable Page Size**: Users can dynamically change the number of news items displayed per page (10, 20, or 50).
  - **Full-Fledged News Editor**:
    - A dedicated page for creating new articles.
    - Integration of CKEditor, a powerful WYSIWYG (What You See Is What You Get) editor.
    - Allows for rich text formatting (bold, italics, lists, etc.).
    - Supports direct image uploads from the computer into the body of the article.
- **Main Image Upload**: Ability to attach a primary "header" image to each news article with a live preview and removal option in the creation form.
- **Clean User Interface**: A modern and visually appealing design built with Bootstrap 5.
- **Environment-Based Configuration**: Securely manages sensitive data like database credentials and SECRET_KEY using a .env file.
- **Containerized Deployment**: The entire application stack (web application + database) is containerized using Docker and Docker Compose for easy, reliable, and consistent deployment.

## Tech Stack
- **Backend**: Django 4.x+, Python 3.9+
- **Database**: PostgreSQL (or MySQL as per requirements)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Key Python Libraries**:
  - django: The core web framework.
  - psycopg2-binary: PostgreSQL adapter for Python.
  - django-ckeditor: Provides the rich text editor widget and image upload functionality.
  - python-dotenv: For managing environment variables from a .env file.
  - Pillow: For image processing.
- **Deployment**:
  - Docker
  - Docker Compose
    
## Project Structure

```text
    news_project/
    ├── news_project/         # Django project configuration
    │   ├── settings.py
    │   ├── urls.py
    │   └── ...
    ├── news_feed/            # Django app for the news feed
    │   ├── migrations/
    │   ├── templates/
    │   │   └── news_feed/
    │   │       ├── add_news.html
    │   │       ├── base.html
    │   │       └── news_list.html
    │   ├── admin.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── urls.py
    │   └── views.py
    ├── static/
    │   └── images/
    │       └── back.jpeg
    ├── .env.example          # Example environment file
    ├── .gitignore
    ├── Dockerfile            # Instructions to build the web container
    ├── docker-compose.yml    # Defines the multi-container application
    ├── manage.py
    ├── README.md
    └── requirements.txt
```

## Setup and Deployment

There are two ways to run this project: using Docker (recommended for simplicity and consistency) or setting it up manually.

### Option 1: Running with Docker (Recommended)

This method automatically sets up the Django application and the PostgreSQL database.
    
1. **Clone the repository:**
    ```bash
    git clone https://github.com/YourUsername/your-repo-name.git
    cd your-repo-name
    ```
    
2. **Create the environment file:**

    Copy the example .env.example file to .env and fill in your desired database credentials. These will be used to initialize the PostgreSQL container.
    ```bash
    cp .env.example .env
    ```
    (Then, open .env in a text editor and set your DB_USER, DB_PASSWORD etc.)

    
3. **Build and run the containers:**
    ```bash
    docker-compose up --build
    ```
    The application will be available at http://127.0.0.1:8000/.
    
### Option 2: Manual Local Development Setup
    
1. **Clone the repository:**
    ```bash
    git clone https://github.com/YourUsername/your-repo-name.git
    cd your-repo-name
    ```
   
2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
    
3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    
4. **Set up the database:**
    
    Ensure you have PostgreSQL running on your machine. Create a new database and a user for the project.
    

5. **Create the environment file:**
    
    Copy .env.example to .env and fill in the connection details for the database you just created.
    ```bash
    cp .env.example .env
    ```
    
6. **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```
7.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will be available at http://127.0.0.1:8000/.

## Key Code Highlights
### Rich Text Content with CKEditor
To provide a powerful content creation experience, the project integrates django-ckeditor. The News model uses a RichTextField instead of a standard TextField, which automatically renders the WYSIWYG editor in forms.
```bash
# news_feed/models.py
from ckeditor.fields import RichTextField

class News(models.Model):
    # ... other fields
    body = RichTextField(verbose_name="Тело новости")
```
To correctly display the HTML-formatted content from the editor, the template uses the |safe filter, instructing Django to render the raw HTML instead of escaping it.
```bash
<!-- news_feed/news_list.html -->
<div class="news-body-text">
    {{ news.body|safe }}
</div>
```

### Secure Configuration with Environment Variables
All sensitive settings (like SECRET_KEY and database credentials) are kept out of version control. The python-dotenv library is used in settings.py to load these values from a .env file at runtime.
```bash
# news_project/settings.py
from dotenv import load_dotenv
import os

load_dotenv() # Loads variables from .env

SECRET_KEY = os.getenv("SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        # ... and so on
    }
}
```
## Contact
Created by Veanyk - feel free to contact me