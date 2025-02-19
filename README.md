# Flask-MySQL-Docker

A simple Flask web application that connects to a MySQL database, containerized with Docker and Docker Compose. Demonstrates how to use Docker secrets, environment variables, and a `my.cnf` file for database configuration.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Docker](#docker)
- [Database](#database)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Description

This project showcases how to build a Flask web application with a MySQL database, and how to containerize it using Docker and Docker Compose. It provides a practical example of managing database configurations and secrets in a Dockerized environment.

## Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/ibredam/flask-MySQL-Docker.git

    cd Flask-MySQL-Docker
    ```

2.  Ensure Docker and Docker Compose are installed on your system.

3.  Build and run the application:

    ```bash
    docker-compose up --build
    ```

## Usage

1.  Access the application in your web browser at `http://localhost:5000`.

2.  The application displays data from the `users` table in the MySQL database.

## Configuration

* **Database Credentials:** Database credentials are stored in the `secrets/secrets.env` file.
    ```
    MYSQL_HOST=db
    MYSQL_USER=app_user
    MYSQL_PASSWORD=app_password
    MYSQL_DATABASE=py_db
    ```
* **MySQL Configuration:** MySQL server configuration can be customized in the `my.cnf` file.
* **Python Configuration:** Database connection settings for the Flask application are managed in `database_config.py`.

## Docker

* **`Dockerfile`:** Defines the Docker image for the Flask application, installing dependencies and setting up the environment.
* **`docker-compose.yml`:** Defines the services (Flask app and MySQL database), volumes, secrets, and network configurations.
* **Volumes:** `db_volume` persists the MySQL database data, and `web_volume` mounts the application code.
* **Secrets:** Database credentials are passed as Docker secrets.

## Database

* **`init.sql`:** Initializes the MySQL database with the `users` table and sample data.
* **`my.cnf`:** Customizes the MySQL server configuration, allowing you to optimize performance or change default settings.

## Troubleshooting

* **"failed to solve: process "/bin/sh -c pip install --no-cache-dir -r requirements.txt" did not complete successfully: exit code: 1"**
    * This usually indicates missing system dependencies. Add the following to your Dockerfile, before the pip install line.
        ```dockerfile
        RUN apt-get update && apt-get install -y \
            pkg-config \
            libmariadb-dev \
            gcc \
            && rm -rf /var/lib/apt/lists/*
        ```
    * Also, check that all packages in your requirements.txt file are correct.
* **"Author identity unknown"**
    * Run the following git commands:
        ```bash
        git config --global user.email "your_email@example.com"
        git config --global user.name "Your Name"
        ```

## Contributing

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes.
4.  Submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgments

This project uses the Flask framework and MySQL.
