# Content-Based Movie Recommender System 🎬

This project implements a Content-Based Movie Recommender System using Streamlit, Python, and the TMDB API.

## Overview

The Content-Based Movie Recommender System suggests movies based on the similarity of their content. It utilizes the TMDB API to fetch movie details and posters.

## Methodology

1. **Data Collection:** Movie data is obtained from the [TMDB API](https://www.themoviedb.org/documentation/api). The dataset includes information such as movie titles, genres, and posters.

2. **Feature Extraction:** Features are extracted from the dataset, and a similarity matrix is computed based on these features. The similarity matrix helps identify movies with similar content.

3. **Streamlit Application:** The Streamlit web application allows users to select a movie from the dropdown menu. When the "Show Recommendations" button is clicked, the system provides personalized movie recommendations using the similarity matrix.

## Features

- Select a movie from the dropdown menu.
- Click the "Show Recommendations" button to get personalized movie recommendations.
- Recommendations are displayed with movie posters and titles in an interactive card layout.

## Prerequisites

Make sure you have the necessary libraries installed. You can install them using the following:

```bash
pip install streamlit requests
