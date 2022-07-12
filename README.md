https://ascii-generator.site/ - to create ASCII version of images
https://stackoverflow.com/questions/23623288/print-full-ascii-art - how to insert ASCII images into Python
https://www.codespeedy.com/check-if-user-input-is-a-string-or-number-in-python/ - to check name input for digits instead of letters
https://pypi.org/project/colorama/ - to add yellow to lightning bolt
https://harrypotter.fandom.com/wiki/Hufflepuff - for about houses


'''def generate_questions(): # only gave one/two questions then stopped - had to remove return answers
    """
    Runs through sorting hat questions
    """
    clear_display()
    answers = []
    for q in questions:  #https://stackoverflow.com/questions/33069253/looping-through-multiple-choice-questions
        print(q['question'])
        sleep(1)
        for i, c in enumerate(q['options']):
            print(chr(97 + i)+ ':', c)
            
        while True: 
            answer = input("Enter your answer:\n>>> ".center(70))
    
            if validate_answer(answer):
                print('\n\nThank you'.center(70))
                answers.append(answer)
                break

        sleep(1)
        clear_display()

        return answers'''

Bug
Questions were looping twice - was calling fucntion from within sort function and then again in main
Was breaking after two questions - 

Bug 
Was updating spreadsheet after welcome moved to after generate questions to update with all details (name etc plus house)
Moved house determination within function to be able to access house variable

Bug 
Centering text on line - not centring when using \n on line so included blank lines before instead of line breaks to ensure centring worked.