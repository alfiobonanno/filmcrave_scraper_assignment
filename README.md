# FilmCrave Scraper & Analysis Assignment

## Project Overview

This academic project demonstrates web scraping techniques and data analysis skills by extracting information about the top-rated movies from FilmCrave and performing comprehensive exploratory data analysis (EDA) on the collected dataset.

The project consists of two main components:
1. **Web Scraper** (`filmscraper.py`): Automated data collection from FilmCrave's top movies list
2. **Data Analysis** (`film_analysis.ipynb`): In-depth exploratory data analysis with visualizations

## What This Project Does

### Web Scraping Component
The `filmscraper.py` script:
- Scrapes movie data from FilmCrave's "Top Movies of All Time" pages
- Automatically navigates through multiple pages using pagination
- Extracts comprehensive movie information including:
  - Rank and title
  - Release year
  - Overall rating
  - Language
  - Genre(s)
  - MPAA rating
  - Director(s)
  - Lead actors
  - Plot summary
- Handles missing data gracefully with try-except blocks
- Saves the collected data to a CSV file (`films.csv`)

### Data Analysis Component
The `film_analysis.ipynb` Jupyter notebook performs:
- **Data Cleaning & Preparation**: 
  - Checking for null values and duplicates
  - Parsing multi-value fields (genres, directors, actors)
  - Data type validation and formatting
  
- **Exploratory Data Analysis** answering key questions:
  - Correlation between release year and ratings
  - Trends in average film ratings over time
  - Distribution of movie releases by year
  - MPAA rating distribution and evolution
  - Most frequent directors and their rating consistency
  - Most recurring actors and common collaborations
  - Language distribution across films
  - Genre distribution patterns
  - Common themes extracted from plot summaries using NLP

- **Visualizations**:
  - Interactive plots using Plotly
  - Statistical charts with Matplotlib and Seaborn
  - Word clouds for thematic analysis

## Technologies Used

- **Python 3.x**: Core programming language
- **Beautiful Soup 4**: HTML parsing and web scraping
- **Requests**: HTTP requests for web page retrieval
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib & Seaborn**: Data visualization
- **Plotly**: Interactive visualizations
- **TextBlob**: Natural language processing for plot analysis
- **NLTK**: Advanced text processing
- **Jupyter Notebook**: Interactive development environment

## Learning Outcomes

Through completing this project, the following skills and concepts were developed:

### 1. Web Scraping Techniques
- Understanding HTML structure and DOM navigation
- Using CSS selectors to target specific elements
- Implementing pagination logic to scrape multiple pages
- Error handling for missing or malformed data
- Ethical web scraping practices (respecting website structure)

### 2. Data Collection & Processing
- Structuring scraped data into organized formats
- Handling various data types and edge cases
- Cleaning and validating collected data
- Dealing with missing values appropriately
- Exporting data to CSV format

### 3. Exploratory Data Analysis (EDA)
- Formulating analytical questions about datasets
- Statistical analysis of numerical and categorical data
- Identifying trends and patterns in time-series data
- Analyzing relationships between different features
- Drawing meaningful insights from raw data

### 4. Data Visualization
- Creating clear, informative visualizations
- Using multiple visualization libraries effectively
- Designing interactive plots for better data exploration
- Selecting appropriate chart types for different data types

### 5. Python Programming Best Practices
- Writing modular, readable code
- Implementing error handling strategies
- Using list comprehensions for data transformation
- Working with libraries and managing dependencies
- Documentation and code organization

### 6. Domain Knowledge
- Understanding film industry metrics (MPAA ratings, genres)
- Analyzing cinema trends over decades
- Identifying patterns in successful films
- Recognizing frequent collaborations in filmmaking

### 7. Problem-Solving Skills
- Breaking down complex problems into manageable steps
- Debugging scraping logic when page structure varies
- Adapting analysis techniques to data characteristics
- Finding creative solutions to data extraction challenges

## Setup & Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation Steps

1. Clone this repository:
```bash
git clone https://github.com/alfiobonanno/filmcrave_scraper_assignment.git
cd filmcrave_scraper_assignment
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Web Scraper

To scrape fresh data from FilmCrave:

```bash
python filmscraper.py
```

This will:
- Fetch all movies from the top movies list
- Save the results to `films.csv`
- Print the first few entries to the console

**Note**: The scraping process may take several minutes depending on the number of pages and your internet connection.

### Running the Analysis

To perform the data analysis:

1. Ensure Jupyter Notebook is installed (included in requirements.txt)
2. Launch Jupyter:
```bash
jupyter notebook
```
3. Open `film_analysis.ipynb` in your browser
4. Run all cells to reproduce the analysis

Alternatively, you can use JupyterLab:
```bash
jupyter lab
```

## Project Structure

```
filmcrave_scraper_assignment/
├── filmscraper.py          # Web scraping script
├── film_analysis.ipynb     # Data analysis notebook
├── films.csv               # Scraped movie data
├── requirements.txt        # Project dependencies
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## Data Schema

The `films.csv` file contains the following columns:

| Column | Type | Description |
|--------|------|-------------|
| rank | Integer | Movie ranking on FilmCrave |
| film_title | String | Title of the movie |
| film_year | String/Integer | Year of release |
| overall_rating | Float | Average rating (0-5 scale) |
| language | String | Primary language |
| genre | String | Genre(s), multiple separated by "/" |
| mpaa_rating | String | MPAA rating (G, PG, PG-13, R, etc.) |
| director | String | Director(s), multiple separated by "," |
| actors | String | Main actors, separated by "," |
| plot_summary | String | Brief plot description |

## Key Findings

Some interesting insights discovered through the analysis:
- The dataset contains movies spanning several decades
- Certain directors consistently produce highly-rated films
- Drama is the most common genre among top-rated movies
- English is the predominant language
- There are notable actor-director collaborations
- Film ratings show interesting temporal patterns

## Acknowledgments

- FilmCrave for providing the movie data
- Open-source Python community for excellent libraries

## Academic Context

This project was completed as an academic assignment to demonstrate proficiency in:
- Web scraping and data collection
- Data cleaning and preparation
- Exploratory data analysis
- Data visualization
- Python programming
- Scientific computing with Python ecosystem

## License

This project is for educational purposes only.

## Author

Alfio Bonanno

## Date

2025
