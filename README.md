The Trivia App is a simple and interactive web application built using Django for the backend, and HTML, CSS, and JavaScript for the frontend. The app allows users to answer trivia questions, provides hints, and dynamically loads new questions after each correct answer. I designed this project as a fun way to practice  Django, AJAX, and frontend technologies.

Features
Dynamic Question Display: Trivia questions are dynamically loaded from a database.
Hint System: A hint is available for each question, which users can reveal with a button click.
AJAX for Answer Evaluation: The app uses AJAX to evaluate answers without reloading the page.
Responsive Design: Built using Bootstrap, the app is responsive and mobile-friendly.
User Interaction: Immediate feedback is provided based on the correctness of the answer.
Technologies Used
Backend: Django (Python)

Models for storing trivia questions, answers, and hints.
Views to handle question rendering and answer evaluation using JSON responses.
Frontend:

HTML/CSS: For structuring and styling the pages, with custom styling for the trivia app.
Bootstrap: For responsive design and layout.
JavaScript: For interactivity and DOM manipulation (e.g., fading effects, handling form submissions).
jQuery: Used for handling AJAX requests to evaluate answers and update questions dynamically.
Database: Django ORM (e.g., SQLite by default) to manage trivia questions and answers.
