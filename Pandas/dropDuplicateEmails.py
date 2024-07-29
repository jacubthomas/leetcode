'''
DataFrame.drop_duplicates(subset=None, *, keep='first', inplace=False, ignore_index=False)[source]
Return DataFrame with duplicate rows removed.

Considering certain columns is optional. Indexes, including time indexes are ignored.

Parameters:
subsetcolumn label or sequence of labels, optional
Only consider certain columns for identifying duplicates, by default use all of the columns.

keep{‘first’, ‘last’, False}, default ‘first’
Determines which duplicates (if any) to keep.

‘first’ : Drop duplicates except for the first occurrence.

‘last’ : Drop duplicates except for the last occurrence.

False : Drop all duplicates.

inplacebool, default False
Whether to modify the DataFrame rather than creating a new one.

ignore_indexbool, default False
If True, the resulting axis will be labeled 0, 1, …, n - 1.'''

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset='email', keep='first')