import streamlit as st
from recommend import recommend,product_list

st.set_page_config(page_title="Market Basket Recommendation", layout="centered")

st.title("🛒 Market Basket Recommendation System")
st.write("Select a frequent product to get recommendations.")


# Select Product

product = st.selectbox("Select Product:", product_list)


# Recommendation Button
if st.button("Recommend"):

    recommendations = recommend(product)

    if not recommendations:
        st.warning("No recommendations found for this product.")
    else:
        st.success("Customers also bought:")
        for item in recommendations:
            st.write("•", item)
