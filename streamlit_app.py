import streamlit as st
import random
st.title("おみくじアプリ")

if st.button("おみくじを引く"):
     results = ["大吉","大吉","大吉","大貴ょう"]
     result = random.choice(results)
     st.write(f"結果: {result}")