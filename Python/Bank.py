import pandas as pd

#------------------------------
# Downloading Raw Data
df= pd.read_csv("../Data/Churn_Modelling.csv")
print ("Before cleaning:",df.shape)

#------------------------------
#Explore Data
print("\n Missing Value :")
print(df.isnull().sum())

print("\n Duplicate Rows:")
print(df.duplicated().sum())

print("\nDuplicate Customer IDs:")
print(df["CustomerId"].duplicated().sum())

print("\nData Types:")
print(df.dtypes)

#------------------------------
# Remove dublication
before = df.shape[0]
df= df.drop_duplicates()
after = df.shape[0]
print (f"Duplicate rows were deleted: {before -after }")

#------------------------------
#Delete duplicate customers based on CustomerId
#(If the same customer has more than one row by mistake)
before = df.shape[0]
df= df.drop_duplicates(subset ="CustomerId" ,keep="first")
after = df.shape[0]
print (f" duplicate customers(CustomerId) were deleted: {before -after }")

#------------------------------
#Handling null values ​​(if any)
# Our strategy: Important numeric columns -> We delete the row
# (Here there is no NULL at all, but the code is ready for any new data)
before = df.shape[0]
df= df.dropna(subset=["CustomerId","Balance", "Age", "CreditScore"])
after = df.shape[0]
print (f" Rows deleted due to NULL in primary columns: {before -after }")

#------------------------------
#Uniformity in text column formatting (removing extra spaces, adding letter colors)
# Very important if the data comes from different sources containing "France" or "france"
df["Geography"] = df["Geography"].str.strip().str.title()
df["Gender"] = df["Gender"].str.strip().str.title()


#------------------------------
df.to_csv("../Data/Bank_clean.csv", index=False)
print("\nShape after cleaning:", df.shape)
print("saved Data/Bank_clean.csv")
