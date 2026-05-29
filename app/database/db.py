from database.session import SessionLocal


def get_connection():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
