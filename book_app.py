import pandas as pd
import pickle
import numpy as np
import streamlit as st
st.set_page_config(layout="wide")
st.title('BOOK RECOMMENDATION ENGINE')

def recommend(book_name):
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)[1:7]

    data = []
    a = []
    b = []
    c = []
    for i in similar_items:
        item = []
        p=i[0]
        temp_df = new_book[new_book['title'] == pt.index[p]]
        item.extend(list(temp_df.drop_duplicates('title')['title'].values))
        item.extend(list(temp_df.drop_duplicates('title')['authors'].values))
        item.extend(list(temp_df.drop_duplicates('title')['image_url'].values))
        data.append(item)
    for i in range(0, 6):
        a.append([data[i][0]])
        b.append([data[i][1]])
        c.append([data[i][2]])
    return a, b, c

def PopularityBased():
    result = sorted_dataset['title'][:10]
    poster = sorted_dataset['image_url'][:10]
    author = sorted_dataset['authors'][:10]
    return result, poster, author

book_dataset = pickle.load(open('books_df1.pkl', 'rb'))
books = pd.DataFrame(book_dataset)
similarity = pickle.load(open('similarity.pkl', 'rb'))
sorted_dataset = pickle.load(open('sorted_data.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
book_new = pickle.load(open('books_new.pkl', 'rb'))
new_book = pd.DataFrame(book_new)

st.subheader('Select a book: ')
option = st.selectbox('Following Books are available', books['title'].values)

if st.button('Get Recommendations'):
    st.header('Recommending 6 books based on your selection')
    t, a, i = recommend(option)
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    with col1:
        st.image(i[0])
        st.caption(t[0])
        st.caption(a[0])
        st.write('\n')
    with col2:
        st.image(i[1])
        st.caption(t[1])
        st.caption(a[1])
        st.write('\n')
    with col3:
        st.image(i[2])
        st.caption(t[2])
        st.caption(a[2])
        st.write('\n')
    with col4:
        st.image(i[3])
        st.caption(t[3])
        st.caption(a[3])
        st.write('\n')
    with col5:
        st.image(i[4])
        st.caption(t[4])
        st.caption(a[4])
        st.write('\n')
    with col6:
        st.image(i[5])
        st.caption(t[5])
        st.caption(a[5])
        st.write('\n')

st.write('\n\n\n\n')


st.header("HAVE A LOOK AT THE TOP 10 MOST POPULAR BOOKS")
names, posters, author = PopularityBased()
col0, col1, col2, col3, col4 = st.columns(5)
col5, col6, col7, col8, col9 = st.columns(5)
with col0:
    st.image(posters[0])
    st.caption(names[0])
    st.caption(author[0])
    st.write('\n')
with col1:
    st.image(posters[1])
    st.caption(names[1])
    st.caption(author[1])
    st.write('\n')
with col2:
    st.image(posters[2])
    st.caption(names[2])
    st.caption(author[2])
    st.write('\n')
with col3:
    st.image(posters[3])
    st.caption(names[3])
    st.caption(author[3])
    st.write('\n')
with col4:
    st.image(posters[4])
    st.caption(names[4])
    st.caption(author[4])
    st.write('\n')
with col5:
    st.image(posters[5])
    st.caption(names[5])
    st.caption(author[5])
    st.write('\n')
with col6:
    st.image(posters[6])
    st.caption(names[6])
    st.caption(author[6])
    st.write('\n')
with col7:
    st.image(posters[7])
    st.caption(names[7])
    st.caption(author[7])
    st.write('\n')
with col8:
    st.image(posters[8])
    st.caption(names[8])
    st.caption(author[8])
    st.write('\n')
with col9:
    st.image(posters[9])
    st.caption(names[9])
    st.caption(author[9])
    st.write('\n')
