import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Load data
df = pd.read_csv("cleaned_market.csv")

# Create transactions
# create group of only invoice no and extract description as a list then from it only extract values!!
transactions = df.groupby('invoiceno')['description'].apply(list).values.tolist()

# Transaction Encoding
te = TransactionEncoder() # make te strong enough to encode the transactions
te_array = te.fit(transactions).transform(transactions) # fit() → learn the unique items  transform() → encode the transactions into a boolean array
basket = pd.DataFrame(te_array, columns=te.columns_) # te.columns_ → get the unique items as column names

# Apriori
frequent_itemsets = apriori(
                                basket, 
                                min_support=0.01, 
                                use_colnames=True)

# Extract only single-item frequent products
single_items = frequent_itemsets[
                                frequent_itemsets['itemsets']     #get unique single items 
                                .apply(lambda x: len(x) == 1)      #{bread,milk} len->2 false
                                                                    #{bread} len->1 true
                            ]

# Convert frozenset → string
product_list = sorted(
    single_items['itemsets'].apply(lambda x: list(x)[0])  # {bread} → bread
)

# Association Rules
rules = association_rules(
                            frequent_itemsets, 
                            metric="confidence", 
                            min_threshold=0.05)
rules.to_csv("association_rules.csv", index=False)