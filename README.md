# Portfolio Backend Django

## Overview
This project is the backend for a personal portfolio website, developed using Django. It serves as the API for managing and retrieving portfolio data, including projects, education, experience, and a downloadable CV.

## Features
- **Project Management**: API endpoints to create, retrieve, update, and delete project information.
- **Education and Experience**: Endpoints to manage and display educational background and professional experience.
- **Dynamic Content**: Ability to handle dynamic content updates for the portfolio.
- **File Handling**: Supports file uploads, including images and PDFs for projects and CV.

## Installation

To set up and run this backend locally, follow these steps:

1. **Clone the Repository**
   ```
   git clone https://github.com/AMustafa4983/portfolio-backend-django.git
   cd portfolio-backend-django
   ```

2. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

3. **Database Migrations**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Run the Server**
   ```
   python manage.py runserver
   ```

## API Endpoints

The backend provides several API endpoints:

- `GET /get-projects/`: Retrieve all projects.
- `GET /get-project/<id>`: Retrieve a specific project by ID.
- `GET /get-education/`: Retrieve educational background.
- `GET /get-experience/`: Retrieve professional experience.
- `GET /get-cv/`: Download the CV.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please follow the standard fork-and-pull request workflow.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

This project is open-sourced under the MIT License. See the [LICENSE](LICENSE) file for more details.
