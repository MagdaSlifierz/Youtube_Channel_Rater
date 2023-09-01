

# Youtube Channel Rater - Rate the YouTube channel you watched and save it. 

This project is a Django-based web application that provides a platform for users to rate and review YouTube channels. The application utilizes Django's Model-View-Controller (MVC) architecture, along with Django Rest Framework to create a RESTful API for managing YouTube channels, their ratings, and user information.

## Features

- Users can view a list of YouTube channels and their details, including title, description, average rating, and number of ratings.
- Users can rate and update their ratings for specific YouTube channels.
- User registration and authentication are implemented using Token Authentication, ensuring secure access to the rating system.
- User passwords are securely hashed and not exposed in the API responses.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   ```

2. Install the required packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database by running migrations:

   ```bash
   python manage.py migrate
   ```

4. Create a superuser account to access the Django admin panel:

   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Access the API documentation and admin panel:

   - API Documentation: `http://localhost:8000/`
   - Admin Panel: `http://localhost:8000/admin/`

## API Endpoints

### YouTube Channels

- `GET /youtubeChannel/`: Retrieve a list of all YouTube channels with their details.
- `GET /youtubeChannel/{id}/`: Retrieve details of a specific YouTube channel.
- `POST /youtubeChannel/{id}/rate_youtube_channel/`: Rate or update the rating for a specific YouTube channel.

### Ratings

- `GET /ratings/`: Retrieve a list of all ratings.
- `GET /ratings/{id}/`: Retrieve details of a specific rating.

### Users

- `GET /user/`: Retrieve a list of all registered users.
- `POST /user/`: Register a new user.

## Authentication

Token-based authentication is used to secure the API endpoints. To authenticate, include an `Authorization` header with the value `Token <your-token>` in your requests. Tokens are generated upon user registration and login.

