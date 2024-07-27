# Gemini Health App

Gemini Health App is a web application that analyzes the nutritional content of food items in an image. It uses Google Gemini API to provide detailed calorie breakdowns and assess the overall healthiness of the meal.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Deployed Application](https://huggingface.co/spaces/atharv20/caloriellm)
- [Screenshot]![calloriellm](https://github.com/user-attachments/assets/011cd9ee-951b-4e6e-9a25-9730a2f2bdbe)


## Features

- Upload an image of food items.
- Analyze the food items and calculate the total calories.
- Get a detailed breakdown of each food item's calorie content.
- Assess the overall healthiness of the meal based on its nutritional content.

## Prerequisites

- Python 3.7 or higher
- Streamlit
- Google Gemini API key

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/gemini-health-app.git
    cd gemini-health-app
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

5. Set up environment variables:

    Create a `.env` file in the root directory of the project and add your Google Gemini API key:

    ```plaintext
    GOOGLE_API_KEY=your_google_gemini_api_key
    ```

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Upload an image of food items and click "Tell me about the total calories" to analyze the image.

## Project Structure

```plaintext
gemini-health-app/
│
├── .env.example         # Example environment file
├── app.py               # Main Streamlit app
├── index.html           # HTML template for the app
├── styles.css           # CSS file for styling the app
├── script.js            # JavaScript file for client-side interactions
├── images/              # Directory for images
│   └── placeholder.jpg  # Placeholder image
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation


