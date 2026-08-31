import pandas, seaborn, questionary
import matplotlib.pyplot as plt
from pathlib import Path

# Modifying some options for Pandas to display it better in VS Code terminal
pandas.set_option('display.max_columns', None)
pandas.set_option('display.max_rows', None)
pandas.set_option('display.width', 1000)

# path to the files in the folder
localDir = Path(__file__).parent
carDataPath = localDir / "car_dataset.csv"
sellerDataPath = localDir / "seller_dataset.csv"

# Loads the initial Data sets into variables
dfCarData = pandas.read_csv(str(carDataPath))
dfSellerData = pandas.read_csv(str(sellerDataPath))

# Prints first 5 rows of each dataset to check they loaded properly
def PrintFirst5():
    print(f"\nFirst 5 Rows of Car Dataset \n{dfCarData.head()}")
    print(f"\nFirst 5 Rows of Seller Dataset \n{dfSellerData.head()}\n\n")

# Function prints the duplicate count for both data sets
def CheckForDuplicates():
    print(f"\nFound {dfCarData.duplicated().sum()} duplicates in the car data")
    print(f"\nFound {dfSellerData.duplicated().sum()} duplicates in the seller data")

# Function prints the null count and columns with null counts + their count for both datasets
def CheckForNulls():
    carDataNullCount = dfCarData.isnull().sum().sum()
    sellerDataNullCount = dfSellerData.isnull().sum().sum()
    print(f"\nFound {carDataNullCount} null values in the car data \n")
    if carDataNullCount > 0:
        nulls = dfCarData.isnull().sum()
        print(nulls[nulls > 0].to_string())
    print(f"\nFound {sellerDataNullCount} null values in the seller data\n")
    if sellerDataNullCount > 0:
        nulls = dfSellerData.isnull().sum()
        print(nulls[nulls > 0].to_string())

# This function does the conversion by iterating through the column, extracting any numbers and then setting 
# The value to the extracted numbers, due to the column having a Dtype of str initially i cast it as object so that it doesnt
# Care what the actual type is then finally cast the column as an int64 - 64 bit integer
# Could have written it as a real function that takes in a dataframe and column name an returns the int but didnt find it
# Necessary for the assignment but would be a better approach if the dataset was variable or wanted a general function for it
def CarNumericalConversion():
    dfCarData["mileage"] = dfCarData["mileage"].astype("object")
    for i, value in dfCarData["mileage"].items():
        convertedNum = "".join(n for n in str(value) if n.isdigit())
        dfCarData.at[i, "mileage"] = int(convertedNum)
    dfCarData["mileage"] = dfCarData["mileage"].astype("Int64")
    dfCarData["num_of_doors"] = dfCarData["num_of_doors"].astype("object")
    for i, value in dfCarData["num_of_doors"].items():
        convertedNum = "".join(n for n in str(value) if n.isdigit())
        dfCarData.at[i, "num_of_doors"] = int(convertedNum)
    dfCarData["num_of_doors"] = dfCarData["num_of_doors"].astype("Int64")
    dfCarData["seating_capacity"] = dfCarData["seating_capacity"].astype("object")
    for i, value in dfCarData["seating_capacity"].items():
        convertedNum = "".join(n for n in str(value) if n.isdigit())
        dfCarData.at[i, "seating_capacity"] = int(convertedNum)
    dfCarData["seating_capacity"] = dfCarData["seating_capacity"].astype("Int64")
    dfCarData["fuel_consumption"] = dfCarData["fuel_consumption"].astype("object")
    for i, value in dfCarData["fuel_consumption"].items():
        convertedNum = "".join(n for n in str(value) if n.isdigit())
        dfCarData.at[i, "fuel_consumption"] = int(convertedNum)
    dfCarData["fuel_consumption"] = dfCarData["fuel_consumption"].astype("Int64")
    print(dfCarData.head())
    dfCarData.info()

def EngineFeatureSplit():
    dfCarData.insert(loc=10, column="type_of_engine", value=None)
    dfCarData.insert(loc=11, column="engine_capacity", value=None)

    for i in dfCarData.index:
        engineValue = dfCarData.at[i, "engine"]
        engineCapacity = "".join(n for n in str(engineValue) if n.isdigit() or n == ".")
        engineCapacity = float(engineCapacity) if engineCapacity else None
        dfCarData.at[i, "engine_capacity"] = engineCapacity
        if str(engineValue).lower().__contains__("petrol"):
            dfCarData.at[i, "type_of_engine"] = "Petrol"
        elif str(engineValue).lower().__contains__("diesel"):
            dfCarData.at[i, "type_of_engine"] = "Diesel"
        elif str(engineValue).lower().__contains__("hybrid"):
            dfCarData.at[i, "type_of_engine"] = "Hybrid"
        elif str(engineValue).lower().__contains__("electric"):
            dfCarData.at[i, "type_of_engine"] = "Electric"
        else:
            dfCarData.at[i, "type_of_engine"] = "Unknown"
    dfCarData["engine_capacity"] = dfCarData["engine_capacity"].astype("float")
    dfCarData["type_of_engine"] = dfCarData["type_of_engine"].astype("str")
    print(dfCarData.head(10))
    dfCarData.info()


EngineFeatureSplit()
CheckForNulls()








def MenuChoices() -> list[str]:
    choices = []
    choices.append("Print First 5 rows of each dataset")
    choices.append("Task 1A")
    choices.append("Task 1B")
    choices.append("Task 1C")
    choices.append("Task 1D")
    choices.append("Task 1E")
    choices.append("Task 2A")
    choices.append("Task 2B")
    choices.append("Task 3A")
    choices.append("Task 3B")
    choices.append("Task 3C")
    choices.append("Task 4A")
    choices.append("Task 4B")
    choices.append("Quit")
    return choices

if __name__ == "s":
    print(f"\n\n                       Data Analysis and Visualisation Assignment")
    print(f"\n                Uses Quesntionary to output specific data or visualisations\n\n")
    while True:
        choice = questionary.select("What task would you like done?", choices=MenuChoices()).ask()
        if choice is None:  # Ctrl-C
            break
        if choice == "Print First 5 rows of each dataset":
            PrintFirst5()
            choice = questionary.select("",choices=["Return", "Quit"]).ask()
            if choice == "Return":
                continue
            elif choice == "Quit":
                break
        elif choice == "Task 1A":
            CarNumericalConversion()
            choice = questionary.select("",choices=["Return", "Quit"]).ask()
            if choice == "Return":
                continue
            elif choice == "Quit":
                break            
        elif choice == "Task 1B":
            continue
        elif choice == "Task 1C":
            continue
        elif choice == "Task 1D":
            continue
        elif choice == "Task 1E":
            continue
        elif choice == "Task 2A":
            continue
        elif choice == "Task 2B":
            continue
        elif choice == "Task 3A":
            continue
        elif choice == "Task 3B":
            continue
        elif choice == "Task 3C":
            continue
        elif choice == "Task 4A":
            continue
        elif choice == "Task 4B":
            continue
        elif choice == "Quit":
            break




