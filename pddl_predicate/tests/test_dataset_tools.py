from unittest import TestCase
from pddl_predicate import dataset_tools
from pathlib import Path

class TestDataset_tools(TestCase):
    def test_get_n_more_present_words(self):
        p = Path('.')
        p = p / ".." / ".." / ".." / "Visual_Genome" / "objects.json"
        tool = dataset_tools.DatasetTools(p)
        out = Path('.')
        n = 1000
        file = str(n) + "_more_present_word"
        out = out / file
        tool.get_n_more_present_words(n, out)