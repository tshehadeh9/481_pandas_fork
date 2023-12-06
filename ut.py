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
print(df1.dtypes['A'])


# df = pd.DataFrame({'A': [1, 2, 3], 'B': [400, 500, 600]})
# new_df = pd.DataFrame({'B': [4, 5, 6], 'C': [7, 8, 9]})
# df.update(new_df)
# df
import numpy as np
import pytest

import pandas.util._test_decorators as td

import pandas as pd
from pandas import (
    DataFrame,
    Series,
    date_range,
)
import pandas._testing as tm

@pytest.mark.parametrize('dtype', ['int8', 'int16', 'int32', 'int64', 'string', 'datetime', 'float'])
def test_update_perserves_dtypes(dtype):

	#test ints
	if dtype == 'int8':
		df1 = pd.DataFrame([[1, 2, 3]], columns=["A", "B","C"], dtype="Int64")
		df2 = pd.DataFrame([[4, 5, 6]], columns=["A", "B", "C"], dtype="Int64")
		df1.update(df2)
		assert df1.dtypes["A"] == df2.dtypes["A"]
		assert df1.dtypes["B"] == df2.dtypes["B"]
		assert df1.dtypes["C"] == df2.dtypes["C"]

	if dtype == 'int16':
		df1 = pd.DataFrame([[1, 2, 3]], columns=["A", "B","C"], dtype="int16")
		df2 = pd.DataFrame([[4, 5, 6]], columns=["A", "B", "C"], dtype="int16")
		df1.update(df2)
		assert df1.dtypes["A"] == df2.dtypes["A"]
		assert df1.dtypes["B"] == df2.dtypes["B"]
		assert df1.dtypes["C"] == df2.dtypes["C"]

	if dtype == 'int32':
		df1 = pd.DataFrame([[1, 2, 3]], columns=["A", "B","C"], dtype="int32")
		df2 = pd.DataFrame([[4, 5, 6]], columns=["A", "B", "C"], dtype="int32")
		df1.update(df2)
		assert df1.dtypes["A"] == df2.dtypes["A"]
		assert df1.dtypes["B"] == df2.dtypes["B"]
		assert df1.dtypes["C"] == df2.dtypes["C"]

	if dtype == 'int64':
		df1 = pd.DataFrame([[1, 2, 3]], columns=["A", "B","C"], dtype="int64")
		df2 = pd.DataFrame([[4, 5, 6]], columns=["A", "B", "C"], dtype="int64")
		df1.update(df2)
		assert df1.dtypes["A"] == df2.dtypes["A"]
		assert df1.dtypes["B"] == df2.dtypes["B"]
		assert df1.dtypes["C"] == df2.dtypes["C"]

	if dtype == 'string':
		df1 = pd.DataFrame([['thomas', '481', 'cool']], columns=["A", "B","C"], dtype="string")
		df2 = pd.DataFrame([['hello', 'goodbye', 'beatles']], columns=["A", "B","C"], dtype="string")
		df1.update(df2)

		assert df1.dtypes["A"] == df2.dtypes["A"]
		assert df1.dtypes["B"] == df2.dtypes["B"]
		assert df1.dtypes["C"] == df2.dtypes["C"]

	if dtype == 'datetime':
		df1 = pd.DataFrame([[pd.Timestamp('20180310'), pd.Timestamp('20190410'), pd.Timestamp('20200810')]], columns=["A", "B","C"], dtype="datetime64[ns]")
		df2 = pd.DataFrame([[pd.Timestamp('20140610'), pd.Timestamp('20110411'), pd.Timestamp('20220817')]], columns=["A", "B","C"], dtype="datetime64[ns]")

		df1.update(df2)

		assert df1.dtypes["A"] == df2.dtypes["A"]
		assert df1.dtypes["B"] == df2.dtypes["B"]
		assert df1.dtypes["C"] == df2.dtypes["C"]	#test strings

	if dtype == 'float':
		df1 = pd.DataFrame([[1.0, 2.4242, 3.1111]], columns=["A", "B","C"], dtype="float64")
		df2 = pd.DataFrame([[4.4, 5.0, 6.123]], columns=["A", "B", "C"], dtype="float64")
		df1.update(df2)

		assert df1.dtypes["A"] == df2.dtypes["A"]
		assert df1.dtypes["B"] == df2.dtypes["B"]
		assert df1.dtypes["C"] == df2.dtypes["C"]
	#test lists





# def test_update_with_different_dtype(self, using_copy_on_write):
#     # GH#3217
#     df = DataFrame({"a": [1, 3], "b": [np.nan, 2]})
#     df["c"] = np.nan
#     if using_copy_on_write:
#         df.update({"c": Series(["foo"], index=[0])})
#     else:
#         df["c"].update(Series(["foo"], index=[0]))

#     expected = DataFrame({"a": [1, 3], "b": [np.nan, 2], "c": ["foo", np.nan]})
#     tm.assert_frame_equal(df, expected)