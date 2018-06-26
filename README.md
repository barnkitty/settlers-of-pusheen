# settlers-of-pusheen

//description should go here, eventually

# (Windows) DevEnv Setup / Install Guide

1.  Install [Python3](https://www.python.org/downloads/)
2.  Install [Pycharm Community Edition](https://www.jetbrains.com/pycharm/download/)
    * Install the Markdown plugin (makes editing this file easy-ish)
3. Update `pip`
    1. Launch a command prompt (`WIN + R` -> `cmd`)
    2. Navigate in the command prompt to the directory where you installed python3
    3. `python -m pip install -U pip`
4. Setup personal virtual environment for this project (jic the one Katja initially set up doesn't work)
    1. Install [virtualenv](https://virtualenv.pypa.io/en/stable/) using `pip install virtualenv`
    2. Using the terminal at the bottom of pycharm
        `virtualenv v_env` 
        (gitignore is set to ignore the directory at v_env)
5. Install [Django](https://www.djangoproject.com/download/) using the virtual environment's pip
    1. In pycharm's terminal, launch v_env/Scripts/activate 
        * this will change your command line to be executing the python of the virtual environment
        * as well as the doing pip installs to that location
    2. `pip install Django==2.0.6`
    3. Verify install
        1. in pycharms terminal, launch python
        2. check django version
        
        ```python
           import django
           print(django.get_version())
        ```
6. Check that the dev server runs successfully
    1. cd to project root (settlers-of-pusheen)
    2. launch dev server
        * `python manage.py runserver`
        * if this prints out "something something something starting dev server at xxx"
    3. check the science / muckery page
        * navigate in browser to <ip_goes_here>:<port_goes_here>/science/
        * if this results in a depressed basic looking hello world page.  You're done (for now)