"""System module."""

def is_year_leap(year):
    """Calcula si un anio determinado es bisiesto"""
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

def days_in_month(year, month):
    """Retorna la cantidad de dias en el mes dado un anio y numero de mes"""
    no_year_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    is_leap = is_year_leap(year)
    #print()
    #print("Year ", year, " is ", is_leap)

    if is_leap == True:
        for i in range(len(no_year_leap)):
            if i == month and month == 2:
                return (no_year_leap[1] + 1)
            elif i == month and i != 2:
                return no_year_leap[month-1]
    else:
        return no_year_leap[month-1]
    
  
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print("year month")
    print(yr, mo, "-> ", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK", end=" cantidad dias: ")
        print(result)
    else:
        print("Fallido", end=" cantidad dias: ")
        print(result)
    print()
