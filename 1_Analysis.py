import pandas as pd
df=pd.read_csv('Travel.csv')
df
df.describe()

#------------------------------------------------------------------------

# A

# Age distribution
df['Age'].value_counts().plot(kind='hist')

# Age vs. product purchase
df.groupby('Age')['ProdTaken'].value_counts().unstack().plot(kind='bar')

#------------------------------------------------------------------------

#B

# Group by contact type and calculate purchase rate
purchase_rate = df.groupby('TypeofContact')['ProdTaken'].mean()
print(purchase_rate)

#------------------------------------------------------------------------

#C

# Check correlation between city tier and income
correlation = df['CityTier'].corr(df['MonthlyIncome'])
print(correlation)

#------------------------------------------------------------------------

#D

# Average pitch duration for purchase and no purchase
purchased = df[df['ProdTaken'] == True]['DurationOfPitch'].mean()
not_purchased = df[df['ProdTaken'] == False]['DurationOfPitch'].mean()
print(f"Purchased: {purchased}, Not Purchased: {not_purchased}")

#------------------------------------------------------------------------

#E

# Occupation distribution
df['Occupation'].value_counts().plot(kind='pie')

# Occupation vs. product purchase
purchase_by_occupation = df.groupby('Occupation')['ProdTaken'].mean()
print(purchase_by_occupation.sort_values(ascending=False))

#------------------------------------------------------------------------

#F

# Group by gender and product pitched, then calculate percentages
product_pitched_gender = df.groupby(['Gender', 'ProductPitched']).size().unstack().apply(lambda x: x / x.sum() * 100, axis=1)
print(product_pitched_gender)

#------------------------------------------------------------------------

#G

# Group by number of trips and calculate purchase rate
purchase_by_trips = df.groupby('NumberOfTrips')['ProdTaken'].mean()
print(purchase_by_trips)

#------------------------------------------------------------------------

#H

# Group by passport ownership and calculate average trips/purchase rate
passport_groups = df.groupby('Passport')
avg_trips_passport = passport_groups['NumberOfTrips'].mean()
purchase_rate_passport = passport_groups['ProdTaken'].mean()
print(f"Average Trips: {avg_trips_passport}, Purchase Rate: {purchase_rate_passport}")

#------------------------------------------------------------------------

#I

# Group by satisfaction score and calculate purchase rate
purchase_by_satisfaction = df.groupby('PitchSatisfactionScore')['ProdTaken'].mean()
print(purchase_by_satisfaction)

#------------------------------------------------------------------------

#J

# Filter customers with children
with_children = df[df['NumberOfChildrenVisiting'] > 0]

# Group by number of children and calculate purchase rate
purchase_by_children = with_children.groupby('NumberOfChildrenVisiting')['ProdTaken'].mean()
print(purchase_by_children)

#------------------------------------------------------------------------

#K

# Group by gender and product pitched, then calculate percentages
product_pitched_gender = df.groupby(['Gender', 'ProductPitched']).size().unstack().apply(lambda x: x / x.sum() * 100, axis=1)
print(product_pitched_gender)