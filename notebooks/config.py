# Some things that need to be known accross notebooks
from typing import Dict, List, Tuple
from pathlib import Path
from collections import defaultdict


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
                   'study', 'https', 'http', 'ii', 'david']
