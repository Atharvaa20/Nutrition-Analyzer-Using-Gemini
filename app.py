from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Configure Google Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Pro Vision API and get response
def get_gemini_response(input_prompt, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_prompt, image[0]])
    return response.text

# Function to handle uploaded image
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Health App", page_icon="🍎")

# Add custom CSS styles
st.markdown(
    """
    <style>
    body {
        background-color: gray;
        font-family: 'Arial', sans-serif;
    }
    .big-font {
        font-size: 34px;
        font-weight: bold;
    }
    .small-font {
        font-size: 16px;
    }
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    .upload-button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add header and description
st.markdown('<p class="big-font centered">Gemini Health App</p>', unsafe_allow_html=True)
st.markdown('<p class="small-font centered">Analyze the nutritional content of your meals by uploading a photo.</p>', unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Display uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Submit button
submit = st.button("Tell me about the total calories", key="submit_button",)

# Input prompt for the API
input_prompt = """
You are a nutrition expert. Analyze the food items in the provided image and calculate the total calories. Provide a detailed breakdown of each food item and its calorie content in the following format:

Item 1 - Number of calories
Item 2 - Number of calories
...
...
Finally, assess and mention whether the overall meal is healthy or not based on its nutritional content.
"""

# If submit button is clicked
if submit:
    try:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(input_prompt, image_data)
        st.subheader("The Response is")
        st.write(response)
    except FileNotFoundError:
        st.error("Please upload a file before submitting.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
