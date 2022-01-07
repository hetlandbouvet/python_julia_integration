"""https://towardsdatascience.com/how-to-embed-your-julia-code-into-python-to-speed-up-performance-e3ff0a94b6e"""

import nltk  # ; nltk.download(["gutenberg", "punkt"])

# import julia; julia.install()
from nltk.corpus import gutenberg
from nltk.stem import PorterStemmer
import time


def load_data():
    data = gutenberg.raw("shakespeare-hamlet.txt")
    data = data.replace("\n", " ")
    data = data.replace("  ", " ")
    return data


def py_compute(data: str):
    porter = PorterStemmer()

    print("Computing using Python")
    t0 = time.time()

    stem_words = []
    nltk_tokens = nltk.word_tokenize(data)
    for token in nltk_tokens:
        new_token = porter.stem(token)
        stem_words.append(new_token)
    t1 = time.time()
    print("Time elapsed: ", t1 - t0)  # CPU seconds elapsed (floating point)


def jl_compute(data):
    print("Setting up Julia")
    from julia.api import Julia
    from julia import Main

    jl = Julia(compiled_modules=False)

    jl.using("TextAnalysis")

    print("Computing using Julia")
    t0 = time.time()
    jl.eval('include("computation.jl")')
    Main.data = data
    stem_list = jl.eval("stemming_document(data)")
    t1 = time.time()
    print("Time elapsed: ", t1 - t0)  # CPU seconds elapsed (floating point)


if __name__ == "__main__":
    print("Loading data...")
    data = load_data()
    data *= 100
    # py_compute(data)
    jl_compute(data)
