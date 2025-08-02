import pickle
import streamlit as st
import pandas as pd

# NEW IMPORTS for Graph
import matplotlib.pyplot as plt
import networkx as nx


# ------------------ Existing Recommender Function ------------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        # fetch poster from API (commented out since not used here)
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# ------------------ NEW: Graph Building Function ------------------
def build_similarity_graph(selected_movie, top_n=5):
    index = movies[movies['title'] == selected_movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:top_n + 1]

    G = nx.Graph()
    G.add_node(selected_movie)

    for i in distances:
        title = movies.iloc[i[0]]['title']
        score = round(i[1], 2)
        G.add_node(title)
        G.add_edge(selected_movie, title, weight=score)

    fig = plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G, k=0.5)
    weights = nx.get_edge_attributes(G, 'weight')

    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
    plt.title(f"Top {top_n} Similar Movies to '{selected_movie}'")

    return fig


# -------------------------------------------------------------------

# Load movie data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit UI
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations =  recommend(selected_movie_name)

    st.subheader('Recommended Movies:')
    for i in recommendations:
        st.write(i)

    # NEW: Display Graph
    st.subheader('Graph Visualization of Similar Movies')
    fig = build_similarity_graph(selected_movie_name)
    st.pyplot(fig)
