from src.database import SessionLocal

def load(transformed_games):
    db = SessionLocal()

    try:
        for game in transformed_games:
                db.merge(game)

        db.commit()
        print("Data saved to database.")

    except Exception as e:
        print("Error while saving data:")
        print(e)
        db.rollback()

    finally:
        db.close()