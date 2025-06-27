import sys
import os
import pandas as pd

# Add the src folder to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import load_and_process_data

def test_no_duplicates():
    """
    Test if duplicate rows are removed.
    """
    # Arrange
    test_input_path = "data/dataset.csv"
    test_output_path = "data/processed_dataset.csv"

    # Act
    df = load_and_process_data(test_input_path, test_output_path)

    # Assert
    assert df.duplicated().sum() == 0, "Duplicate rows were not removed"
