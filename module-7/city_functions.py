# city_functions.py

def city_country(city, country, population=None, language=None):
    """Return a formatted string for a city and country, with optional population and language."""
    output = f"{city.title()}, {country.title()}"
    if population:
        output += f" - population {population}"
    if language:
        output += f", {language.title()}"
    return output

if __name__ == "__main__":
    # 1. City, Country
    print(city_country("santiago", "chile"))
    # 2. City, Country, Population
    print(city_country("santiago", "chile", 5000000))
    # 3. City, Country, Population, Language
    print(city_country("santiago", "chile", 5000000, "spanish"))
