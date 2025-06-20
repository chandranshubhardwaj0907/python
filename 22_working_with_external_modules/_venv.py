#virtual environmnet is a self-contained directory that contains a Python installation for a particular version of Python, plus several additional packages.
# A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus several additional packages.'


# commands used are 
# python -m venv myenv
# myenv\Scripts\activate  # Windows 

# piplist 

# pip install upgrade pip  used when pip is not updated
# pip install requests  # Install a package

# pip install requests==2.25.1  # Install a specific version of a package
# pip install requests>=2.25.1  # Install a package with a minimum version
# pip install requests<=2.25.1  # Install a package with a maximum version
# pip install requests!=2.25.1  # Install a package excluding a specific version


# pip freeze > requirements.txt  # Export installed packages to a requirements file
# # pip install -r requirements.txt  # Install packages from a requirements file

# deactivate  # Deactivate the virtual environment



