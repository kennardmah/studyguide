from study_guide import StudyGuide
import clear_database
import os

def run_study_guide():
    db_file = "study_guide.db"
    study_guide = StudyGuide(db_file)
    run = True

    while run:
        prompt = input('Would you like to add content? [y/n]\n')
        if prompt == 'y':
            # Adding sections
            study_guide.add_section("Math")
            study_guide.add_section("Science")
            # Adding flashcards
            study_guide.add_flashcard(1, "What is the Pythagorean theorem?", "a^2 + b^2 = c^2")
            study_guide.add_flashcard(1, "What is the quadratic formula?", "x = (-b ± √(b^2 - 4ac)) / 2a")
            study_guide.add_flashcard(2, "What is DNA?", "Deoxyribonucleic acid")
        elif prompt == 'n':
            prompt = input('Would you like to review content? [y/n]\n')
            if prompt == 'y':
                study_guide.display_all_sections()
                section_name = input('Which section would you like to review? ')
                study_guide.display_section(section_name)
        elif prompt == 'esc':
            study_guide.close()
            run = False
        elif prompt == 'force delete':
            clear_database.clear_database(db_file)
            # run = False  # Exit the program after clearing the database
        else:
            print('Retry, entered value did not work.')

if __name__ == '__main__':
    run_study_guide()
