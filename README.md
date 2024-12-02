# Deep Opinion

To take a look at some code, I'd like to propose a small practical project. The idea is to 
develop a Flask application with the following specifications:

**Main functionality:**
A simple HTML page collects 3 inputs from the user:

    A string identifier.
    Two positive integers: integer_1 and integer_2.

The application returns a list of even integers between these two integers.

**Example:**
If the user enters 1 and 8, the application returns [2, 4, 6, 8].

**Data storage :**
The following data must be stored in a database or structure such as a dataframe:

    The identifier
    The generated list

**Attention to user input:**
Entries must be validated (for example: check that integers are positive, handle cases where 
integer_1 > integer_2, etc.).

**Deliverables:**
- Comment your code to make it readable and self-explanatory.
- Update your Git repository with your project. I'll take a look! 