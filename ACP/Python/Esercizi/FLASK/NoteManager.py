import uuid
from flask import Flask, request, make_response
from note import noteBook

app = Flask(__name__)


@app.post('/note')
def note():
    note = request.get_json()
    id = uuid.uuid1()
    noteBook[str(id)] = note

    ritorno = {
        "result": "added",
        "id":id
    }

    return ritorno 


@app.get('/note/<id>')
def getNote(id):
    if id in noteBook:
        return noteBook[id]
    else:
        backMessage = {
            "result": "Note not found"
        }
        return backMessage, 404
    

@app.get('/notes')
def getAllNotes():
    print(noteBook)
    noteList = []
    for note in noteBook.keys():
        temp = {}
        temp[str(note)] = noteBook[note]
        noteList.append(temp)
    print(noteList)
    return noteList

@app.put('/note/<id>')
def put(id):
    if id in noteBook:
        noteBook[id] = request.get_json()
        backMessage = {
            "result": "updated",
            "id" : id
        }

        return backMessage
    else:
        id = uuid.uuid1()
        noteBook[id] = request.get_json()

        backMessage = {
            "result":"added",
            "id": id
        }

        return backMessage



@app.delete('/note')
def delete():
    param = request.args

    id = param['id']

    if id in noteBook:
        noteBook.pop(id)

        backMessage = {
            "result":"deleted",
            "id":id
        }
        return backMessage
    else:
        backMessage = {
            "result":"Note not found"
        }
        return backMessage,404
    

@app.delete('/notes')
def deleteAll():
    noteBook.clear()
    backMessage = {
        "result":"No more notes"
    }

    return backMessage

if __name__ == "__main__":
    app.run(debug = True)