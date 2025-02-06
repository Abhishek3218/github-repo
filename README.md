<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Netflix Clone</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background-color: #141414;
                color: white;
            }
            .navbar {
                display: flex;
                justify-content: space-between;
                padding: 20px;
                background-color: rgba(0, 0, 0, 0.7);
                position: fixed;
                width: 100%;
                z-index: 100;
            }
            .nav-items {
                display: flex;
                gap: 20px;
            }
            .nav-items a {
                color: white;
                text-decoration: none;
                font-size: 14px;
            }
            .hero-section {
                height: 100vh;
                background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('hero.jpg');
                background-size: cover;
                display: flex;
                flex-direction: column;
                justify-content: center;
                padding-left: 50px;
            }
            .hero-title {
                font-size: 48px;
                font-weight: bold;
                margin-bottom: 20px;
            }
            .hero-buttons {
                display: flex;
                gap: 10px;
            }
            .hero-buttons button {
                padding: 10px 20px;
                border: none;
                border-radius: 2px;
                font-size: 16px;
                cursor: pointer;
            }
            .content-section {
                padding: 20px;
            }
            .category {
                margin-bottom: 30px;
            }
            .category-title {
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 10px;
            }
            .movie-row {
                display: flex;
                gap: 10px;
                overflow-x: auto;
            }
            .movie-card {
                width: 200px;
                height: 300px;
                background-color: gray;
                display: flex;
                justify-content: center;
                align-items: center;
                flex-shrink: 0;
            }
        </style>
    </head>
    <body>
        <nav class="navbar">
            <div class="logo">NETFLIX</div>
            <div class="nav-items">
                <a href="#">Home</a>
                <a href="#">TV Shows</a>
                <a href="#">Movies</a>
                <a href="#">New & Popular</a>
                <a href="#">My List</a>
            </div>
        </nav>

        <section class="hero-section">
            <div class="hero-title">Featured Title</div>
            <div class="hero-buttons">
                <button>Play</button>
                <button>My List</button>
            </div>
        </section>

        <section class="content-section">
            <div class="category">
                <div class="category-title">Trending Now</div>
                <div class="movie-row">
                    <div class="movie-card">Movie 1</div>
                    <div class="movie-card">Movie 2</div>
                    <div class="movie-card">Movie 3</div>
                    <div class="movie-card">Movie 4</div>
                    <div class="movie-card">Movie 5</div>
                    <div class="movie-card">Movie 6</div>
                </div>
            </div>
            <div class="category">
                <div class="category-title">Popular on Netflix</div>
                <div class="movie-row">
                    <div class="movie-card">Movie 1</div>
                    <div class="movie-card">Movie 2</div>
                    <div class="movie-card">Movie 3</div>
                    <div class="movie-card">Movie 4</div>
                    <div class="movie-card">Movie 5</div>
                    <div class="movie-card">Movie 6</div>
                </div>
            </div>
            <div class="category">
                <div class="category-title">Continue Watching</div>
                <div class="movie-row">
                    <div class="movie-card">Movie 1</div>
                    <div class="movie-card">Movie 2</div>
                    <div class="movie-card">Movie 3</div>
                    <div class="movie-card">Movie 4</div>
                    <div class="movie-card">Movie 5</div>
                    <div class="movie-card">Movie 6</div>
                </div>
            </div>
            <div class="category">
                <div class="category-title">My List</div>
                <div class="movie-row">
                    <div class="movie-card">Movie 1</div>
                    <div class="movie-card">Movie 2</div>
                    <div class="movie-card">Movie 3</div>
                    <div class="movie-card">Movie 4</div>
                    <div class="movie-card">Movie 5</div>
                    <div class="movie-card">Movie 6</div>
                </div>
            </div>
        </section>
    </body>
    </html>

#Coded with 💙 BY Abhishek3218
