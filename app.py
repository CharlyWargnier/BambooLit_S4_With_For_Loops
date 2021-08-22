import streamlit as st
import pandas as pd

# st.title('Counter Example using Callbacks with kwargs')
# st.stop()
# st.selectbox
# st.set_page_config(layout="wide")


def _max_width_():
    max_width_str = f"max-width: 1000px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )


st.title("🎋BambooLit 🎈")
st.text("[August 2021 Hackathon] An humble attempt to recreate BambooLit in Streamlit!")
st.text("")

data = [["randy", 10], ["thiago", 8], ["adrien", 9], ["marisa", 23]]
df = pd.DataFrame(data, columns=["Name", "Age"])

with st.expander("Check raw data", expanded=True):

    a, b, c = st.columns([1, 1, 1])

    with b:
        # st.write(df)
        st.table(df)
    # column1 = df["Age"]
    # column2 = df["Name"]

if "count" not in st.session_state:
    st.session_state.count = 0

if "count" not in st.session_state:
    st.session_state.count = 0


def increment_counter(increment_value=0):
    st.session_state.count += increment_value


def decrement_counter(decrement_value=0):
    st.session_state.count -= decrement_value


st.text("")
a, b, c, d = st.columns([1, 1, 0.3, 6])

with a:
    st.button("➕ step", on_click=increment_counter, kwargs=dict(increment_value=1))

with b:
    st.button("➖ step", on_click=decrement_counter, kwargs=dict(decrement_value=1))

with d:
    st.write("")
    st.write("Total steps = ", st.session_state.count)

# st.write("Count = ", st.session_state.count)
count = st.session_state.count

if count == 0:
    st.success("☝️ Start by adding a step!")
    st.stop()

elif count < 3:
    # c = 10
    # Create a range based on integer in counter
    cr = range(count)
    # Create a list based on count range
    l = [i for i in cr]
    # For loop based on list above
    for x in l:
        y = x + 10
        z = y + 10
        x = str(x)
        y = str(y)
        z = str(z)
        # button = st.button("Button " + x, key=x)
        a, b, c = st.columns([0.2, 0.4, 0.5])

        with a:
            selectbox1 = st.selectbox("Step " + x, ["Select", "Filter", "Sort"], key=x)

        with b:
            if selectbox1 == "Filter":
                selectbox2 = st.selectbox("Choose column", (df.columns), key=y)
            if selectbox1 == "Sort":
                selectbox2 = st.selectbox("Choose column", (df.columns), key=y)
            else:
                pass

        with c:
            if selectbox1 == "Filter":
                multiselect3 = st.multiselect("Multiselect", df[selectbox2], key=z)

            if selectbox1 == "Sort":
                multiselect3 = st.selectbox(
                    "Select sorting order", ["Ascending", "Descending"], key=z
                )
            else:
                pass

        if selectbox1 == "Filter":

            st.markdown("###")
            st.subheader("Check wrangled data!")

            df = df[df[selectbox2].isin(multiselect3)]

            a, b, c = st.columns([1, 1, 1])

            with b:

                st.table(df)

            st.subheader("Grab your code. Reuse anywhere! 👇🐍🔥")
            st.code(
                f"""

            import pandas as pd
            df = pd.read_csv("Add_your_file_name_here")
            df = df[df["{selectbox2}"].isin({multiselect3})] 
            print(df)

            """
            )

        if selectbox1 == "Sort":

            if multiselect3 == "Ascending":

                num_str = f'{"ascending=True"}'
                st.markdown("###")
                st.subheader("Check wrangled data!")
                df = df.sort_values(by=[selectbox2], ascending=True)
                a, b, c = st.columns([1, 1, 1])

                with b:

                    st.table(df)

            else:

                num_str = f'{"ascending=False"}'
                st.markdown("###")
                st.subheader("Check wrangled data!")
                df = df.sort_values(by=[selectbox2], ascending=False)
                a, b, c = st.columns([1, 1, 1])

                with b:

                    st.table(df)

            st.subheader("Grab your code. Reuse anywhere! 👇🐍🔥")
            st.code(
                f"""

            import pandas as pd
            df = pd.read_csv("### Add your file_name here")
            df.sort_values(by=["{selectbox2}"],{num_str})
            print(df)

            """
            )


else:
    st.warning("Only 2 steps for now, stay tuned!")

st.stop()

# if count == 0:
#     st.success("☝️ Start by adding a step!")
#     st.stop()
#
# elif count == 1:
#
#     a, b, c = st.columns([0.2, 0.4, 0.5])
#
#     with a:
#         selectbox1_1 = st.selectbox(
#             "Step #01", ["Select", "Filter 🔈", "Sort ♻️"], key="1"
#         )
#
#     with b:
#         if selectbox1_1 == "Filter 🔈":
#             selectbox1_2 = st.selectbox("Choose column", (df.columns), key="2")
#         if selectbox1_1 == "Sort ♻️":
#             selectbox1_2 = st.selectbox("Choose column", (df.columns), key="2")
#         else:
#             pass
#     with c:
#
#         if selectbox1_1 == "Filter 🔈":
#             multiselect1_3 = st.multiselect("Multiselect", df[selectbox1_2], key="3")
#
#         if selectbox1_1 == "Sort ♻️":
#             multiselect1_3 = st.selectbox(
#                 "Select sorting order", ["Ascending", "Descending"], key="3"
#             )
#         else:
#             pass
'''
    if selectbox1_1 == "Filter 🔈":

        st.markdown("###")
        st.subheader("Check wrangled data!")

        df = df[df[selectbox1_2].isin(multiselect1_3)]

        a, b, c = st.columns([1, 1, 1])

        with b:

            st.table(df)

        st.subheader("Grab your code. Reuse anywhere! 👇🐍🔥")
        st.code(
            f"""

        import pandas as pd
        df = pd.read_csv("Add_your_file_name_here")
        df = df[df["{selectbox1_2}"].isin({multiselect1_3})] 
        print(df)

        """
        )

    if selectbox1_1 == "Sort ♻️":

        if multiselect1_3 == "Ascending":

            num_str = f'{"ascending=True"}'
            st.markdown("###")
            st.subheader("Check wrangled data!")
            df = df.sort_values(by=[selectbox1_2], ascending=True)
            a, b, c = st.columns([1, 1, 1])

            with b:

                st.table(df)

        else:

            num_str = f'{"ascending=False"}'
            st.markdown("###")
            st.subheader("Check wrangled data!")
            df = df.sort_values(by=[selectbox1_2], ascending=False)
            a, b, c = st.columns([1, 1, 1])

            with b:

                st.table(df)

        st.subheader("Grab your code. Reuse anywhere! 👇🐍🔥")
        st.code(
            f"""

        import pandas as pd
        df = pd.read_csv("### Add your file_name here")
        df.sort_values(by=["{selectbox1_2}"],{num_str})
        print(df)

        """
        )

# elif count == 2:
# 
#     a, b, c = st.columns([0.2, 0.15, 0.5])
# 
#     with a:
#         selectbox1_1 = st.selectbox(
#             "Step #01", ["Select", "Filter 🔈", "Sort ♻️"], key="1"
#         )
#         selectbox2_1 = st.selectbox(
#             "Step #02", ["Select", "Filter 🔈", "Sort ♻️"], key="20"
#         )
# 
#     with b:
#         if selectbox1_1 == "Filter 🔈":
#             selectbox1_2 = st.selectbox("Choose column", (df.columns), key="2")
#         if selectbox1_1 == "Sort ♻️":
#             selectbox1_2 = st.selectbox("Choose column", (df.columns), key="2")
#         else:
#             pass
# 
#         if selectbox2_1 == "Filter 🔈":
#             selectbox2_2 = st.selectbox("Choose column", (df.columns), key="200")
#         if selectbox2_1 == "Sort ♻️":
#             selectbox2_2 = st.selectbox("Choose column", (df.columns), key="2000")
#         else:
#             pass
# 
#     with c:
# 
#         if selectbox1_1 == "Filter 🔈":
#             multiselect1_3 = st.multiselect("Multiselect", df[selectbox1_2], key="3")
# 
#         if selectbox1_1 == "Sort ♻️":
#             multiselect1_3 = st.selectbox(
#                 "Select sorting order", ["Ascending", "Descending"], key="3"
#             )
#         else:
#             pass
# 
#         if selectbox2_1 == "Filter 🔈":
#             multiselect2_3 = st.multiselect("Multiselect", df[selectbox2_2], key="30")
# 
#         if selectbox2_1 == "Sort ♻️":
#             multiselect2_3 = st.selectbox(
#                 "Select sorting order", ["Ascending", "Descending"], key="3000"
#             )
#         else:
#             pass

    if (selectbox1_1 == "Filter 🔈") and (selectbox2_1 == "Select"):

        st.markdown("###")
        st.subheader("Check wrangled data!")

        df = df[df[selectbox1_2].isin(multiselect1_3)]

        a, b, c = st.columns([1, 1, 1])

        with b:

            st.table(df)

        st.subheader("Grab your code. Reuse anywhere! 👇🔥")
        st.text("")
        st.code(
            f"""

        import pandas as pd
        df = pd.read_csv("Add_your_file_name_here")
        df = df[df["{selectbox1_2}"].isin({multiselect1_3})] 
        print(df)

        """
        )

    if (selectbox1_1 == "Sort ♻️") and (selectbox2_1 == "Select"):

        if multiselect1_3 == "Ascending":

            num_str = f'{"ascending=True"}'
        else:

            num_str = f'{"ascending=False"}'

        st.subheader("Grab your code. Reuse anywhere! 👇🐍🔥")
        st.code(
            f"""

        import pandas as pd
        df = pd.read_csv("### Add your file_name here")
        df.sort_values(by=["{selectbox1_2}"],{num_str})
        print(df)

        """
        )

    if selectbox1_1 == "Filter 🔈" and selectbox2_1 == "Filter 🔈":

        st.markdown("###")
        st.subheader("Check wrangled data!")
        df = df[df[selectbox1_2].isin(multiselect1_3)]
        df = df[df[selectbox2_2].isin(multiselect2_3)]
        a, b, c = st.columns([1, 1, 1])

        with b:

            st.table(df)

        st.subheader("Grab your code. Reuse anywhere! 👇🐍🔥")
        st.code(
            f"""

        import pandas as pd
        df = pd.read_csv("Add_your_file_name_here")
        df = df[df["{selectbox1_2}"].isin({multiselect1_3})] 
        df = df[df["{selectbox2_2}"].isin({multiselect2_3})] 
        print(df)

        """
        )

    if selectbox1_1 == "Filter 🔈" and selectbox2_1 == "Sort ♻️":

        if multiselect2_3 == "Ascending":

            num_str = f'{"ascending=True"}'

            st.markdown("###")
            st.subheader("Check wrangled data!")
            df = df[df[selectbox1_2].isin(multiselect1_3)]
            df = df.sort_values(by=[selectbox2_2], ascending=True)
            a, b, c = st.columns([1, 1, 1])

            with b:

                st.table(df)
        else:

            num_str = f'{"ascending=False"}'
            st.markdown("###")
            st.subheader("Check wrangled data!")
            df = df[df[selectbox1_2].isin(multiselect1_3)]
            df = df.sort_values(by=[selectbox2_2], ascending=False)
            a, b, c = st.columns([1, 1, 1])

            with b:

                st.table(df)

        st.subheader("Grab your code. Reuse anywhere! 👇🐍🔥")
        st.code(
            f"""

        import pandas as pd
        df = pd.read_csv("Add_your_file_name_here")
        df = df[df["{selectbox1_2}"].isin({multiselect1_3})] 
        df.sort_values(by=["{selectbox2_2}"],{num_str})
        print(df)

        """
        )

    if selectbox1_1 == "Sort ♻️" and selectbox2_1 == "Filter 🔈":

        if multiselect2_3 == "Ascending":

            num_str = f'{"ascending=True"}'

            st.markdown("###")
            st.subheader("Check wrangled data!")
            df = df.sort_values(by=[selectbox1_2], ascending=True)
            df = df[df[selectbox2_2].isin(multiselect2_3)]
            a, b, c = st.columns([1, 1, 1])

            with b:

                st.table(df)
        else:

            num_str = f'{"ascending=False"}'
            st.markdown("###")
            st.subheader("Check wrangled data!")
            df = df.sort_values(by=[selectbox1_2], ascending=False)
            df = df[df[selectbox2_2].isin(multiselect2_3)]
            a, b, c = st.columns([1, 1, 1])

            with b:

                st.table(df)

        st.subheader("Grab your code. Reuse anywhere! 👇🐍🔥")
        st.code(
            f"""

        import pandas as pd
        df = pd.read_csv("Add_your_file_name_here")
        df.sort_values(by=["{selectbox1_2}"],{num_str})
        df = df[df["{selectbox2_2}"].isin({multiselect2_3})] 
        print(df)

        """
        )

    if selectbox1_1 == "Sort ♻️" and selectbox2_1 == "Sort ♻️":
        st.warning("I've not worked on that combo yet. Stay tuned!")


else:
    st.warning("Only 2 steps for now, stay tuned!")


st.stop()

'''