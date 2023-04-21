# Step 1. Import the necessary libraries
import pandas as pd
# Step 2. Import the dataset from this address.
import_df = pd.read_csv('chipotle.tsv', delimiter='\t', header=0)
# Step 3. Assign it to a variable called chipo.
chipo = import_df
# Step 4. See the first 10 entries
print('Step 4. See the first 10 entries')
print(chipo.head(10))
# Step 5. What is the number of observations in the dataset?
print('Step 5. What is the number of observations in the dataset?')
print(len(chipo.index))
# Step 6. What is the number of columns in the dataset?
print('Step 6. What is the number of columns in the dataset?')
print(len(chipo.columns))
# Step 7. Print the name of all the columns.
print('Step 7. Print the name of all the columns.')
for column in chipo.columns:
    print(column)
# Step 8. How is the dataset indexed?
print('Step 8. How is the dataset indexed?')
print(chipo.index)
# Step 9. Which was the most-ordered item?
print('Step 9. Which was the most-ordered item?')
most_ordered = str(chipo.item_name.value_counts()[:1].index.to_list()[0])
print('Most-ordered item:', most_ordered)
# Step 10. For the most-ordered item, how many items were ordered?
print('Step 10. For the most-ordered item, how many items were ordered?')
print('Number of times', most_ordered, 'was ordered:', chipo.item_name.value_counts()[:1].to_list()[0])
# Step 11. What was the most ordered item in the choice_description column?
print('Step 11. What was the most ordered item in the choice_description column?')
most_ordered = str(chipo.choice_description.value_counts()[:1].index.to_list()[0])
print('Most-ordered item:', most_ordered)
# Step 12. How many items were ordered in total?
print('Step 12. How many items were ordered in total?')
print('Number of times', most_ordered, 'was ordered:', chipo.choice_description.value_counts()[:1].to_list()[0])
# Step 13.
# • Turn the item price into a float
# • Check the item price type
# • Create a lambda function and change the type of item price
# • Check the item price type
print("Step 13\n"
      "• Turn the item price into a float\n"
      "• Check the item price type\n"
      "• Create a lambda function and change the type of item price\n"
      "• Check the item price type")
for i in range(len(chipo.index)):
    chipo.at[i, 'item_price'] = str(chipo.at[i, 'item_price']).replace('$', '')
chipo.item_price = chipo.item_price.astype(float)
print('dtype of item_price:', chipo.item_price.dtype)
# Step 14. How much was the revenue for the period in the dataset?
print('Step 14. How much was the revenue for the period in the dataset?')
revenue = list()
for i in range(len(chipo.index)):
    revenue.append(float(chipo.at[i, 'quantity']) * chipo.at[i, 'item_price'])
print(round(sum(revenue), 2))
# Step 15. How many orders were made in the period?
print('Step 15. How many orders were made in the period?')
print(len(chipo.order_id.unique()))
# Step 16. What is the average revenue amount per order?
print('Step 16. What is the average revenue amount per order?')
print(round(round(sum(revenue), 2)/len(chipo.order_id.unique()), 2))
# Step 17. How many different items are sold?
print('Step 17. How many different items are sold?')
print(len(chipo.item_name.unique()))
