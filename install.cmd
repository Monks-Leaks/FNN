@echo off
REM Install required Python packages

REM Make sure you have Python and pip installed
REM You can download Python from https://www.python.org/downloads/
REM pip is usually installed by default with Python

REM List of packages to install
set packages=requests,colorama,schedule,discord,Pillow,app_commands,datetime,tweepy

REM Loop through the packages and install them
for %%p in (%packages%) do (
    pip install %%p
)

echo.
echo Installation completed. Press any key to exit.
pause > nul
