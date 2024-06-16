# SocialMedia API

## Introduction

This repository contains a social media API built with Django. This API provides various endpoints to interact with social media functionalities like sending, listing, accepting and rejecting friend requests etc.

## Getting Started

### Prerequisites

Ensure you have the following installed on your machine:

- Docker
- Python 3.12
- PostgreSQL

### Setting Up the Environment

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/socialmedia-api.git
   cd socialmedia-api
   ```

2. **Create a `.env` file:**
   ```bash
   cp env.sample .env
   ```

### Running with Docker

1. **Build the Docker image:**
   ```bash
   docker build .
   ```

2. **Run the containers with Docker Compose:**
   ```bash
   docker compose up
   ```

### Running Locally with Django

1. **Create a PostgreSQL user:**
   ```sql
   CREATE USER socialmedia_user WITH PASSWORD 'password';
   ```

2. **Create a PostgreSQL database:**
   ```sql
   CREATE DATABASE socialmedia_db OWNER socialmedia_user;
   ```

3. **Create and activate a virtual environment:**
   ```bash
   python3.12 -m venv venv
   source venv/bin/activate
   ```

4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Migrate the database:**
   ```bash
   python manage.py migrate
   ```

6. **Run the Django development server:**
   ```bash
   python manage.py runserver
   ```

## Using the API

1. **Postman Collection and Environment:**
   The repository includes a Postman collection and environment. Import these files into Postman.

2. **Set the Environment:**
   Configure the environment in Postman with the appropriate values.

3. **Start Using the API:**
   You can now start using the API endpoints defined in the Postman collection.
