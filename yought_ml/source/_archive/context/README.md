# Context Analyser
This package enables users to analyse the context of unstructured written text. A *context* object is initialised with some text, the text is automatically analysed and the output of the analysis is stored in the object. The *context* object consists of the following: *entities*; *themes*; *sentiment*.

## How to use
1. Install the required python libraries
```
conda create --name context-analyser --file requirements.txt
conda activate context-analyser
```
2. Download the spaCy language model
```
python -m spacy download en_core_web_sm
```
3. Try the following basic example to test that the package is working
```python
from context import Context
context = Context("I like blue ribbons!")
print(context.entities)
print(context.themes)
print(context.sentiment)
```
