# Checking package is succesfully created 
step 1:- create setup.py
step 2:- pip install .
step 3:- pip install --upgrade .
step 4:- pip uninstall [package-name]

# Create a package build
step 1:- pip install wheel
step 2:- python3 -m pip install --upgrade build
step 3:- python3 -m build

# Uploading package
step 1:- create a account on pypi(prod) or testpypi(test).
step 2:- python3 -m pip install --upgrade twine
step 3:- 
    Test Server
        python3 -m twine upload --repository testpypi dist/*
    Prod Server
        python3 -m twine upload --repository pypi dist/*

    You will be prompted for a username and password. For the username, 
    use __token__. For the password, use the token value.

versions:-
https://pypi.org/project/srivastav/0.0.1/
https://pypi.org/project/srivastav/0.0.2/