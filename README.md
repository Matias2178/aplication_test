# API REST application test
API REST whit Python flask and Postgresql

# Installation instructions
1. Create an Virtual environment

         python - m virtualenv env

2. Start virtual environment

    - linux

          source /bin/activate
    
    - windows

          source /venv/Scripts/activate

3. Install all used packages
    
         pip install -r Requeriments.txt

4. Create an .env file (in the root of the project) for the environment variables:

         ENV_USER_DB = 'User db'
         ENV_PASS_DB = 'Pasword db'
         ENV_URL_DB =  'location db'
         ENV_NAME_DB = 'Name db'
         ENV_SECRETS_KEY = 'Secret key'


PostgreSQL download: https://www.postgresql.org/download/
Insomnia download: https://insomnia.rest/download