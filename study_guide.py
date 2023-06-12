import sqlite3

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def display(self):
        print("Question:", self.question)
        print("Answer:", self.answer)


class Section:
    def __init__(self, name):
        self.name = name
        self.keywords = []
        self.flashcards = []

    def add_keyword(self, keyword):
        self.keywords.append(keyword)

    def add_flashcard(self, question, answer):
        flashcard = Flashcard(question, answer)
        self.flashcards.append(flashcard)

    def display(self):
        print("Section:", self.name)
        print("Keywords:", ", ".join(self.keywords))
        print("Flashcards:")
        for flashcard in self.flashcards:
            flashcard.display()


class StudyGuide:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sections (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS flashcards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                section_id INTEGER,
                question TEXT,
                answer TEXT,
                FOREIGN KEY (section_id) REFERENCES sections (id)
            )
        ''')
        self.conn.commit()

    def add_section(self, name):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO sections (name) VALUES (?)", (name,))
        self.conn.commit()

    def add_flashcard(self, section_id, question, answer):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO flashcards (section_id, question, answer) VALUES (?, ?, ?)",
            (section_id, question, answer)
        )
        self.conn.commit()

    def display_section(self, section_name):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id FROM sections WHERE name=?", (section_name,))
        result = cursor.fetchone()
        if result:
            section_id = result[0]
            cursor.execute("SELECT * FROM flashcards WHERE section_id=?", (section_id,))
            flashcards = cursor.fetchall()
            section = Section(section_name)
            for flashcard in flashcards:
                _, _, question, answer = flashcard
                section.add_flashcard(question, answer)
            section.display()
        else:
            print("Section not found.")


    def display_all_sections(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM sections")
        sections = cursor.fetchall()
        for section in sections:
            section_id, section_name = section
            print("Section:", section_name, "\n")

    def close(self):
        self.conn.close()