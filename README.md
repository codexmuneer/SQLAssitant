# SQLAssitant

# Instructions to run this project  <br />
  Git clone https://github.com/codexmuneer/SQLAssitant.git  <br />
  Open any IDE you like.  <br />
  In terminal create and activate virtual environment using these commands  <br />
  python3 -m venv venv  <br />
  venv\Scripts\activate  <br />
  install all requirements using  <br />
  pip install --ignore-installed -r requirements.txt  <br />
  run app using uvicorn main:app --reload  <br />

# Note:  <br />
 add your openAi key in .env file  <br />
 create database using any name in pgadmin   <br />
 add your PSQL server password in database.py file  <br />
   'postgresql://postgres:passHERE@localhost:5432/databasename'  <br />

# Working:  <br />
step 1 - to populate db with random values  <br />
  post request to http://127.0.0.1:8000//init-db  <br />
step 2 - to chat with chatbot  <br />
  post request to http://127.0.0.1:8000//process-prompt  <br />
   with this json data example  <br />
{
    "input" : "find all prices for trades in database"
}
example output should be like this  <br />
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


