

# Youtube Channel Rater - Rate the YouTube channel you watched and save it. 

This project is a Django-based web application that provides a platform for users to rate and review YouTube channels. The application utilizes Django's Model-View-Controller (MVC) architecture, along with Django Rest Framework to create a RESTful API for managing YouTube channels, their ratings, and user information.

## Features

- Users can view a list of YouTube channels and their details, including title, description, average rating, and number of ratings.
- Users can rate and update their ratings for specific YouTube channels.
- User registration and authentication are implemented using Token Authentication, ensuring secure access to the rating system.
- User passwords are securely hashed and not exposed in the API responses.

<img width="1423" alt="Screenshot 2023-09-05 at 8 33 36 PM" src="https://github.com/MagdaSlifierz/Youtube_Channel_Rater/assets/49603115/0b4369a9-a30f-458a-8d44-55e7afeb27db">

<img width="1436" alt="Screenshot 2023-09-05 at 8 50 27 PM" src="https://github.com/MagdaSlifierz/Youtube_Channel_Rater/assets/49603115/585e7e96-5b82-42e4-ae83-7f25a24bf4fb">

<img width="1434" alt="Screenshot 2023-09-05 at 9 29 22 PM" src="https://github.com/MagdaSlifierz/Youtube_Channel_Rater/assets/49603115/94a222a8-b209-408c-a3ca-4e7b655a7b9a">

<img width="1436" alt="Screenshot 2023-09-05 at 8 55 47 PM" src="https://github.com/MagdaSlifierz/Youtube_Channel_Rater/assets/49603115/7e0e7c87-e5f3-40f5-a788-00e510b90037">

<img width="1434" alt="Screenshot 2023-09-05 at 8 31 43 PM" src="https://github.com/MagdaSlifierz/Youtube_Channel_Rater/assets/49603115/3514f99b-7f17-4d1d-8696-dbd483c25507">
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

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   ```

2. Set up the database by running migrations:

   ```bash
   python manage.py migrate
   ```

3. Create a superuser account to access the Django admin panel:

   ```bash
   python manage.py createsuperuser
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

5. Access the API documentation and admin panel:

   - API Documentation: `http://localhost:8000/`
   - Admin Panel: `http://localhost:8000/admin/`
