
## Project Setup

## Setup with Docker

If you prefer using Docker, follow these steps (NOTE!!! make sure you have Docker installed and running):

1. Build the Docker image:
    ```bash
    docker build -t yp-remarcable .
    ```

2. Start the application using Docker:
    ```bash
    docker run -p 8000:8000 remarcable
    ```

The application will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).


## Alternative: Setup on local machine

### Requirements:
- Python 3.11 or higher
- pip (Python package installer)
- virtual environment (example: [venv ](https://docs.python.org/3/library/venv.html#))

### 1. Clone the Repository

```bash
git clone https://github.com/ypyrko/yp-remarcable.git
cd yp-remarcable
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
source venv/bin/activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
``` 

### 6. Populate the Database
```bash
python manage.py populate_sample_data
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

### 8. Access the Application   
Open your web browser and go to:

```
http://128.0.1:8000/
```

### 9. Create a Superuser (Admin Account)
To access the admin interface, you need to create a superuser account:
```bash
python manage.py createsuperuser
```
Follow the prompts to set up your admin account.

### 10. Access the Admin Interface
Open your web browser and go to:
```
http://128.0.1:8000/admin/
```