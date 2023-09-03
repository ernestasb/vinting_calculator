# Vinting Calculator

### Description. 
A module created to parse file containing transaction information, validates it and applies rules.  
The code is written in python-3.10.12

### Packages
* pytest - package for testing tools
* poverage - package for test covevrage review

### How to run
The project was developed within 'pipenv' virtual environment.   
#### Run the project  
```pipenv sync``` - installs Pipfile.lock dependencies and creates virtual env.  
```pipenv shell``` - enters virtual env.  
```python main.py input.txt``` - runs the program which calls transaction calculation module and passes a file to it.  
#### Testing and coverage
```pytest``` - runs all the tests within the project  
```coverage html --omit="test/*" -d tests/coverage``` - runs the coverage and generates /tests/coverage/index.html for interactive view
## Project structure
<pre>
├── `Pipfile`  file containing required packages  
├── `Pipfile.lock`  file containing locked versions  
├── `README.md`  
├── `input.txt`  file containing input data  
├── `main.py`  file to call the module  
├── `module_config.json`  file containing module configs  
├── `modules`  directory containing modules (currently only calc module)  
│   ├── `errors.py`  file containing custom errors  
│   ├── `extensions.py`  file containing custom shhareable code snippets  
│   ├── `models.py`  file containing models (currently Transaction)  
│   └── `transaction_calc`  directory containinng transaction calculation files  
│       ├── `main.py`  file containing calculation logic (rule calls)  
│       └── `rules`  rules used by transaction calculator  
│           ├── `discount_limit.py`  discount limit rule  
│           ├── `free_shipping.py`  free shipping rule  
│           └── `lowest_shipping.py`  lowest shipping rule  
└── `tests`  directory containing tests  
    ├── `__init__.py`  
    ├── `conftest.py`  file containing shareable fixtures between tests/classes  
    ├── `coverage`  code coverage diirectory  
    │  ├── `...`  various coverage files  
    │  └── `index.html`  interactive HTML file to review coverage  
    ├── `functional`  directory containing functional tests  
    │   └── `test_transaction_calc.py`  calculation function tests  
    └── `unit`  directory containing unit tests  
        ├── `test_discount_limit.py`  
        ├── `test_free_shipping.py`  
        ├── `test_lowest_shipping.py`  
        └── `test_models.py`  
</pre>
        