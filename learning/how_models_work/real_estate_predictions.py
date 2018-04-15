import pandas as pd

main_file_path = '../input/train.csv'
data = pd.read_csv(main_file_path)

# save filepath to variable for easier access
melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(main_file_path) 

# store the series of prices separately as melbourne_price_data.
#melbourne_price_data = melbourne_data.SalePrice
# the head command returns the top few lines of data.
#print(melbourne_price_data.head())

#select multiple columns
#columns_of_interest = ['GarageCars', 'YearBuilt']
#two_columns_of_data = melbourne_data[columns_of_interest]
#print(two_columns_of_data.describe())

# print a list of columns and a summary of the data in Melbourne data
print(melbourne_data.columns)
#print(melbourne_data.describe())

#import scikit-learn bits
from sklearn.tree import DecisionTreeRegressor
#choose target
y = melbourne_data.SalePrice
#choose predictors
melbourne_predictors = ['YearRemodAdd', 'LotArea', 'YearBuilt', 'Fireplaces']
x = melbourne_data[melbourne_predictors]
#define model
melbourne_model = DecisionTreeRegressor()
#fit model
melbourne_model.fit(x, y)

