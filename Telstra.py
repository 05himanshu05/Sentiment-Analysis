import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb



# Setting pandas column width for better visibility
from matplotlib.cm import cmap_d

pd.set_option("display.max_rows", 20)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)

log_feature = pd.read_csv('C:\\Himanshu\\Tesla Network\\telstra-recruiting-network\\log_feature.csv')
resource_type = pd.read_csv('C:\\Himanshu\\Tesla Network\\telstra-recruiting-network\\resource_type.csv')
severity_type = pd.read_csv('C:\\Himanshu\\Tesla Network\\telstra-recruiting-network\\severity_type.csv')
event_type = pd.read_csv('C:\\Himanshu\\Tesla Network\\Data_used\\event_type.csv')
train_data = pd.read_csv('C:\\Himanshu\\Tesla Network\\telstra-recruiting-network\\train.csv')


# data_aggregated_4cols = pd.DataFrame().empty

# print(train_data.dtypes, end="\n\n")
# print(train_data.describe())

# def predict():
    # logic here

def _graph_analysis(data_df):
    # print(data_df.head(5))
    data_df_new = data_df[["id", "severity_num", "event_num", "location_num"]]
    data_df_new["location_num"] = data_df_new["location_num"].astype(int)
    print(data_df_new.head(5))
    print(data_df_new.dtypes)

    "correlating all columns(multi-dim corr)"
    # plt.interactive(False)
    # plt.figure()
    # data_df_new.boxplot()
    # plt.show()

    # df = pd.DataFrame(data_df_new)
    # df["severity_num"].plot(kind = "hist")
    # plt.show()

    "plotting correlation graph"
    df = pd.DataFrame(data_df_new)
    corr = df.corr()
    # plt.figure()
    f, ax = plt.subplots(figsize=(9,8))
    sb.heatmap(corr, ax=ax, cmap="YlGnBu", linewidths=0.1)
    plt.show()

def _init_eda():
    temp = event_type[["id", "event_type"]].sort_values(by="id", ascending=False)
    # print(temp)
    temp_2 = temp.drop(index=31170)

    # changing object to int for id field
    temp_2["id"] = temp_2["id"].astype(int)

    temp_3 = temp_2.merge(resource_type, on="id")

    temp_4 = log_feature.merge(temp_3, on="id")

    temp_5 = train_data.merge(temp_4, on="id")

    data_aggregated = severity_type.merge(temp_5, on="id")
    # print(data_aggregated)

    # Data with only following fields -
    # id, severity_tyoe and event_type

    # global data_aggregated_4cols = pd.DataFrame().empty
    data_aggregated_4cols = data_aggregated[["id", "severity_type", "event_type", "location"]]
    # print(data_aggregated_4cols, end="\n\n")
    # print(data_aggregated_4cols.info())

    "categorical to numerical"
    # data_2 = pd.get_dummies(data_aggregated_4cols, columns=["severity_type", "event_type"])
    # print(data_2.info())

    # data_aggregated_4cols["severity_type"].cat.codes
    #print(data_aggregated_4cols.head(5))

    "separating severity_type and number"
    severity = data_aggregated_4cols["severity_type"].str.split(" ", n=1, expand=True)
    data_aggregated_4cols["severity_num"] = severity[1]
    print(data_aggregated_4cols)
    "separating event_type and number"
    event = data_aggregated_4cols["event_type"].str.split(" ", n=1, expand=True)
    data_aggregated_4cols["event_num"] = event[1]

    "separating location and number"
    #location = data_aggregated_4cols["location"].str.split(" ", n=1, expand=True)
    #data_aggregated_4cols["location_num"] = location[1]
    #print(data_aggregated_4cols)

    "changing object type for severity and event to int"
    #severity_num_int = data_aggregated_4cols["severity_num"] = data_aggregated_4cols["severity_num"].astype(int)
    #event_num_int = data_aggregated_4cols["event_num"] = data_aggregated_4cols["event_num"].astype(int)
    #data_aggregated_4cols["severity_int"] = severity_num_int
    #data_aggregated_4cols["event_int"] = event_num_int
    print(data_aggregated_4cols, end="\n\n")
    # print(data_aggregated_4cols.dtypes, end="\n\n\n")

    # data_new_1 = data_aggregated_4cols[""]

    # print(data_aggregated_4cols["severity_num"].unique, end="\n\n")
    # print(data_aggregated_4cols["event_num"].unique, end="\n\n")

    "get unique severity types"
    severity_types_unique = pd.Series(data_aggregated_4cols["severity_num"]).unique()
    # et_u = pd.Series(severity_types_unique).unique()
    # print(severity_types_unique, end="\n\n")

    "get unique event types"
    event_types_unique = pd.Series(data_aggregated_4cols["event_num"]).unique()
    # print(event_types_unique, end="\n\n")
    # print(pd.Series.sort_values(event_types_unique, axis=0))
    # print(type(event_types_unique))
    # print(np.sort(event_types_unique), end="\n\n")
    # print(pd.value_counts(event_types_unique), end="\n\n")
    # print(event_types_unique)

    "get unique location and counts"
    location_unique = pd.Series(data_aggregated_4cols["location_num"]).unique()
    # print(np.sort(location_unique), end="\n\n")
    # print(pd.Series(location_unique).count())

    #_graph_analysis(data_aggregated_4cols)

    # data_aggregated_4cols["severity_type"] = data_aggregated_4cols["severity_type"].astype()
    # # # data_aggregated_4cols["event_type"] = data_aggregated_4cols["event_type"].astype("category")
    # # data_aggregated_4cols.dtypes

    # plt.interactive(False)
    # plt.figure()
    # data_aggregated_4cols.boxplot()
    # plt.show()


if __name__ == '__main__':
    _init_eda()
    # _graph_analysis(tra)
