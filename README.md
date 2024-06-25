# Getting Started with ollama-chatbot
This is a chatbot application built using Ollama and Streamlit. In this guide, we will walk you through the process of setting up and running the project on your local machine.

## Before You Begin 
To get started with this project, you will need to have the following tools installed on your machine:
- Python 3.11 [https://www.python.org/downloads/release/python-3110/](https://www.python.org/downloads/release/python-3110/)
- pip [https://pip.pypa.io/en/stable/installation/](https://pip.pypa.io/en/stable/installation/)
- Ollama [https://ollama.com/](https://ollama.com/)

## Setting Up the Project
1. Clone the repository: `git clone https://github.com/adhika16/ollama-chatbot.git`
2. Activate your virtual environment. If you haven't created one yet, you can create it using `python -m venv <venv_name>` and activate it based on your operating system:
    - On Windows:
        ```shell
        <venv_name>\Scripts\activate
        ```
    - On Unix or MacOS:
        ```bash
        source <venv_name>/bin/activate
        ```
3. Once the virtual environment is activated, use pip to install the dependencies listed in the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```
    - After installing the dependencies, you can verify that they were installed correctly by running: `pip list`
4. Run the following command to start the Streamlit application:
    ```bash
    streamlit run app.py
    ```
5. Open a web browser and navigate to `http://localhost:8501` to see the chatbot in action!