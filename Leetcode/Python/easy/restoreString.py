#it uses pandas


# import pandas as pd
# import numpy as np
# df = pd.DataFrame({

#     'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],

#     'col2': [2, 1, 9, 8, 7, 4],

#     'col3': [0, 1, 9, 4, 2, 3],

#     'col4': ['a', 'B', 'c', 'D', 'e', 'F']

# })
# print(df)
# print(df.sort_values(by=['col1']))

# class Solution:
#     def __init__(self):
#         super().__init__()
#     def restoreString(self, s, indices):
#         import pandas as pd
#         temp=[]
#         for letter in s:
#             temp.append(letter)
#         st=''

#         df=pd.DataFrame({"col1":temp,"col2":indices})
#         df=df.sort_values(by="col2")
#         for letter in df["col1"]:
#             st=st+letter

#         return st
        

# print(Solution().restoreString("codeleet",[4,5,6,7,0,2,1,3]))
