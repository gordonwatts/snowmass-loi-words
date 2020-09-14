# Some things that need to be known accross notebooks
from typing import Dict, List, Tuple, Any, Iterable
from pathlib import Path
from collections import defaultdict

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import _check_stop_list


loi_unpacked = "./loi-text" # Where we can write the output

def load_text() -> Dict[str, List[Tuple[str, str]]]:
    loi = Path(loi_unpacked)
    all_files = ((f.relative_to(loi).parent.name, f) for f in Path(loi_unpacked).glob('**/*.txt'))
    files_by_area = defaultdict(list)
    for area, file in all_files:
        files_by_area[area].append((file.stem, file.read_text()))
    return files_by_area


def text_file_info() -> List[Tuple[str, str, str]]:
    'Return (filename stem, area, full_path) for all files in the corpus'
    loi = Path(loi_unpacked)
    return ((f.stem, f.relative_to(loi).parent.name, str(f)) for f in Path(loi_unpacked).glob('**/*.txt'))

# Extra stop words - these should always be lower case!
extra_stopwords = ['high', 'energy', 'physics', 'beam', 'beams', 
                   'will', 'well', 'et', 'al', 'due', 'phys',
                   'rev', 'use', 'small', 'lett', 'using',
                   'one', 'two', 'within', 'several', 'may',
                   'arxiv', 'hep', 'astro', 'letter',
                   'provide', 'new', 'jhep', 'ph', 'need',
                   'study', 'https', 'http', 'ii', 'david',
                   'aaaczhichvfls8naej7gv1tfvy9egkxwvbir9fh84uwpab',
                   'aoxd3nbp6nxdqja0z1mkp0rtxu4ac6f3qln',
                   'tv0t3jwy5okwqqbnjp7ztffzuzyocdjarjvow1hcwl5jv8orq6tb2ywtrybczbedqs7grdeldukmccfq0supdyki2b5tsea9uasjtehlip5io7lkgrd33if73phkoduoij5kjwniqgwpuuymvombnwc0gd1qecbozsqt4wesfgewrtja5njboxaujqgfshjks5oqkxkjmaxmcyga',
                   'xdnnozknbonwov7eawdztcpk772jdk0qy7vzxbj2e',
                   'zlpv5l6dkk64agvvejap',
                   'qfknsbvyabekykdtsqzev',
                   'finally',
                   'edu',
                   'briefly',
                   'astron',
                   'extra',
                   'cao',
                   'careful',
                   'com',
                   'figure',
                   'date',
                   
                  ]

# Clustering Config
n_features = 4000  # How many words should we grab from the documents?

def word_vectors(filenames: Iterable[str], do_idf: bool = True) -> Tuple[Any, TfidfVectorizer]:
    '''
    Read in the list of documents, tokenize the strings, and then create a vector
    for each document after making some decisions about what words belong in the list.
    
    - Removes the standard english stop words and the list of `extra_stopwords` above.
    - Ignores numbers
    - Words must appear in at least 2 documents if they are to make this list
    - If a word appears in 50% of the documents, then it does not make this list.
    - Word must be at least 3 letters long
    - Word importance is the standard IDF (https://en.wikipedia.org/wiki/Tf%E2%80%93idf)
    
    If the above gets changed, also update the word_list_template.md document.
    '''
    stopwords = list(_check_stop_list('english')) + extra_stopwords
    vectorizer = TfidfVectorizer(input='filename',
                                 max_df=0.5, max_features=n_features,
                                 min_df=2, stop_words=stopwords,
                                 use_idf=do_idf,
                                 token_pattern=r'\b[a-zA-Z]\w\w+\b')
    return vectorizer.fit_transform(filenames), vectorizer
