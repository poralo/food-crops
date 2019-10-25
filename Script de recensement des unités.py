import pandas

dataframe = pandas.read_csv("FeedGrains.csv")

UnitList = []

for index, row in dataframe.iterrows():
    column_value = row['SC_Unit_Desc']
    print("Column_value : ", column_value)
    if column_value not in UnitList:
        UnitList.append(column_value)
print(UnitList)

