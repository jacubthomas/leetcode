import pandas as pd
from typing import List

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
    # return employees[0:3]
    # return employees.truncate(0, 2)