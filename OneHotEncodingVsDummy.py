import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 50)
# pd.set_option('display.width', 1000)

# Define the headers since the data does not have any
headers = ["symboling", "normalized_losses", "make", "fuel_type", "aspiration",
           "num_doors", "body_style", "drive_wheels", "engine_location",
           "wheel_base", "length", "width", "height", "curb_weight",
           "engine_type", "num_cylinders", "engine_size", "fuel_system",
           "bore", "stroke", "compression_ratio", "horsepower", "peak_rpm",
           "city_mpg", "highway_mpg", "price"]

# Read in the CSV file and convert "?" to NaN
df = pd.read_csv("C:\Himanshu\Data.txt",
                 header=None, names=headers, na_values="?")
# print(df.dtypes)

obj_df = df.select_dtypes(include=['object'])

# print(obj_df.isnull().any())

# print(obj_df['num_doors'].isnull().sum())

# print(obj_df['num_doors'].value_counts())

obj_df = obj_df.fillna({"num_doors": "four"})

# print(obj_df['num_doors'].isnull().sum())

# ************************************************************************

# Approach 1 Find and replace

# print(obj_df["num_cylinders"].value_counts())

# print(obj_df["num_doors"].value_counts())

# print(obj_df.loc[:10,['num_doors','num_cylinders']])

cleanup_nums = {"num_doors": {"four": 4, "two": 2},
                "num_cylinders": {"four": 4, "six": 6, "five": 5, "eight": 8,
                                  "two": 2, "twelve": 12, "three": 3}}

# print(type(cleanup_nums))

# print(type(obj_df))

obj_df.replace(cleanup_nums, inplace=True)

# print(obj_df[['num_doors', 'num_cylinders']].head())

# ************************************************************************

# Approach #2 - Label zr

obj_df['body_style'] = obj_df['body_style'].astype('category')

# print(obj_df['body_style'])

# print(obj_df.dtypes)

obj_df["body_style_cat"] = obj_df['body_style'].cat.codes

# print(obj_df.head())


# ************************************************************************

# Approach #3 - One Hot Encoding

obj_df = pd.get_dummies(obj_df, columns=["body_style", "drive_wheels"], prefix=["body", "drive"]).head(4)

print(obj_df)


# ************************************************************************

# Approach #4 - Custom Binary Encoding

obj_df["OHC_Code"] = np.where(obj_df["engine_type"].str.contains("ohc"), 1,0)

#obj_df["OHC_Code"] = np.where(obj_df["engine_type"].str.contains("ohc"),1,other=0)
#print(obj_df)
