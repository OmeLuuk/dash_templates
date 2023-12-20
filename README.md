# dash_templates
Python Dash templates for building simple Dash apps

# Quick start steps (Windows):
1. Check if Python is installed on your machine; open a terminal and execute `python --version` or `python3 --version`
2. If you get an error indicating that your computer doesn't know what to do with this command, download and install Python for windows from https://www.python.org/downloads/release/python-3121/
3. Create and start a virtual environment to keep our project isloated and make our environment reproducable: execute `python -m venv .venv` and then `.venv\Scripts\activate` in your terminal. Make sure that you do everything in your terminal in your virtual environment, which you can check by observing that it says (.venv) before your command line, like so `(.venv) PS D:\dev\dash_templates>`
4. If you get an error in step 3 saying running scripts is disabled on this system, execute `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` and then try running `.venv\Scripts\activate` again
5. Install dash: execute `pip install dash dash-renderer dash-html-components dash-core-components plotly`
