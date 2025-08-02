# 🎬 Movie Recommendation System

[![Streamlit App](https://img.shields.io/badge/Streamlit-Deployed-success?logo=streamlit&logoColor=white&color=FF4B4B)](#)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](#license)

> 🚀 A content-based movie recommender powered by **Python**, **scikit-learn**, and **Streamlit** — with an interactive graph visualization of similar movies!

---

# 📖 Overview

This project recommends movies similar to a selected one using **cosine similarity** on movie metadata from the [TMDB 5000 Movies Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).

The recommender is deployed as an **interactive web app** with:
- 🔍 **Searchable movie dropdown**
- 🎯 **Top-5 similar movies list**
- 📊 **Graph network visualization** showing movie similarity

---

## ✨ Features

✅ **Content-based filtering** (no user history required)  
✅ **Natural Language Processing**: Bag-of-Words + stemming for better matching  
✅ **Interactive Streamlit UI**  
✅ **Graph visualization** using `networkx` + `matplotlib`  
✅ **Deployed-ready** (load from pickled model artifacts)  


---

## 📂 Dataset

**Source**: [TMDB 5000 Movies Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)  
Files used:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

**Important**: You need to download these CSV files and place them in the project root before running the notebook.

---

## 🛠️ Technologies Used

- **Python 3.8+**
- **Pandas** — Data manipulation  
- **scikit-learn** — Vectorization & similarity  
- **NLTK** — Text preprocessing (stemming)  
- **Streamlit** — Web app UI  
- **Matplotlib** + **NetworkX** — Graph visualization  

---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
2️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
Tip: If you don't have requirements.txt yet, create one:

bash
Copy
Edit
pip freeze > requirements.txt
3️⃣ Prepare the dataset
Download and place:

tmdb_5000_movies.csv

tmdb_5000_credits.csv

in the root folder.

4️⃣ Generate model artifacts
Run the Jupyter notebook to preprocess data and save:

bash
Copy
Edit
jupyter notebook Movie_Recommendation_System.ipynb
This will generate:

movie_dict.pkl

similarity.pkl

5️⃣ Run the Streamlit app
bash
Copy
Edit
streamlit run Streamlit_app.py
📌 Usage Guide
Select a movie from the dropdown.

Click "Recommend".

View:

📃 List of top-5 similar movies

📈 Graph visualization of similarity relationships

📊 How It Works
Data Preprocessing

Merge movies and credits datasets

Extract genres, keywords, cast, and crew

Clean and normalize text

Feature Engineering

Combine features into tags

Apply Bag-of-Words (CountVectorizer)

Apply Porter stemming

Similarity Computation

Calculate cosine similarity between movies

Recommendation

Rank movies by similarity score

Return top-5 matches

🤝 Contributing
Contributions are welcome!
To contribute:

Fork the repo

Create a new branch:

bash
Copy
Edit
git checkout -b feature/your-feature
Commit your changes:

bash
Copy
Edit
git commit -m "Add your feature"
Push to your branch and create a Pull Request

📜 License
This project is licensed under the MIT License.

📬 Contact
👤 Afzal Shah
📧 Email: syedafzal.career59@gmail.com
💼 LinkedIn: https://www.linkedin.com/in/afzal-shah-ai-engineer
🐙 GitHub: https://github.com/syed-afzal-shah

⭐ If you like this project, give it a star on GitHub!
🙌 Your support helps make this project better.
