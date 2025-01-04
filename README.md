# SummaryGenie - AI Document Summarizer

SummaryGenie is an AI-powered tool designed to automatically summarize large documents, making it easier to grasp essential information in a matter of seconds. Built with Python, Flask, and modern front-end technologies, this tool provides an intuitive and responsive interface for users to input text and receive a summary instantly.

## Features
+ Summarize Documents: Paste or type large blocks of text, and SummaryGenie will generate concise and coherent summaries.
+ Summary History: View a history of all previous summaries for reference.
+ Modern & Aesthetic UI: Clean, intuitive, and responsive design for a seamless user experience.
+ Easy to Use: Just enter text and hit "Summarize" to get the summary.

# Tech Stack

## Frontend
+ HTML5: For structuring the web pages.
+ CSS3: For styling the web pages and creating a responsive layout.
+ JavaScript: For interacting with the backend and updating the UI dynamically.

## Backend
+ Python: Used to write the core functionality of the document summarization engine.
+ Flask: Lightweight web framework to serve the frontend and handle requests.
+ Sumy Library: Text summarization library used to summarize documents.
+ Git: Version control for code management and collaboration.

# Installation

## Prerequisites
To run this project locally, you need to have the following installed:

+ Python: Version 3.x
+ Pip: Package manager for Python
+ Git: For version control and pushing code to GitHub

## Setup
Follow these steps to set up and run the project on your local machine:

- Clone the Repository: Open your terminal or command prompt and run the following command to clone the repository:


- git clone https://github.com/Adityaps234/SummarryGenie.git
Navigate to the Project Folder: After cloning, go to the project directory:


>  cd SummarryGenie
Create a Virtual Environment (Optional but recommended): It's a good practice to use a virtual environment to manage dependencies. To create and activate a virtual environment, run:


python -m venv venv
# On Windows
> .\venv\Scripts\activate
- Install Dependencies: Install all necessary Python packages using pip:


- pip install -r requirements.txt

This will install the following dependencies:

Flask
Sumy
etc.
Run the Application: After installing the dependencies, run the Flask application:


> python app.py
This will start the development server. Open your web browser and go to http://127.0.0.1:5000/ to view the application.

# How to Use
1. Input Text: Paste or type the document/text you want to summarize into the text area.

2. Summarize: Click on the "Summarize" button, and the application will generate a concise summary of the input text.

3. View Summary History: As you summarize more documents, a history of all the previous summaries will be displayed on the left side, allowing you to refer back to them.

# Project Structure
Here’s an overview of the project structure:


SummarryGenie/
│
├── backend/
│   ├── app.py                # Flask application file
│   ├── requirements.txt      # Project dependencies
│   ├── summarizer.py         # Core text summarization logic
│   └── ...
│
├── frontend/
│   ├── index.html            # Main HTML file for the UI
│   ├── style.css             # Custom styles for the frontend
│   ├── script.js             # JavaScript to handle frontend logic
│   └── ...
│
└── README.md                 # Project documentation (this file)

# Contribution Guidelines
We welcome contributions to improve SummaryGenie! If you want to contribute, follow these steps:

# Fork the repository.
* Create a new branch (git checkout -b feature-name).
* Make your changes.
* Commit your changes (git commit -m 'Add new feature').
* Push to your forked repository (git push origin feature-name).
* Open a pull request to merge your changes into the main repository.

# License
This project is open source and available under the MIT License. See the LICENSE file for more information.

# Acknowledgments
* Sumy Library for text summarization.
* Flask for providing the backend framework.
* All open-source contributors who helped make this project possible.