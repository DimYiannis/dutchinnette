"""
Module test definitions for Dutchinnette
Each module contains exercises with their test cases
"""

# ===================== MODULE00 =====================
MODULE00 = {
    "ex0": {
        "file": "ex0/ft_hello_garden.py",
        "func": "ft_hello_garden",
        "cases": [
            ([], "Hello, Garden Community!")
        ],
    },
    "ex1": {
        "file": "ex1/ft_plot_area.py",
        "func": "ft_plot_area",
        "cases": [
            (["5", "3"], "Plot area: 15"),
        ],
    },
    "ex2": {
        "file": "ex2/ft_harvest_total.py",
        "func": "ft_harvest_total",
        "cases": [
            (["5", "8", "3"], "Total harvest: 16"),
        ],
    },
    "ex3": {
        "file": "ex3/ft_plant_age.py",
        "func": "ft_plant_age",
        "cases": [
            (["75"], "Plant is ready to harvest!"),
            (["45"], "Plant needs more time to grow."),
        ],
    },
    "ex4": {
        "file": "ex4/ft_water_reminder.py",
        "func": "ft_water_reminder",
        "cases": [
            (["4"], "Water the plants!"),
            (["1"], "Plants are fine"),
        ],
    },
    "ex5": {
        "file": "ex5/ft_count_harvest_iterative.py",
        "func": "ft_count_harvest_iterative",
        "cases": [
            (["5"], "Day 1"),
            (["5"], "Day 2"),
            (["5"], "Day 3"),
            (["5"], "Day 4"),
            (["5"], "Day 5"),
            (["5"], "Harvest time!"),
        ],
    },
    "ex5_recursive": {
        "file": "ex5/ft_count_harvest_recursive.py",
        "func": "ft_count_harvest_recursive",
        "cases": [
            (["5"], "Day 1"),
            (["5"], "Day 2"),
            (["5"], "Day 3"),
            (["5"], "Day 4"),
            (["5"], "Day 5"),
            (["5"], "Harvest time!"),
        ],
    },
    "ex6": {
        "file": "ex6/ft_garden_summary.py",
        "func": "ft_garden_summary",
        "cases": [
            (["Community Garden", "25"], "Garden: Community Garden"),
            (["Community Garden", "25"], "Plants: 25"),
            (["Community Garden", "25"], "Status: Growing well!"),
        ],
    },
    "ex7": {
        "file": "ex7/ft_seed_inventory.py",
        "func": "ft_seed_inventory",
        "cases": [
            (["tomato", 15, "packets"], "15 packets"),
            (["carrot", 8, "grams"], "8 grams"),
            (["lettuce", 12, "area"], "12"),  # Just check the number appears
            (["basil", 10, "unknown"], "Unknown unit"),
        ],
    },
}

# ===================== MODULE01 =====================
MODULE01 = {
    "ex0": {
        "file": "ex0/ft_garden_intro.py",
        "func": None,  # Script execution, not function call
        "cases": [
            ([], "=== Welcome to My Garden ==="),
            ([], "Plant: Rose"),
            ([], "Height: 25cm"),
            ([], "Age: 30 days"),
            ([], "=== End of Program ==="),
        ],
    },
    "ex1": {
        "file": "ex1/ft_garden_data.py",
        "func": None,
        "cases": [
            ([], "=== Garden Plant Registry ==="),
            ([], "Rose"),
            ([], "25cm"),
            ([], "30 days"),
            ([], "Sunflower"),
            ([], "80cm"),
            ([], "45 days"),
            ([], "Cactus"),
            ([], "15cm"),
            ([], "120 days"),
        ],
    },
    "ex2": {
        "file": "ex2/ft_plant_growth.py",
        "func": None,
        "cases": [
            ([], "=== Day 1 ==="),
            ([], "Rose"),
            ([], "25cm"),
            ([], "30 days"),
            ([], "=== Day 7 ==="),
            ([], "31cm"),
            ([], "36 days"),
            ([], "Growth this week: +6cm"),
        ],
    },
    "ex3": {
        "file": "ex3/ft_plant_factory.py",
        "func": None,
        "cases": [
            ([], "=== Plant Factory Output ==="),
            ([], "Created: Rose"),
            ([], "25cm"),
            ([], "30 days"),
            ([], "Created: Oak"),
            ([], "200cm"),
            ([], "365 days"),
            ([], "Created: Cactus"),
            ([], "5cm"),
            ([], "90 days"),
            ([], "Created: Sunflower"),
            ([], "80cm"),
            ([], "45 days"),
            ([], "Created: Fern"),
            ([], "15cm"),
            ([], "120 days"),
            ([], "Total plants created: 5"),
        ],
    },
    "ex4": {
        "file": "ex4/ft_garden_security.py",
        "func": None,
        "cases": [
            ([], "=== Garden Security System ==="),
            ([], "Plant created: Rose"),
            ([], "Height updated: 25cm"),
            ([], "[OK]"),
            ([], "Age updated: 30 days"),
            ([], "[OK]"),
            ([], "Invalid operation attempted"),
            ([], "-5cm"),
            ([], "[REJECTED]"),
            ([], "Negative height rejected"),
            ([], "Current plant: Rose"),
            ([], "25cm"),
            ([], "30 days"),
        ],
    },
    "ex5": {
        "file": "ex5/ft_plant_types.py",
        "func": None,
        "cases": [
            ([], "=== Garden Plant Types ==="),
            ([], "Rose"),
            ([], "Flower"),
            ([], "25cm"),
            ([], "30 days"),
            ([], "red"),
            ([], "blooming"),
            ([], "Oak"),
            ([], "Tree"),
            ([], "500cm"),
            ([], "1825 days"),
            ([], "50cm diameter"),
            ([], "shade"),
            ([], "Tomato"),
            ([], "Vegetable"),
            ([], "80cm"),
            ([], "90 days"),
            ([], "summer"),
            ([], "vitamin"),
        ],
    },
    "ex6": {
        "file": "ex6/ft_garden_analytics.py",
        "func": None,
        "cases": [
            ([], "=== Garden Management System Demo ==="),
            ([], "Added Oak Tree"),
            ([], "Alice's garden"),
            ([], "Added Rose"),
            ([], "Added Sunflower"),
            ([], "helping all plants grow"),
            ([], "Oak Tree grew 1cm"),
            ([], "Rose grew 1cm"),
            ([], "Sunflower grew 1cm"),
            ([], "=== Alice's Garden Report ==="),
            ([], "Plants in garden:"),
            ([], "Oak Tree: 101cm"),
            ([], "Rose: 26cm"),
            ([], "red flowers"),
            ([], "blooming"),
            ([], "Sunflower: 51cm"),
            ([], "yellow flowers"),
            ([], "Prize points: 10"),
            ([], "Plants added: 3"),
            ([], "Total growth: 3cm"),
            ([], "Plant types:"),
            ([], "1 regular"),
            ([], "1 flowering"),
            ([], "1 prize flowers"),
            ([], "Height validation test: True"),
            ([], "Garden scores"),
            ([], "Alice: 218"),
            ([], "Bob: 92"),
            ([], "Total gardens managed: 2"),
        ],
    },
}

# ===================== MODULE02 (Template for future) =====================
MODULE02 = {
    # Add module02 exercises here when available
}

# Export all modules
__all__ = ['MODULE00', 'MODULE01', 'MODULE02']