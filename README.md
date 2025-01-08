# Dynamic Cold Email Generator

The **Dynamic Cold Email Generator** is an AI-powered tool designed to automate the creation of personalized cold emails for outreach campaigns. By leveraging advanced language models, the application crafts tailored email content based on user inputs, streamlining the outreach process and enhancing engagement rates.

## Key Features:

- **Personalized Email Generation**: Utilizes AI to create customized cold emails, improving the likelihood of recipient engagement.
- **User-Friendly Interface**: Built with Streamlit, the app offers an intuitive interface for seamless user interaction.
- **Integration with Vector Databases**: Employs vector databases to efficiently manage and retrieve relevant information, ensuring contextually accurate email content.
- **Environment Variable Management**: Incorporates the `python-dotenv` library to securely handle environment variables, maintaining the confidentiality of sensitive information.

## Technologies Used:

- **Streamlit**: A framework for building interactive web applications in Python.
- **Llama3.1**: An open-source large language model utilized for generating human-like text.
- **Vector Databases**: Databases optimized for storing and querying vector embeddings, enhancing the app's ability to process and retrieve information.
- **python-dotenv**: A Python library for reading key-value pairs from `.env` files and setting them as environment variables, ensuring secure management of sensitive data.

## Installation:

1. Clone the repository:
   
2. Install the required dependencies:
   pip install -r requirements.txt
   
3. Set up environment variables:
   Create a .env file in the root directory of the project.
   Add the necessary environment variables (e.g., API keys, database URLs) to the .env file.

4. Run the application:
   streamlit run app/main.py
           or
   python -m streamlit run app/main.py


Usage:
1. Open the application in your web browser.
2. Input the necessary details for the cold email generation.
3. Click on the "Generate Email" button to receive a personalized cold email draft.
4. Review and edit the generated email as needed before sending it.


