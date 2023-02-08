# Ship rental assignment

Flask project containing API to optimize the profitability of a small rental company with a single spaceship to rent

The goal is to produce a list of contract names maximizing the profit. As there's only a single ship to rent there should not be any overlap between the accepted contracts and of course not all proposed contracts can be picked.


## API Reference

#### [POST] /spaceship/optimize
```bash
json_data = [
    {"name": "Contract1", "start": 0, "duration": 5, "price": 10},
    {"name": "Contract2", "start": 3, "duration": 7, "price": 14},
    {"name": "Contract3", "start": 5, "duration": 9, "price": 8},
    {"name": "Contract4", "start": 5, "duration": 9, "price": 7}]
```
#### Output
```bash
{
    "income": 18,
    "path": [
        "Contract1",
        "Contract3"
    ]
}
```

## Prerequisites

```Python 3.10```

## Dependencies
```
Flask
pytest
coverage
```

## Directory structure
```bash
ship_rental_assignment
├── application.py
├── env
├── flask_app
│   ├── __init__.py
│   ├── calculate_profit_archived.py
│   └── calculate_profit_service.py
├── readme.md
├── requirements.txt
└── tests
    ├── conftest.py
    └── test_shipping_optimize.py
```

## Run Locally

Clone the project

```bash
  git clone https://github.com/AkshayHartalkar/ship_rental_assignment.git
```

Go to the project directory

```bash
  cd ship_rental_assignment
```

Create virtual ENV

```bash
  python3 -m venv env
  source env/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python application.py
```

## Running Tests
To run tests;
after virtual ENV is activated, run the following command

```bash
  python -m pytest
```

Test output
```bash
===================================================== test session starts =====================================================
platform darwin -- Python 3.10.8, pytest-7.2.1, pluggy-1.0.0
rootdir: /path/ship_rental_assignment
collected 7 items                                                                                                             

tests/test_shipping_optimize.py .......                                                                                 [100%]

====================================================== 7 passed in 0.03s ======================================================
```


## Notes

- Developed on ```Python 3.10.8```
- API are not browsable API, please use a REST client to test POST api such as POSTman or Insomnia
- Core logic will be found under ship_rental_assignment/flask_app/calculate_profit_service.py