# Flask-MySQL Docker Project

This project demonstrates a simple Flask web application that connects to a MySQL database using Docker Compose.
My Project

This is my project. You can find it on GitHub at:

[https://github.com/ibredam/Docker]

## Prerequisites

* Docker and Docker Compose installed.
* Git (optional, for version control).

## Setup

1.  **Clone the Repository (if you haven't already):**

    ```bash
    git clone https://github.com/ibredam/Docker

    cd flask-mysql-docker
    ```

2.  **Create `.env` File:**

    * Create a `.env` file in the project root directory.
    * Add the following environment variables, replacing the placeholders with your actual values:

        ```
        MYSQL_USER=your_mysql_user
        MYSQL_PASSWORD=your_mysql_password
        MYSQL_DATABASE=mydatabase
        FLASK_SECRET_KEY=your_flask_secret_key
        ```

    * **Important:** Generate a strong, random `FLASK_SECRET_KEY`.

3.  **Run Docker Compose:**

    ```bash
    docker-compose up --build
    ```

    * This will build the Docker images and start the containers.

## Access the Application

* Open your web browser and go to `http://localhost:5000`.

## Database Initialization

* The `init.sql` script is used to initialize the MySQL database. It creates the `mydatabase` database and populates it with sample data.

## Docker Compose Configuration

* The `docker-compose.yml` file defines two services: `db` (MySQL) and `web` (Flask application).
* The `web` service depends on the `db` service.
* The `secrets.env` file is used to pass environment variables to the `web` service.
* The database data is persisted using a Docker volume.

## Gunicorn Configuration

* The `gunicorn.py` file configures the Gunicorn server.

## Notes

* This project is intended for demonstration purposes.
* In a production environment, you should use more robust security measures and consider using a dedicated database service.
* Never commit your `.env` file to version control.

## Project Structure Diagram (Text-Based):

+---------------------+
| flask-mysql-docker  |
+---------------------+
|                     |
|  app.py             |  (Flask Application)
|  requirements.txt    |  (Python Dependencies)
|  Dockerfile          |  (Docker Image Build)
|  docker-compose.yml  |  (Container Orchestration)
|  init.sql            |  (Database Setup)
|  secrets.env         |  (Environment Variables)
|  gunicorn.py         |  (WSGI Server Config)
|  templates/          |  (HTML Templates)
|    index.html        |
|  static/             |  (Static Assets)
|    style.css         |
|                     |
+---------------------+
|            |
v            v
+-------------+  +-------------+
| MySQL       |  | Flask App   |
| (db)        |  | (web)       |
+-------------+  +-------------+
^            ^
|            |
+---------------------+
| Docker Compose      |
+---------------------+
