# recommend.py

import pandas as pd

# Load precomputed rules
rules = pd.read_csv("association_rules.csv")

# Convert string representation back to set
rules['antecedents'] = rules['antecedents'].apply(eval)
rules['consequents'] = rules['consequents'].apply(eval)

# Create product list from antecedents
product_list = sorted(
    set(item for sublist in rules['antecedents'] for item in sublist)
)

def recommend(product_name):
    matched_rules = rules[
        rules['antecedents'].apply(lambda x: product_name in x)
    ]
    
    recommendations = set()
    for cons in matched_rules['consequents']:
        for item in cons:
            recommendations.add(item)
    
    return list(recommendations)

print("Recommendation system is ready to use!")
