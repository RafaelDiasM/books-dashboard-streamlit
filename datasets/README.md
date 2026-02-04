# Interactive Dashboard for Book and Review Analysis

This project is an **interactive web dashboard** developed in **Python** to analyze best-selling books and customer reviews, using datasets from Kaggle.

The application allows users to explore prices, popularity, publication year, and customer feedback through clear and intuitive visualizations.

---

## Preview
![Dashboard](assets/dashboard.png)

---

## Features
- Visualization of the **Top 100 most popular books**
- Filtering books by **price range**
- Analysis of **book prices and publication years**
- Exploration of **customer reviews**
- Interactive charts using **Plotly**
- Multi-page navigation with **Streamlit**

---

## Project Structure

- **app.py**  
  Main Streamlit application file. Responsible for loading datasets, applying filters, and displaying interactive tables and charts.

- **pages/**  
  Contains the dashboard pages:
  - `visao_geral.py`: customer reviews overview
  - `analise_precos.py`: price analysis
  - `book_reviews.py`: combined analysis of books and reviews

- **data/**  
  Datasets used in the project:
  - `customer reviews.csv`
  - `Top-100 Trending Books.csv`

---

## Technologies Used
- Python
- Streamlit
- pandas
- Plotly

---

##  How to Run the Project

```bash
git clone https://github.com/your-username/dashboard-livros-streamlit.git
cd dashboard-livros-streamlit
pip install -r requirements.txt
streamlit run app.py
