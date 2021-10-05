from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
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
        try:
            query = db.session.execute(
                f"Select * from note where note_title='{note_title}'"
            ).fetchone()
            if query is None:
                flash("Not note for this title")
            else:
                flash(f"Your note is: {query['data']}")
        except SQLAlchemyError as e:
            flash(e, category="error")

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
