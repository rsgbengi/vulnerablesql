from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        note = request.form.get("note")
        note_title = request.form.get("note_title")
        print(note)
        print(note_title)

        if len(note) < 1 and len(note_title) < 1:
            flash("Note or title is too short!", category="error")
        else:
            new_note = Note(data=note, note_title=note_title, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added!", category="success")

    return render_template("home.html", user=current_user)


@views.route("/search", methods=["POST", "GET"])
@login_required
def search():
    if request.method == "POST":
        note_title = request.form.get("note_title")
        query = db.session.execute(
            f"Select data from note where note_title={note_title}"
        )
        flash(f"Your note is: {query.get()}")

    return render_template("search.html", user=current_user)


@views.route("/delete-note", methods=["POST"])
def delete_note():
    note = json.loads(request.data)
    noteId = note["noteId"]
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
