DATABASE_CONFIG = {
    'host': '10.138.0.6',
    'port': 3306,
    'user': 'curw',
    'password': 'curw@123',
    'db': 'curw'
}

SOURCES = [
    'FLO2D',
    'HEC-HMS',
    'wrf0',
    'wrf1',
    'wrf2',
    'wrf3'
]

FORECAST_DAYS = {
    'FLO2D': 2,
    'HEC-HMS': 5,
    'wrf0': 2,
    'wrf1': 2,
    'wrf2': 2,
    'wrf3': 2
}

EMAIL_SERVER_CONFIG = {
    'host': 'smtp.gmail.com',
    'port': 587,
    'user-name': 'curwalerts@gmail.com',
    'password': 'curwalerts@data'
}

RECIPIENT_LIST = [
    'thilina.11@cse.mrt.ac.lk',
    'srikantha.herath@gmail.com',
    'gihan.09@cse.mrt.ac.lk',
    'lahikos@gmail.com',
    'niranda.17@cse.mrt.ac.lk'
]

NO_ALERT_MESSAGE = """The gap between the 
    1. last recorded end_date (%s) and
    2. the current data (%s)
is more than or equal to %d days."""

ALERT_MESSAGE = """The gap between the 
    1. last recorded end_date (%s) and 
    2. the current date (%s) 
is NOT more than %d days."""

EMAIL_ALERT_TEMPLATE = """
Hi,

%s

Please look into the data inconsistency issue at %s and proceed as necessary.

Thanks,
curwalerts.
"""
