# CORENSIC Startup Landing

An informational web page for the **CORENSIC** startup, providing an extended list of services and products offered by the company. The website features a convenient contact card and also collects visitor statistics, including their location, which is recorded in the database and can be viewed through the admin panel.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [License](#license)
- [Author](#author)

## Project Overview
The **CORENSIC Startup Landing** project serves as a professional landing page that showcases all the services and products provided by the startup. Additionally, it gathers visitor statistics (like location data) and stores them in a database, which can be accessed via the Django admin panel for insights and further analysis.

## Features
- **Comprehensive service and product listing**: Displays all offerings provided by the company.
- **Contact form**: A user-friendly contact card to facilitate communication with the company.
- **Visitor analytics**: Tracks and records guest visits and their locations.
- **Admin panel**: Django's built-in admin panel allows you to view and analyze visitor data.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/Ivan-Grigorev/CORENSIC_web-site.git
    cd CORENSIC
    ```

2. Set up a virtual environment:

    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

7. Visit `http://127.0.0.1:8000/` in your browser to view the landing page, and access the admin panel at `http://127.0.0.1:8000/admin`.

## Usage

After installation, you can use the web interface to explore the services offered by CORENSIC. The visitor statistics are automatically recorded and stored in the database, and you can manage or view them through the Django admin panel.

## Technologies

- **Django**: The web framework used for building the landing page and handling visitor statistics.
- **SQLite**: Database to store visitor statistics.
- **HTML/CSS/JavaScript**: Front-end technologies used to display the landing page content.

## Secret Key Management

To securely manage the Django `SECRET_KEY`, it is stored in a `secret_key.txt` file located in the root directory. The `settings.py` file automatically reads the key from this file.

Make sure to add `secret_key.txt` to your `.gitignore` to prevent it from being exposed in a public repository:

```bash
echo "secret_key.txt" >> .gitignore
```

## License

This project is licensed under the terms of the [LICENSE](./LICENSE).

## Copyright

© 2024 **CORENSIC Company**. All rights reserved.

While this project is released under the MIT License, all branding, logos, and trademarks used by the **CORENSIC Company** remain the exclusive property of the company. Unauthorized use of these elements is prohibited.


## Author

This repository was built and is maintained by [Ivan Grigorev](https://github.com/Ivan-Grigorev).
