import requests

localNoteBook = {}
nota = {
    "test":"prova",
    "tag":"work"
}
post_resp = requests.post('http://127.0.0.1:5000/note', json = nota)
ritorno = post_resp.json()
localNoteBook[ritorno['id']] = nota


nota = {
    "test1":"prova1",
    "tag1":"work1"
}
post_resp = requests.post('http://127.0.0.1:5000/note', json = nota)
ritorno = post_resp.json()
localNoteBook[ritorno['id']] = nota

print(localNoteBook)
valueKey = next(iter(localNoteBook.keys()))

get_resp = requests.get(f'http://127.0.0.1:5000/note/{valueKey}')
ritorno = get_resp.json()
localNoteBook.update(ritorno)


get_resp = requests.get(f'http://127.0.0.1:5000/notes')
ritorno = get_resp.json()
print(ritorno)
for i in ritorno:
    localNoteBook.update(i)



print(localNoteBook)