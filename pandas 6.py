import pandas as pd
df = pd.DataFrame()
print(df)

data = [1,2,3,4,5] 
df = pd.Dataframe(data)
print (df)

data = [['Alex', 10], ['bob',12], ['clarke',13]]
df = pd.DataFrame(data,columns=['Name', 'Age']) #dtype= float 
print(df)