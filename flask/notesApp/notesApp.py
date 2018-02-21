from sqlalchemy import *
from flask import Flask, render_template, request

app = Flask(__name__)
db = create_engine("sqlite:///notesApp.db")
db.echo = False
metadata = MetaData(db)

try:
	notes = Table("notes", metadata,
		Column("noteId", Integer, primarykey=True),
		Column("noteName", String),
		Column("note", String)
	)
	notes.create()
except:
	notes = Table('notes', metadata, autoload=True)

@app.route("/", methods=["GET", "POST"])
def index():
	'''renders the index template, shows stored notes, and allows new notes to be added'''
	if request.method == "POST":
		try:
			noteName = request.form("noteName")
			note = request.form("note")
			insert = notes.insert()
			insert.execute(noteName = noteName, note = note)
			selectName = notes.select(notes.noteName)
			selectNote = notes.select(notes.note)
			selExNa = selectName.execute()
			selExNo = selectNote.execute()
			oldNotes = {selExNa : selExNo}
			return render_template("index.html", oldNotes = oldNotes)
		except Exception as e:
			selectName = notes.select(notes.noteName)
			selectNote = notes.select(notes.note)
			selExNa = selectName.execute()
			selExNo = selectNote.execute()
			oldNotes = {selExNa : selExNo}
			return render_template("index.html", e = e, oldNotes = oldNotes)
	elif request.method == "GET":
		return render_template("index.html")

if __name__ == "__main__":
	app.run()
