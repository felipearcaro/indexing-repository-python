# indexing-repository-python
Index and search inside of docx files in a repository using Whoosh-2.7.4

# how to use
1. install python 
2. go to src/example file.doc and change its name and content
3. go to src/run program.py and use 
"qp = QueryParser(u"content", schema=ix.schema)" to look for what's inside of the file
"qp = QueryParser(u"title", schema=ix.schema)" to look for file's names
"q = qp.parse(u"KEYWORD")" to look for a specific key word
