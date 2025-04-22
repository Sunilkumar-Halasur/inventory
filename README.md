Prerequisites
Make sure the following are installed on your system:
Python 3.8 or higher
pip (Python package manager)
virtualenv (optional, but recommended)
Git (if cloning from a repository)


1. Clone the Repository
git clone <your_repo_url>
cd <project_folder>


2. Create and Activate Virtual Environment
python -m venv venv
source venv/bin/activate     # For Windows: venv\Scripts\activate


3. Install Dependencies
pip install -r requirements.txt


4. Run Migrations
python manage.py makemigrations
python manage.py migrate


5. Create a Superuser (Optional)
python manage.py createsuperuser


6. Start the Development Server
python manage.py runserver

7. Access the Application
http://127.0.0.1:8000/
http://127.0.0.1:8000/api/items/