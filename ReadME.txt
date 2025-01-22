How to implement the Project:
1. Setting Up the Environment:

Download the project zip file: Locate and download the compressed file containing the project code.
Extract the zip file: Use a decompression tool like unzip on Linux/Mac to extract the files from the downloaded zip.
Activate the virtual environment: we created a virtual environment named venv using python -m venv venv, activate it with the appropriate command for your operating system (e.g., source venv/bin/activate on Linux/Mac or venv\Scripts\activate on Windows).


2. Running the Application:

Navigate to the project directory: Use the cd command in your terminal to navigate to the folder containing the extracted project files.
Run the api.py file: Assuming the main application script is named api.py, execute it using python api.py. This will start the Flask development server.
Open the provided port in your browser: The terminal output when running api.py should display a message indicating the server is running on a specific port (e.g., "http://127.0.0.1:5000"). Open this URL in your web browser to access the application's user interface.


3. Using the User Interface:

Analyze Sentiment: The interface likely provides a text field where you can enter a review or multiple reviews . Click a button labeled "Analyze Sentiment" the text for analysis.
Sentiment Score: The application should process the submitted text and display a sentiment score as a numerical value. This score might represent high number to low number.

4. Accessing Reviews :

Reviews Endpoint: This application allows exploring existing reviews, it has a dedicated endpoint. Try adding /reviews to the end of the base URL (e.g., "http://127.0.0.1:5000/reviews"). This will display a list of reviews or provides access to them in JSON format.

