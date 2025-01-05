# Deep Opinion

To take a look at some code, I'd like to propose a small practical project. The idea is to 
develop a Flask application with the following specifications:

**Main functionality:**
A simple HTML page collects 3 inputs from the user:
- A string identifier.
- Two positive integers: integer_1 and integer_2.

The application returns a list of even integers between these two integers.

**Example:**
If the user enters 1 and 8, the application returns [2, 4, 6, 8].

**Data storage :**
The following data must be stored in a database or structure such as a dataframe:
- The identifier
- The generated list

**Attention to user input:**
Entries must be validated (for example: check that integers are positive, handle cases where 
integer_1 > integer_2, etc.).

**Deliverables:**
- Comment your code to make it readable and self-explanatory.
- Update your Git repository with your project. I'll take a look! 

**Database:**
The database has been created with the file: `database.py`.

Verify the data inside the deep_opinion.db-database in terminal:

    sqlite3 deep_opinion.db
    sqlite> .open deep_opinion.db
    sqlite> select username, result_list from user_results;
    TestUser|[2, 4, 6, 8, 10, 12]
    Dean|[4]
    Nelly|[2, 4, 6, 8]
    sqlite> .quit

For a more detailed approach, use the following:

    sqlite3 deep_opinion.db
    sqlite> .open deep_opinion.db
    sqlite> .tables
    user_results
    sqlite> pragma table_info(user_results);
    0|id|INTEGER|0||1
    1|username|TEXT|1||0
    2|result_list|TEXT|1||0
    sqlite> select username, result_list from user_results;
    TestUser|[2, 4, 6, 8, 10, 12]
    Dean|[4]
    Nelly|[2, 4, 6, 8]
    sqlite> .quit

**Installation:**

Clone the GitHub repository with: 
```
$ git clone https://github.com/DoriDoro/DeepOpinion.git
$ cd DeepOpinion
```

Create a SECRET_KEY with command: <br>
`$ make generate_secret_key` <br>
and add the SECRET_KEY in a `.env` file on root directory.

Create a virtual environment on Linux machine: <br>
```
$ python3 -m venv .venv
$ .venv/bin/activate
```

Install all dependencies: <br>
`$ pip install -r requirements.txt`

Start the development server: <br>
`$ make server`
