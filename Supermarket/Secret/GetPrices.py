import random


def get_prices():
    """Returns a dictionary of supermarket items and their prices."""
    product_list = ["Gallon of milk", "Carton of eggs", "Cheese block", "Yogurt", "Apples", "Bananas", "Carrots",
                    "Tomatoes", "Potatoes", "Broccoli", "Chicken breast", "Fresh or frozen fish", "Loaf of bread",
                    "Dry pasta", "Brown rice", "Couscous", "Tomato sauce", "Peanut butter", "Granola bars", "Nuts",
                    "Dried or canned beans"]
    return {product: round(random.uniform(0.5, 100), 2) for product in product_list}
