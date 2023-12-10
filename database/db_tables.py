import aiosqlite

from src.config.default import db_path


async def db_tables():
    aio_base = await aiosqlite.connect(db_path)
    cur = await aio_base.cursor()
    try:
        print("sqlite.db connection is OK")
        await cur.execute("CREATE TABLE IF NOT EXISTS users("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                    "user_id INTEGER UNIQUE, "
                    "user_name TEXT)")

        await cur.execute("CREATE TABLE IF NOT EXISTS questionnaires("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                    "title TEXT, "
                    "is_active INTEGER DEFAULT 0, "
                    "description TEXT NULL)")

        await cur.execute("CREATE TABLE IF NOT EXISTS questions("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                    "question_text TEXT NOT NULL, "
                    "questionnaire_id INTEGER NOT NULL, "
                    "FOREIGN KEY (questionnaire_id) REFERENCES questionnaires(id))")

        await cur.execute("CREATE TABLE IF NOT EXISTS answers("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                    "answer_text VARCHAR(40) NOT NULL, "
                    "question_id INTEGER NOT NULL, "
                    "FOREIGN KEY (question_id) REFERENCES questions(id))")

        await cur.execute("CREATE TABLE IF NOT EXISTS result("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                    "user_id INTEGER NOT NULL, "
                    "answer_id INTEGER NOT NULL, "
                    "FOREIGN KEY (user_id) REFERENCES users(id), "
                    "FOREIGN KEY (answer_id) REFERENCES answers(id), "
                    "UNIQUE(user_id, answer_id))")
    finally:
        await aio_base.close()
