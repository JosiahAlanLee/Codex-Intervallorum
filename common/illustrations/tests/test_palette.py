"""Compare the drawn table with the book's independent cast enumeration."""
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import unittest

from common.illustrations.palette import credentials, transition_counts

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location(
    'notoria_math', ROOT/'books/05_notoria/manuscript/check_math.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class Palette(unittest.TestCase):
    def test_every_cell_matches_independent_cast_enumeration(self):
        for weights in ((1, 5, 7, 3), (1, 3, 3, 1)):
            total = sum(weights)
            primary, resulting, joint = checker.check([Fraction(w, total) for w in weights])
            table = transition_counts(weights)
            denominator = total**6
            for a in range(64):
                for b in range(64):
                    self.assertEqual(Fraction(table[a][b], denominator), joint[a, b])
            self.assertEqual([Fraction(sum(row), denominator) for row in table], primary)
            self.assertEqual([Fraction(sum(row[b] for row in table), denominator)
                              for b in range(64)], resulting)

    def test_invalid_weights_rejected(self):
        for weights in ((1, 2, 3), (0, 5, 7, 3), (1, -5, 7, 3), (1., 5, 7, 3)):
            with self.assertRaises(ValueError):
                transition_counts(weights)

    def test_credentials_follow_current_catalogue(self):
        book = json.loads((ROOT/'books/03_escalationum/manuscript/catalogue.json').read_text())
        key = ' '.join(book['illustrations']['credentials']['paragraphs']).casefold()
        for office in book['tiers']:
            self.assertIn(office['name'].casefold(), key)
        before = credentials(book)
        # A changed competence in the source adds one centre ring, without a cached lookup.
        book['tiers'][-1]['competence'] += 1
        after = credentials(book)
        self.assertEqual(len(after.paths), len(before.paths)+1)
        self.assertNotEqual(before.svg(), after.svg())
        self.assertEqual(after.metadata['tiers'][-1]['competence'], 1)


if __name__ == '__main__':
    unittest.main()
