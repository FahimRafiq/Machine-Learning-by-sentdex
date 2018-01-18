import pandas as pd

df = pd.DataFrame(
    {
        "a" : [1,3,5],
        "b" : [7,4,5]
    },
    index = [1,2,3]
)

# print(df)

df02 = pd.DataFrame(
    [[0,4,5],
    [2,5,6],
    [4,5,6]],
    index = [0,1,3],
    columns= ['a','b','c']
)

# df02.rename(columns = {"a":"z"},inplace = True)


print(df.head())




