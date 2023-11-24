# Flight Booking Management System

Welcome to the Flight Booking Management System! This web application allows users to search for flights worldwide, find the best deals, and book accommodations hassle-free. The system is equipped with various features to enhance user experience, and it utilizes modern web development frameworks and technologies.

## Features

- **User Authentication:** Users can sign up and log in to the platform, ensuring a personalized experience.
- **Submission Throttling:** Throttling is implemented for search boxes to optimize the retrieval of search results.
- **Auto-fill User Details:** Simplify the booking process by auto-filling user details on the booking page.
- **Booking Confirmation:** Before payment, the system displays all confirmed details, providing users with a final review before completing the booking.
- **Print Booking:** Users can print their booking details for reference.
- **Review System:** Past guests can write reviews for flights, and the system performs sentiment analysis on these reviews.

## Technologies Used

- **Backend Framework:** Django
- **Backend Scripting Language:** Python
- **Frontend Technologies:** HTML, CSS, Django Template Language, Bootstrap, jQuery
- **Database:** SQLite3
- **Communication:** RESTful APIs implemented with Django's in-built support
- **AJAX Patterns:** XHR used for making AJAX requests
- **Microservices:** All functionality is implemented as microservices with communication through REST APIs.

## Intelligent Component - Sentiment Analysis

The sentiment analysis component of the system adds an intelligent touch. It retrieves all flight reviews from the database, classifies them into positive, neutral, and negative categories, and dynamically updates the sentiment as users post new reviews.

## How to Use

1. **Sign Up or Log In:** Start by creating an account or logging into the platform.
2. **Search for Flights:** Use the search feature to find flights in your desired destination.
3. **Book a Flight:** Select a flight, review the details, and complete the booking process hassle-free.
4. **Leave a Review:** Share your experience by leaving a review, and contribute to the sentiment analysis of the system.
