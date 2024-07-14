# Flask Task Management Application

## Table of Contents
1. [Introduction](#introduction)
   - [Overview](#overview)
   - [Purpose](#purpose)
   - [Features](#features)
2. [Getting Started](#getting-started)
   - [Installation](#installation)
   - [Configuration](#configuration)
   - [Dependencies](#dependencies)
3. [Architecture](#architecture)
   - [Overview](#architecture-overview)
   - [Structure](#structure)
   - [Database Schema](#database-schema)
4. [Usage](#usage)
   - [User Guide](#user-guide)
     - [Login and Signup](#login-and-signup)
     - [Managing Tasks](#managing-tasks)
     - [Task Categories](#task-categories)
5. [Development](#development)
   - [Technologies Used](#technologies-used)
   - [Folder Structure](#folder-structure)
   - [Key Components](#key-components)
6. [Testing](#testing)
   - [Test Cases](#test-cases)
   - [Tools Used](#tools-used)
7. [Appendix](#appendix)
    - [Glossary](#glossary)
    - [Troubleshooting](#troubleshooting)
    - [References](#references)

## Introduction

### Overview
The Flask Task Management Application is a web-based tool designed to help users organize and manage their tasks efficiently.

### Purpose
The purpose of this application is to provide users with a simple yet effective platform to keep track of tasks, manage deadlines, and categorize tasks based on their priority.

### Features
- User authentication and authorization using Flask-Login.
- Task management with features for adding, editing, and deleting tasks.
- Task categorization with default and customizable categories.
- Responsive web design for usability across devices.

## Getting Started

### Installation
To install and run the application locally, follow these steps:
1. Clone the repository from GitHub.
  ```bash
  git clone <repository_url>
  ```
2. Install dependencies using pip
  ```bash
  pip install -r requirements.txt
  ```
3. Set up the database configuration in config.py.
4. Initialize the database.
  ```bash
  flask db init
  flask db migrate -m "Initial migration"
  flask db upgrade
  ```
5. Run the application.
  ```bash
  flask run
  ```
6. Access the application at http://localhost:5000.
   
### Configuration

Ensure all necessary environment variables are set, especially `SECRET_KEY` and database credentials.

### Dependencies

- Flask
- Flask-Login
- Flask-SQLAlchemy

## Architecture

### Overview
The application follows a client-server architecture with Flask serving as the backend framework and MySQL as the database management system.

### Structure
- **Backend**: Flask application structured into modules (`auth`, `main`) and a shared `models` module for database interactions.
- **Frontend**: HTML templates using Jinja2 for dynamic content rendering.
- **Database**: MySQL database with tables for users, tasks, categories, etc.

### Database Schema
Detailed database schema with tables, fields, and relationships.

## Usage

### User Guide

#### Login and Signup
- Access the application with user credentials.
- Create a new account if you are a new user.

#### Managing Tasks
- View all tasks.
- Add new tasks.
- Delete tasks that are no longer needed.

#### Task Categories
- Manage task categories.
- View tasks based on categories.

## Development

### Technologies Used
- Flask
- SQLAlchemy
- HTML/CSS

### Folder Structure
  ```bash
  app/
  init.py
  models.py
  routes.py
  templates/
  static/
  ```


### Key Components
- Flask application setup (`create_app()` in `__init__.py`)
- User authentication (`Flask-Login`)
- Database models (`User`, `Task`, `Category`)

## Testing

### Test Cases
- Unit tests for backend functions
- Integration tests for database interactions

### Tools Used
- `unittest` (Python standard library)
- `pytest` (optional for more advanced testing)

## Appendix

### Glossary
- **Flask**: A lightweight WSGI web application framework in Python.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **MySQL**: An open-source relational database management system.
- **Blueprint**: A way to organize Flask applications into modules.

### Troubleshooting
- **Issue**: Application not starting.
  - **Solution**: Ensure all dependencies are installed and environment variables are set correctly.

- **Issue**: Database connection error.
  - **Solution**: Check the database URI in the configuration and ensure the database server is running.

- **Issue**: Cannot login.
  - **Solution**: Verify user credentials and ensure the database contains the user record.

### References
- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
- [Flask-Login Documentation](https://flask-login.readthedocs.io/en/latest/)
- [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

