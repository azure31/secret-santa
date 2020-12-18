import random
import pandas as pd
import streamlit as st


def generate_secretIds(names):
    df = pd.DataFrame({'name': names})
    secretIds = random.sample(range(100000, 1000000), len(df))
    df['secretId'] = secretIds
    print(df)
    df = df.reset_index()
    df.to_csv("santa_data.csv", index=False)


def assign_santas():
    df = pd.read_csv("santa_data.csv")
    indexes = list(range(len(df)))
    while True:
        random.shuffle(indexes)
        if not sum(df.index == indexes):
            break
    df['giftee'] = indexes
    df.to_csv("post_santa_data.csv", index=False)
    st.markdown("Assignment Done. Ho ho ho! 🎅")
    return df


def find_giftee(secretId):
    df = pd.read_csv("post_santa_data.csv")
    if not secretId in df['secretId'].values:
        st.warning("Incorrect secret Id. Try again!")
    else:
        idx = df[df.secretId == secretId].index.tolist()[0]
        st.markdown(f"### Hello, {df.at[idx, 'name']} 👋")
        giftee = df.at[idx, 'giftee']
        st.markdown("You have to gift * *drumroll* * ")
        st.markdown(f"### {df.at[giftee, 'name']}!")
        st.balloons()


st.title("ADDA Secret Santa 2020")

if st.button("Assign santa-giftee pairs"):
    df = assign_santas()

secretId = st.number_input("Enter your secretId:")
if st.button("Find my giftee!"):
    find_giftee(secretId)
