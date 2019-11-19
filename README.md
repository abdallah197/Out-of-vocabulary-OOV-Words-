# Out-of-vocabulary-OOV-Words-
In this repo i  use a multilingual corpus  to investigate the relation between the vocabulary and the OOV rate in different languages

to install used libraries please run
```
pip install -r requirements.txt
```
The code was done to do the following:
1. Partition each corpus into a training corpus (80% of the word tokens) and a test corpus
(20% of the word tokens).
2. Construct a vocabulary for each language by taking the most frequent 15k word types in
the training corpus. The vocabulary set should be ranked by frequency from the most
frequent to the least frequent.
3. Compute OOV rate (percentage) on the test corpus as the vocabulary grows by 1k words.
4. For each language, plot a logarithmic curve where the x-axis represents the size of the
vocabulary and the y-axis represents the OOV rate. Each curve should be plotted on the
same figure with a legend to identify the language of the text corpus.
