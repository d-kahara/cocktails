## Cocktails API

[![Continous Integration](https://github.com/d-kahara/cocktails/actions/workflows/main.yml/badge.svg)](https://github.com/d-kahara/cocktails/actions/workflows/main.yml)

The API documentation can be found here: https://cocktails-dev-api.herokuapp.com/swagger/


## Set Up Development With Docker (Preferred setup)

1. Download Docker from [here](https://docs.docker.com/)
2. Set up an account to download Docker
3. Install Docker after download
4. Go to your terminal run the command `docker login`
5. Input your Docker email and password

To setup for development with Docker after cloning the repository please do/run the following commands in the order stated below:

-   `cd <project dir>` to check into the directory
-   `make build` to build the application images
-   `make run` to run the api after the previous command is successful

The `make build` command builds the docker image where the api and its postgres database would be situated.
Also this command does the necessary setup that is needed for the API to connect to the database.

The `make run` command starts the application 



### Alternative Development set up

-   Check that python 3 is installed:

    ```
    python --version
    >> Python 3.8.*
    ```


-   Check pip3 is installed:
    ```
    pip3 --version
    >> pip 21.1.1 from /some-path/
    ```
-   Check that postgres is installed:

    ```
    postgres --version
    >> postgres (PostgreSQL) 12.1
    ```

-   Clone the edge-backend repo and cd into it:

    ```
    git clone https://github.com/d-kahara/cocktails.git
    ```

-   Install dependencies:

    ```
    pip install -r requirements.txt
    ```


-   Make a copy of the .env.sample file and rename it to .env and update the variables accordingly:

    ```
    DJANGO_DEBUG=True
    DATABASE_URL='postgresql://postgres:@backend:5432/edge'
    SECRET_KEY='secret_key_here'
    DJANGO_SETTINGS_MODULE='cocktails.settings'
    ```

-   Activate a virtual environment:

    ```
    python -m venv env
    source env/bin/name-of-virtual-env
    ```

-   Apply migrations:

    ```
    make migrate
    ```

*   Run the application with either commands:

    ```
    python manage.py runserver
    ```

    or

    ```
    make serve
    ```

*   Should you make changes to the database models, run migrations as follows

    -   Migrate database:

        ```
        make migrations
        ```

    -   Upgrade to new structure:
        ```
        make migrate
        ```

*   Deactivate the virtual environment once you're done:
    ```
    deactivate
    ```





## Running tests and generating report

On command line run:

```
pytest
```



