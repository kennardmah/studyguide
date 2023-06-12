from study_guide import StudyGuide
import clear_database
import os

def run_study_guide():
    db_file = "study_guide.db"
    study_guide = StudyGuide(db_file)
    run = True

    while run:
        prompt = input('Would you like to add a new study set? [y/n]\n')
        if prompt == 'y':
            # Adding section
            section = input('What is the section name?\n')
            study_guide.add_section(section)
            section_id = 1
            # Adding flashcards
            while prompt == 'y':
                prompt = input('Would you like to add a flash card? [y/n]\n')
                if prompt == 'y': study_guide.add_flashcard(section_id, input('Question: '), input('Answer: '))
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
            run = False  # Exit the program after clearing the database
        else:
            print('Retry, entered value did not work.')

if __name__ == '__main__':
    run_study_guide()
