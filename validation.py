import re
from datetime import date


def email_check(email):

    pattern=r'^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w+$'

    return re.match(
    pattern,email
    )


def dob_check(dob):

    return dob <= date.today()