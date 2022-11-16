# Scrapper
Scrapper Youtube

Author : Cabrera Matthieu
Mail : cabreramat@cy-tech.fr
Version: 1.0.0

# Execution Context : 
To run this project, you must intall Python 3.8 at least
You can use venv environment to isolate the execution, 
but having some troubles I used anaconda
Of course, you'll need to install Beautiful Soup and pytest-cov


# Execution :
You can run the main code using the command
    python scrapper.py --input input.json --output output.json

You can launch the tests using : 
    python -m pytest tests

You can run the test with the coverage : 
    pytest --cov=. tests/

# Execution Results

You can find the result of the execution of the program in the file you put in argument, so in the output.json file.

You can change the file 'input.json' to change the youtube links sources, but some test may failed cause they're attached to the existing ids.