import unittest
from city_functions import city_country


class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Verify city and country formatting."""
        formatted_city = city_country("santiago", "chile")
        self.assertEqual(formatted_city, "Santiago, Chile")

    def test_city_country_population(self):
        """Verify city, country, and population formatting."""
        formatted_city = city_country("santiago", "chile", population=5000000)
        self.assertEqual(
            formatted_city, "Santiago, Chile - population 5000000"
        )

    def test_city_country_population_language(self):
        """Verify city, country, population, and language formatting."""
        formatted_city = city_country(
            "santiago", "chile", population=5000000, language="spanish"
        )
        self.assertEqual(
            formatted_city,
            "Santiago, Chile - population 5000000, Spanish",
        )


if __name__ == "__main__":
    unittest.main()
