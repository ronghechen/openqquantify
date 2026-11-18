# OpenQQuantify

An AI-powered medical regulation assistant built with Flask, OpenAI, and SQLAlchemy.

## Overview

OpenQQuantify is a web application designed to help users explore medical regulations through a conversational interface. Users can submit questions, receive AI-generated responses, and optionally save their question-and-answer history.

## Features

- AI-powered question answering using the OpenAI API
- Flask backend for processing requests
- SQLAlchemy database integration
- Optional Q&A history storage
- Responsive frontend built with HTML, CSS, and JavaScript

## Tech Stack

**Frontend:** HTML, CSS, JavaScript

**Backend:** Python, Flask

**Database:** SQLite, SQLAlchemy

**AI Integration:** OpenAI API

## Local Setup

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:

   `pip install -r requirements.txt`

4. Create a `.env` file containing:

   `OPENAI_API_KEY=your_api_key_here`

5. Initialize the database if required by your application.
6. Start the Flask development server:

   `flask --app flask_app run`

## Project Status

This project is archived as a demonstration of full-stack development and AI API integration. A working OpenAI API key is required to use the AI functionality.

## Disclaimer

This project is an educational prototype and is not intended to provide professional medical or legal advice. Do not submit real patient information or protected health information.