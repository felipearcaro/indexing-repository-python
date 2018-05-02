searcher = ix.searcher()
from whoosh.qparser import QueryParser

qp = QueryParser("title", schema=ix.schema)
q = qp.parse(u"felipe")

with ix.searcher() as s:
    results = s.search(q)
    len(results)