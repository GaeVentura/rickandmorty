
import uuid
from flask import Flask, request

app = Flask(__name__)

noteBook = {}

@app.post('/note')
def addNote():
    json = request.get_json()
    id = str(uuid.uuid1())
    noteBook[id] = json
    return {"result":"added", "id":id}

@app.get('/note/<id>')
def getNote(id):
    if id in noteBook:
        return noteBook[id]
    else:
        return {"result":"Note not found"}, 404
    
@app.get('/notes')
def getNotes():
    listaNote = []
    for noteID in noteBook.keys():
        nota = { 'id':noteID, 'note': noteBook[noteID]}
        listaNote.append(nota)
    
    return listaNote 


@app.put('/note/<id>')
def updateNote(id):
    nota = request.get_json()

    if id in noteBook:
        noteBook[id] = nota

        return {"result": "updated", "id": id}
    else:
        id = str(uuid.uuid1())
        noteBook[id] = nota

        return {"result": "added", "id":id}



@app.delete('/note')
def deleteNote():
    param = request.args
    notaDaEliminare = param['id']
    if notaDaEliminare in noteBook:
        del noteBook[notaDaEliminare]
        return {'result': 'deleted', 'id': notaDaEliminare}
    
    else:
        return {'result': 'Note not found'},404


@app.delete('/notes')
def deleteAllNotes():
    noteBook.clear()

    return {"result": "no more notes"}

if __name__ == "__main__":

    app.run(debug=True)