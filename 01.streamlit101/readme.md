# Streamlit User Interface Project

This project demonstrates the use of Streamlit to create a simple user interface with various features. It consists of two main Python files: `app.py` and `session.py`.

## app.py

This file creates a Streamlit application with the following features:

- A sidebar with a welcome message and an image
- Two tabs: "User Information" and "Usage Preferences"
- User information input fields (email and password)
- Usage preference options (account type, timeout duration, CV upload)
- A save button that stores user information in a JSON file
- Displays a success message and validity period after saving

### Key Features:
- User input collection
- File upload functionality
- Dynamic content based on user input
- Data persistence (saving to a file)

### Additional Features (Currently Commented Out):
- Examples of various text display methods (write, markdown, header, subheader, code, LaTeX)
- Multimedia display (image, video, audio)
- Different input types (number input, slider, radio buttons)
- Two-column layout example

These commented-out sections provide examples of additional Streamlit features that can be easily implemented or experimented with.

## session.py

This file demonstrates the use of Streamlit's session state mechanism:

- Reads data from a CSV file
- Displays a table with a configurable number of rows
- Provides buttons to increase or decrease the number of rows shown
- Uses session state to maintain the row count between reruns

### Key Features:
- Session state management
- Dynamic table display
- Callback functions for button interactions

## How to Run

1. Ensure you have Streamlit and pandas installed:
   ```
   pip install streamlit pandas
   ```

2. Run the applications using:
   ```
   streamlit run app.py
   streamlit run session.py
   ```

## Note

This project is designed to showcase various Streamlit features and is primarily for educational purposes. It demonstrates how to create interactive web applications with Python using the Streamlit framework. The commented-out sections in `app.py` provide additional examples and can be uncommented to explore different Streamlit functionalities.