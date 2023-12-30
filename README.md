# SQLAssitant

# Instructions to run this project
  Git clone https://github.com/codexmuneer/SQLAssitant.git
  Open any IDE you like.
  In terminal create and activate virtual environment using these commands
  python3 -m venv venv
  venv\Scripts\activate
  install all requirements using
  pip install --ignore-installed -r requirements.txt
  run app using uvicorn main:app --reload

# Note:
 add your openAi key in .env file
 create database using any name in pgadmin
 add your PSQL server password in database.py file 
   'postgresql://postgres:passHERE@localhost:5432/databasename'

# Working:
step 1 - to populate db with random values
  post request to http://127.0.0.1:8000//init-db 
step 2 - to chat with chatbot
  post request to http://127.0.0.1:8000//process-prompt
   with this json data example
{
    "input" : "find all prices for trades in database"
}
example output should be like this
[
    {
        "price": 593.5690166390249
    },
    {
        "price": 495.822109095448
    },
    {
        "price": 367.3668440139093
    },
    {
        "price": 645.1729636074459
    },
    {
        "price": 37.9708160183728
    },
    {
        "price": 899.5025028511635
    },
    {
        "price": 181.16417314052308
    },
    {
        "price": 58.274088956189345
    },
    {
        "price": 58.36592501139507
    },
    {
        "price": 604.8497051696809
    }
]


