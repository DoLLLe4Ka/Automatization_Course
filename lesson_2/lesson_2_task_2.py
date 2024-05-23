def is_year_leap(year):
    if year % 4 == 0:
         print("год", year,":", True)
    else:
         print("год", year,":", False)
is_year_leap(2020)
is_year_leap(2026)