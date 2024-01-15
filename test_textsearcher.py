

import unittest
from unittest.mock import Mock, MagicMock
import textsearcher
import operator


class textsearcherTest(unittest.TestCase):
    def test_search(self):
        db = Mock()
        searcher = textsearcher.TextSearcher(db)
        # connectメソッドが引数なしで呼ばれたことを確認する
        db.connect.assert_called_with()
        searcher.setup(cache=True, max_items=100)
        # conigureメソッドが引数ありで呼ばれたことを確認する
        searcher.db.configure.assert_called_with(max_items=100)
        # 結果データのモックを作成する


if __name__ == "__main__":
    unittest.main()