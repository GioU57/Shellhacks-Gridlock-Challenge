@echo off
echo Setting up the Gridlock Challenge environment...

:: Check if the virtual environment directory already exists
IF NOT EXIST "venv\" (
    echo Creating virtual environment...
    python -m venv venv
)

:: Activate the virtual environment
call venv\Scripts\activate.bat

:: Install requirements
echo Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

:: Run the Streamlit application
echo Launching the Gridlock tool...
streamlit run app.py
pause