# import numpy as np
# import pandas as pd
# import streamlit as st

# # Write a data frame
# st.write("Here's our first attempt at using data to create a table:")

# st.write(
#     pd.DataFrame(
#         {"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]}
#     )
# )

# dataframe = np.random.randn(10, 20)
# st.dataframe(dataframe)

# dataframe = pd.DataFrame(
#     np.random.randn(10, 20),
#     columns=('col %d' % i for i in range(20)))

# st.dataframe(dataframe.style.highlight_max(axis=0))

# dataframe = pd.DataFrame(
#     np.random.randn(10, 20), columns=("col %d" % i for i in range(20))
# )
# st.table(dataframe)

# # Draw a line chart
# chart_data = pd.DataFrame(
# np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)

# # plot a map of San Francisco
# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(map_data)

# # Widgets
# import streamlit as st
# x = st.slider('x')  # 👈 this is a widget
# st.write(x, 'squared is', x * x)

# import streamlit as st
# st.text_input("Your name", key="name")

# # You can access the value at any point with:
# st.session_state.name

# # Use checkboxes to show/hide data
# import streamlit as st
# import numpy as np
# import pandas as pd

# if st.checkbox('Show dataframe'):
#     chart_data = pd.DataFrame(
#        np.random.randn(20, 3),
#        columns=['a', 'b', 'c'])

#     chart_data

# # Use a selectbox for options
# import streamlit as st
# import pandas as pd

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
#     })

# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])

# 'You selected: ', option

# # Layout
# import streamlit as st

# # Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )

# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )

# import streamlit as st

# left_column, right_column = st.columns(2)
# # You can use a column just like st.sidebar:
# left_column.button('Press me!')

# # Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")

# # Show progress
# import streamlit as st
# import time

# 'Starting a long computation...'

# # Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)

# '...and now we\'re done!'

# # Session State
# import streamlit as st

# if "counter" not in st.session_state:
#     st.session_state.counter = 0

# st.session_state.counter += 1

# st.header(f"This page has run {st.session_state.counter} times.")
# st.button("Run it again")

# import streamlit as st
# import pandas as pd
# import numpy as np

# if "df" not in st.session_state:
#     st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

# st.header("Choose a datapoint color")
# color = st.color_picker("Color", "#FF0000")
# st.divider()
# st.scatter_chart(st.session_state.df, x="x", y="y", color=color)

# # Connections
import streamlit as st

conn = st.connection("my_database")
df = conn.query("select * from my_table")
st.dataframe(df)