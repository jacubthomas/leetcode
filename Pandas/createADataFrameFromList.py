import pandas as pd
from typing import List

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame.from_records(student_data)
    df.columns = ["student_id", "age"]
    return df

student_data = [[1,15],[2,11],[3,11],[4,20]]