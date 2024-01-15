"""
textsearcer - データベースを探索して結果を返すTextSearcherクラスを含むモジュール
書籍-Pythonで始めるソフトウェアアーキテクチャ Anand Balachandran Pillai 著/ 渡辺賢人 役
see p90 3.3.3モックの便利な利用方法
"""

import operator

class TextSearcher(object):
    def __init__(self, db):
        """ initializer : キャッシュとデータベースオブジェクトの初期化を行う """
        self.cache = False  #そもそもキャッシュするかの有無
        self.cache_dict = {}
        self.db = db
        self.db.connect()

    def setup(self, cache=False, max_items=500):
        """ 設定を行う """
        self.cache = cache
        # DBのconfigureメソッドを呼んで、初期化を行う
        self.db.configure(max_items=max_items)

    def get_results(self, keyword, num=10):
        # キャッシュにデータがある場合はそれを返す
        if keyword in self.cache_dict:
            print('From cache')
            return self.cache_dict[keyword]
        results = self.db.query(keyword)

        # resultsは(string, weightage)のタプルのリストになる
        results = sorted(results, key=operator.itemgetter(1), reverse=True)[:num]

        # キャッシュに登録する
        if self.cache:
            self.cache_dict[keyword] = results
        return results


