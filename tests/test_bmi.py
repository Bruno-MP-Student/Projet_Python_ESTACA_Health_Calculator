import sys
import os

# Ajout du répertoire src au PYTHONPATH pour que Python puisse le trouver
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from health_calculator.bmi import calculate_bmi, bmi_category  # Import des fonctions à tester

def test_calculate_bmi():
    # Test des calculs de l'IMC pour des valeurs valides
    assert calculate_bmi(70, 1.75) == 22.86
    assert calculate_bmi(50, 1.60) == 19.53

    # Test des valeurs invalides, comme un poids ou une taille négatifs
    with pytest.raises(ValueError):
        calculate_bmi(-70, 1.75)

    with pytest.raises(ValueError):
        calculate_bmi(70, 0)  # La taille ne peut pas être égale à 0

def test_bmi_category():
    # Test des catégories d'IMC pour différentes valeurs
    assert bmi_category(17) == "Underweight"  # Sous-poids
    assert bmi_category(22.86) == "Normal weight"  # Poids normal
    assert bmi_category(27) == "Overweight"  # Surpoids
    assert bmi_category(30) == "Obesity"  # Obésité
