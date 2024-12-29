# GBV Support Platform
## Distinctiveness and Complexity
Why this project is distinct and complex:

The GBV Support Platform is a comprehensive web application designed to provide support and resources for survivors of Gender-Based Violence (GBV). Unlike a social network or an e-commerce site, this project focuses on offering a variety of support services, including crisis hotlines, counseling, legal assistance, and safe housing. The platform integrates several features that leverage both Django for back-end processing and JavaScript for front-end interactivity. The system includes user registration, secure login, incident reporting, and an administrative interface for superusers to review and manage incident reports, making it more complex and unique.

## Project Overview
The GBV Support Platform aims to create a safe and supportive environment for survivors of GBV. The application allows users to:

1. Register and log in to the platform securely.

2. Report incidents of GBV confidentially.

3. Access a directory of support services, including crisis hotlines, counseling, legal assistance, and safe housing.

4. Read inspiring survivor stories.

5. Superusers can review and manage incident reports, providing recommendations and connecting users with appropriate resources.

What's Contained in Each File

i) models.py
Defines the database schema for the application, including models for GBVCenter, Message, and IncidentReport.

ii) views.py
Contains the view functions that handle requests and responses for the application, including registration, login, incident reporting, and superuser management of incidents.

iii) urls.py
Maps URL patterns to corresponding view functions, enabling navigation within the application.

iv) admin.py
Configures the Django admin interface to manage models, providing an administrative view for superusers to review and update incident reports.

v) templates/
Contains HTML templates for the application, including home.html, register.html, login.html, report_incident.html, review_incidents.html, and update_incident.html.

vi) static/css/styles.css
Defines the CSS styles for the application, ensuring a consistent and mobile-responsive design across different devices.

## How to Run the Application
1. Clone the Repository

       git clone https://github.com/yourusername/gbv_support_platform.git cd gbv_support_platform

2. Install Dependencies: Ensure you have Python installed. Install the required Python packages:
   
       pip install -r requirements.txt

3. Apply Migrations: Run the database migrations to set up the database schema:
   
       python manage.py migrate

4. Create a Superuser: Create a superuser account to access the Django admin interface:
   
       python manage.py createsuperuser

5. Run the Development Server: Start the Django development server:
   
       python manage.py runserver

6. Access the Application: Open your web browser and go to http://127.0.0.1:8000/ to access the GBV Support Platform.

## Python Packages
The following Python packages are required to run the application:

i) Django

ii) Other packages as listed in requirements.txt

## Administrative Interface
Superusers can access the administrative interface at http://127.0.0.1:8000/admin/ to manage incident reports and provide recommendations.

## Mobile-Responsiveness
The application is designed to be mobile-responsive, ensuring a seamless user experience across different devices.
