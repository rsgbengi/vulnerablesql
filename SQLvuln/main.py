from website import create_app
from website.models import User
from website import db


app = create_app()
with app.app_context():
    exists = db.session.query(User.id).filter_by(first_name='admin').first() is not None
    if(not exists):
        new_user = User(
                    email="thisadmin@gmail.com", first_name="admin", password="thisismypassword"
                )
        db.session.add(new_user)
        db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)
