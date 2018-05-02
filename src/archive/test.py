from whoosh.fields import Schema, TEXT

schema = Schema(title=TEXT, content=TEXT)

import os.path
from whoosh.index import create_in

if not os.path.exists("index"):
    os.mkdir("index")
ix = create_in("index", schema)

from whoosh.index import open_dir

ix = open_dir("index")

writer = ix.writer()
writer.add_document(content = u"tenso",title = u"teste1")
writer.add_document(content = u"thiago zampa",title = u"teste2")
writer.add_document(content = u"felipe arcaro",title = u"teste3")
writer.add_document(content = u"thiago chamorro",title = u"teste4")
writer.add_document(content = u"george",title = u"teste5")
writer.add_document(content = u"gv2c ta ficando rica",title = u"teste6")


searcher = ix.searcher()

print(list(searcher.lexicon("felipe")))
