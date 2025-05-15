## What it does
- Copy and paste a recipe from a supported site (like Allrecipes or Pioneer Woman)
- Click "Scrape Recipe" to extract the data
- View the ingredients and instructions inside the app
- Option to Choose to click "Save Recipe" to export as a text file

## Technologies used
- Python
- Tkinter (GUI)
- Beautiful Soup (Html parsing)
- requests (Web scraping)

## Supported Websites
- [AllRecipes.com](https://www.allrecipes.com/)
- [ThePioneerWoman.com](https://www.thepioneerwoman.com/)
- [WellPlated.com](https://www.wellplated.com/)
- Other websites will show an error message if tried - additional websites can easily be added, these where just the ones I use

## How to Run
- Install libraries
  pip install beautifulsoup4 requests

## Use Case
- You are looking online for something to cook and you find a good looking recipe, but its full of pop up ads and the authors entire life story is described.
- This tool lets you scrape the recipe, read it clearly, and save it as a .txt file

## About
- Created as a side project to look at uses of webscrapping as well as to try out building GUIs with Python
