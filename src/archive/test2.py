#setup

import docx2txt

# extract text
text = docx2txt.process("../documents/ambev.docx")
text2 = docx2txt.process("../documents/ambev2.docx")
text3 = docx2txt.process("../documents/ambev3.docx")

from whoosh.fields import Schema, TEXT

schema = Schema(title=TEXT(stored=True), content=TEXT)

import os, os.path
from whoosh import index

if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

ix = index.create_in("indexdir", schema)

#indexando arquivos

ix = index.open_dir("indexdir")
writer = ix.writer()
writer.add_document(title=u"ambev.docx", content=text)
writer.add_document(title=u"ambev2.docx", content=text2)
writer.add_document(title=u"ambev3.docx", content=text3)
writer.add_document(title=u"sato", content=u"thiago")
writer.commit()

#buscando

searcher = ix.searcher()
from whoosh.qparser import QueryParser

qp = QueryParser(u"content", schema=ix.schema)
q = qp.parse(u"hyppolito")

with ix.searcher() as s:
    results = s.search(q)
    print (results)
    for result in results:
        print (result)
    

