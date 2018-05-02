#setup

import docx2txt

# extract text
text = docx2txt.process("../documents/ambev.docx")
text2 = docx2txt.process("../documents/ambev2.docx")
text3 = docx2txt.process("../documents/ambev3.docx")

from whoosh.fields import Schema, TEXT

schema = Schema(title=TEXT, content=TEXT)

import os, os.path
from whoosh import index

if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

ix = index.create_in("indexdir", schema)

#indexando arquivos

ix = index.open_dir("indexdir")
writer = ix.writer()
writer.add_document(title=u"ambev", content=text)
writer.add_document(title=u"gleidson", content=text2)
writer.add_document(title=u"gleidson", content=text3)
writer.add_document(title=u"sato", content=u"thiago")
writer.commit()

#buscando
with ix.searcher() as searcher:

searcher = ix.searcher()
from whoosh.query import *
myquery = And([Term("content", u"chamorro"))
from whoosh.qparser import QueryParser
parser = QueryParser("content", ix.schema)
myquery = parser.parse(querystring)
    results = searcher.search(myquery)
    print(len(results))
    