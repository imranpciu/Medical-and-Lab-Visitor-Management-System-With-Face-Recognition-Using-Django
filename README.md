# Medical-and-Lab-Visitor-Management-System-with-Face-Recognition-Using-Django
The "Medical and Lab Visitor Management with Face Recognition using Django" project is a cutting-edge solution designed to streamline and enhance the visitor management process in medical facilities and laboratories. Leveraging the power of Django, this web application provides a comprehensive suite of features, including user creation, live camera-based user image capture, face recognition-based user verification, and user management.

The project enables administrators to efficiently manage visitor information by allowing them to add, update, and delete user details. Users can be registered with relevant information and have their pictures taken using the integrated live camera functionality. The advanced face recognition algorithm ensures reliable user verification, eliminating the need for traditional identification methods.

Key Features:

User Management: The application allows administrators to create, update, and delete user accounts with their respective details.

Live Camera Integration: Users can conveniently capture their image using the live camera functionality, ensuring accurate representation.

Face Recognition: The project incorporates advanced face recognition technology to verify user identities, enhancing security and efficiency.

User-Friendly Interface: The intuitive web interface offers an easy-to-use experience for administrators and visitors alike.

This project is an innovative solution for medical facilities and laboratories, offering enhanced visitor management capabilities with the added benefit of face recognition technology. Automating processes, increasing security, and optimizing efficiency contribute to a more streamlined and secure environment for patients, staff, and visitors.

Utilizing Django's robust framework, this project showcases your proficiency in web development, image processing, and database management. By mentioning this project on your resume and GitHub profile, you demonstrate your ability to create sophisticated applications that leverage emerging technologies for practical use in real-world scenarios.


# How to run the project: 

Prerequisite: if don't have the "python 3.9.12" version, first download from here and install it: "https://www.python.org/downloads/release/python-3912/"

> step 1: Navigate the project directory and use the command in Git Bash "pipenv --python 3.9.12"

> step 2: Then "pipenv shell"

> step 3: open "CMD" navigate the project directory and run the virtual environment with "pipenv shell".

	  > Then run "pip install dlib-19.22.99-cp39-cp39-win_amd64.whl" The dlib file is in the project directory.

	  >  After installation exit from CMD.

> step 4: "pip install -r requirements.txt" and you can easily install all dependencies.

> step 5: Create a database in MySQL named "user_details", change the name and password in project setting.py if
	      your database has a different name and password.

> step 6: then run "python manage.py migrate"

> step 5: Now you can run the project with this command "Python manage.py runserver"

> step 6: finally hit this URL: "http://127.0.0.1:8000/user_details/" You can see the index page.  
	  

Note: Don't forget to connect your camera if you are using a Desktop. 

Now you can add users and verify them throw face recognition. 

Thanks...
