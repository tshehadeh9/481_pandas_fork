import pandas as pd
print(pd.__version__)
df1 = pd.DataFrame([[1, 2, 3]], columns=["A", "B","C"], dtype="Int64")
# df1.dtypes returns:
# A    Int64
# B    Int64
# C    Int64
# dtype: object
df2 = pd.DataFrame([[4, 5, 6]], columns=["A", "B", "C"], dtype="Int64")
# df2.dtypes returns:
# A    Int64
# B    Int64
# C    Int64
# dtype: object
df1.update(df2)
# df1 returns
#    A  B  C
# 0  4  5  6
# and df1.dtypes returns
# A    object
# B    object
# C    object
# dtype: object
print(df1)
print("-------")
print(df1.dtypes)