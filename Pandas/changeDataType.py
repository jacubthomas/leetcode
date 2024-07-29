import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students = students.astype({'grade': int})
    # OR 
    # students['grade'] = students[['grade']].astype(int) # changing datatype to int.
    # return students
    return students