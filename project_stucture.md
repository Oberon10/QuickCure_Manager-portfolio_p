<QUICKCURE MANAGER>
   |
   |-- _init_.py                              # Initialize the Flask application.
   |-- routes.py                              # Define URL routes and corresponding view functions.
   |-- models.py                              # Define database models.
   |-- templates/
   |    |
   |    |-- index.html                        # Landing page
   |    |-- auth/
   |    |    |
   |    |    |-- register.html                # Page for patient registration.
   |    |    |-- login.html                   # Login page.
   |    |    |
   |    |-- appointment_scheduling.html       # Page for appointment scheduling.
   |    |-- staff_management.html             # Admin Page
   |    |-- patient.html                      # Patient's Profile
   |    |-- base.html                         # Base template containing common elements.
   |    |-- doctors.html                      # Doctor's Page
   |
   |-- static/
   |    |
   |    |-- css/
   |    |    |-- styles.css                   # Custom styles for the application.
   |    |    
   |    |-- js/
   |         |
   |         |-- main.js                      # Custom JavaScript functions for client-side logic.
   |
   |-- config.py                              # App configuration
   |-- run.py                                 # Start the app in development and production
   |-- requirement.txt                        # Application dependencies
   |
   |tests/
   |
   |-- venv/
   |-- .gitignore