> python -m venv venv
> venv\Scripts\activate
> pip install pymongo faker jsonschema python-dotenv
> pip install jsonschema
> pip freeze > requirements.txt
> pip install -r requirements.txt
> pip freeze > installed_packages.txt for /F "tokens=*" %i in (installed_packages.txt) do pip uninstall -y %i
