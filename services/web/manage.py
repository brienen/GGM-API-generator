from flask.cli import FlaskGroup

from project import app, database


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    database.init_db()


#@cli.command("seed_db")
#def seed_db():
#    db.session.add(User(email="michael@mherman.org"))
#    db.session.commit()


if __name__ == "__main__":
    cli()
