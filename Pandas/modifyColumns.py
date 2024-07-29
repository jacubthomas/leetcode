import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] *= 2
    return employees
    # OR
    # return employees.mul({'name': 1, 'salary': 2})