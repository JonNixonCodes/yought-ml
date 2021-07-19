# test_sentiment_0.py

# %% Import external libraries
import sys

# %% Import user libraries
sys.path.append("/home/jon-dev/Workbench/Projects/yought-ml")

from yought_ml.source.sentiment import extract_sentiment, extract_subjectivity

# %% Define constants
TEXT_0 = "This is fantastic!"
TEXT_1 = "This was not fantastic..."
TEXT_3 = "The sky is blue."

# %% Define tests
def test_extract_sentiment():
    assert(extract_sentiment(TEXT_0) > 0)
    assert(extract_sentiment(TEXT_1) < 0)

def test_extract_subjectivity():
    assert(extract_subjectivity(TEXT_0) > 0.5)
    assert(extract_subjectivity(TEXT_1) > 0.5)
    assert(extract_subjectivity(TEXT_3) < 0.5)

def run_tests():
    print("Running tests...")
    test_extract_sentiment()
    test_extract_subjectivity()
    print("All passed!")

# %% Main
if __name__=="__main__":
    run_tests()
