# setup

import docx2txt

import os
names = os.listdir("/Applications/mamp/htdocs/Whoosh-2.7.4/documents")
comp= len(names)
contentText = []

for i in range(0, comp-1):
    contentText.append(0);

# extract textname  
    
from whoosh.fields import Schema, TEXT

schema = Schema(title=TEXT(stored=True), content=TEXT, path=TEXT(stored=True))

import os, os.path
from whoosh import index

if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

ix = index.create_in("indexdir", schema)

#indexando arquivos

ix = index.open_dir("indexdir")
writer = ix.writer()
for x in range(1, comp-1):
    contentText[x] = docx2txt.process("../documents/" + names[x])
    writer.add_document(title=names[x],content=contentText[x])
writer.commit()

#buscando

searcher = ix.searcher()
from whoosh.qparser import QueryParser

qp = QueryParser(u"content", schema=ix.schema)
q = qp.parse(u"tamura")

with ix.searcher() as s:
    results = s.search(q)
    print (results)
    for result in results:
        print (result)
    

    

