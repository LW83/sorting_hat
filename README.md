# The Sorting Hat 
***
## Overview 

Welcome to The Sorting Hat, a Harry Potter-themed quiz to determine which Hogwarts House you will be in for the upcoming school term! In the Harry Potter series, the Sorting Hat is a hat that students new to Hogwarts put on and it determines which of the four Houses in Hogwarts (Gryffindor, Hufflepuff, Ravenclaw and Slytherin) the student is best suited to based on their personality and characteristics. This is a purely for fun quiz for Harry Potter fans to simulate the experience of wearing the Sorting Hat from the books. 

NOTE: This site has been created purely for demonstrating Python skills learned as part of the Code Institute's Diploma in Full Stack Software Development. No copyright infringement is intended. 

![Responsiveness Demo](./docs/imac.png)

## Live Site

[The Sorting Hat](https://sorting-hat-22.herokuapp.com/)

## Repository 

[GitHub Repository](https://github.com/LW83/sorting_hat)
***
## Table of Contents:
* [**The Sorting Hat**](#the-sorting-hat)
  * [**Overview**](#overview)
  * [**Concept and Planning**](#concept-and-planning)
    * [**UX**](#ux)
    * [**Game Logic**](#game-logic)
    * [**Background Styling**](*background-styling) 
  * [**Existing Features**](#existing-features)
    * [**Game Landing Page**](#game-landing-page)
    * [**User Inputs**](#user-inputs)
    * [**Welcome Page**](#welcome-page)
    * [**Questions**](#questions)
    * [**House Determination**](#house-determination)
  * [**Feature Enhancements**](#feature-enhancements)
  * [**Testing**](#testing)
    * [**User Story Testing**](#user-story-testing)
    * [**Features Testing**](#features-testing)
    * [**Browser Testing**](#browser-testing)
    * [**Code Validation Testing**](#code-validation-testing)
    * [**Fixed Bugs**](#fixed-bugs)
    * [**Unfixed Bugs**](#unfixed-bugs)
  * [**Deployment**](#deployment)
  * [**Languages & Libraries**](#languages-&-libraries)
    * [**Languages Used**](#languages-used)
    * [**Python Libraries & Modules Utilised**](#python-libraries--modules-utilised)
  * [**Credits**](#credits)
    * [**Media & Content**](#media-&-content)
    * [**Tools and Online Resources Utilised**](#tools-and-online-resources-utilised)
    * [**Code Utilisation**](#code-utilisation)
    * [**People**](#people)
***
## Concept and Planning 

### UX

- __Target Audience__

   - Individuals passionate about the Harry Potter series.
   - Children and adults looking to play a free fun online game.
   - Parents/grandparents looking for an entertaining game for their children/grandchildren to play.

- __User Stories__

   - As a user, I want a free fun online game to play.
   - As a user, I want to be able to easily navigate my way through the game.
   - As a user, I want to be able to personalise my experience of the game.
   - As a user, I want to be able to dictate the length of time I play.
   - As a user, I want to see my final House and have a conclusion to the game.

- __Site Aims__
 
  - The site aims to meet the above user requirements through the following: 
    -  Providing a free, online, fun game to meet the target audience requirements.  
    -  Providing an easy and intuitive way to start, navigate and end or exit the game. 
    -  Enabling the user to personalise their game experience by submitting their name, age and country. 
    -  Enabling the user to play the game multiple times or to exit the game if they wish. 
    -  Providing a game conclusion, final house determination and details of fellow housemates for the upcoming term. 

### Game Logic

- I used [Lucidchart](https://www.lucidchart.com) to set out the main logic of the game: 

![Lucidchart Diagram](./docs/lucidchart.png)

### Background Styling
- To add some aesthetics to the site and improve UX, I added a Harry Potter themed background-image. This image was selected from [The Wizarding World of Harry Potter](https://www.wizardingworld.com/features/try-out-our-new-harry-potter-video-call-backgrounds).
- I also used [Image Color Picker](https://imagecolorpicker.com/en) to identify a color from another Harry Potter image on the same site to use as the basis for the styling of the button.

***
## Existing Features 

### Game Landing Page

__Favicon__

  -  A image of the Sorting Hat has been added as a favicon for the page. 
  
  ![Favicon](./docs/favicon.png)

__Logo__

  - The initial load of the page is comprised of a logo of the Harry Potter initials in the Harry Potter font generated in ASCII. 
  - [ASCII-Generator](https://ascii-generator.site/) was used to convert images to ASCII for inclusion in the page. 
  - The [Colorama](https://pypi.org/project/colorama/) module has been used to color this logo text for improved aesthetics. 
  - There is a sleep delay applied to this page for 5 seconds before the display is cleared and inputs requested from the user. 

  ![Logo](./docs/landing-page.png)

### User Inputs

  - I deliberately decided not to give any information about the game prior to asking for user inputs to maintain a level of secrecy and mystique to the application. 
  - The user is requested to input their name, age and country prior to proceeding. 
  - Name and country inputs are validated to ensure they are not blank and are not soley numerical.
  - Age inputs are validated to ensure they are not blank, are numerical and are between the school-going ages of 4 and 18!
  - These inputs are pushed into a student object for use throughout the game. 

  ![Name Validation](./docs/name-validations.png)
  ![Age Validation](./docs/age-validation.png)
  ![Country Validation](./docs/country-validation.png)

   - Once the user has inputted valid inputs, the computer takes these details to "validate" that the student is magical and not a Muggle!
   - A delay has been added to help create this illusion that background checks are being performed on the users information. 

  ![Muggle Validation](./docs/country-validation.png)

### Welcome Page

  - Once the users non-Muggle status has been confirmed they are brought to a new console view welcoming them to Hogwarts. 
  - Again, both the ASCII Generator and Colorama module have been utilised to create a yellow lightning bolt image above the welcome text. 
  - The datetime module has been utilised to get the current year so that this will update to the current year whenever the game is being played.  
  
![Welcome Page](./docs/welcome-page.png)

  - The user is then asked if they want to get started or if they wish to remove the Sorting Hat i.e. quit.
  - The answer input must be y or n (or Y or N) and validations are in place to ensure no blank entry or other character is accepted. 

![Start Sorting](./docs/start-sorting.png)

  - If the user enters n they see the follow message and are then brought back to the landing page view. 

![Remove Sorting Hat](./docs/hat-remove.png)

### Questions

  - When the user has decided to proceed, they are brought through a series of 11 questions with 4 answer options. 
  - Each question is displayed with a small delay before the answer options are displayed.  
  - After each question the console display is cleared again to improve UX. 

![Question View](./docs/question-display.png)

  - Again, validations are in place to ensure the user enters a,b,c or d as their answer or alternatively opts to quit the game. 

![Answer Validation](./docs/answer-validation.png)
![Exit](./docs/quit.png)

  - Once an answer has been entered, the next question appears. No feedback is provided on the answer as the quiz is not a right or wrong quiz. 
  - Answers are pushed to an answers list for use in subsequently determining the correct House for the user. 

### House Determination

  - Once all questions have been answered the statistics module imported is used to calculate the mode of the answer list. 
  - Each answer to a question corresponds to a House so the mode maps to which House the user should be placed. 
  - The console then clears to display the initial logo of the House determined for the user in the House colors. 
  - Again, ASCII Generator and Colorama have been used to create these colored logos. 

![Gryffindor Logo](./docs/gryffindor-logo.png)
![Slytherin Logo](./docs/slytherin-logo.png)
![Hufflepuff Logo](./docs/hufflepuff-logo.png)
![Ravenclaw Logo](./docs/ravenclaw-logo.png)

  - The user is then told a bit about the typical characteristics of students in their House.  

![Gryffindor About](./docs/gryffindor-about.png)
![Slytherin About](./docs/slytherin-about.png)
![Hufflepuff About](./docs/hufflepuff-about.png)
![Ravenclaw About](./docs/ravenclaw-about.png)

  - At this point, the user has three options; to enter h to accept their designated House, to press r to re-sort them into a new house or to press q to quit the game and return to the landing page. 
  - If the user selects r, they are brought back to the first question of the loop to run through and provide new answers. 
  - If the user selects q, the quit message is again displayed for the user and they are brought back to the starting landing page. 
  - If the user selects h, their final student details including determined house are pushed to a Google spreadsheet, they are brought to the concluding view and shown a list of housemates that will be in their House.
  - This list is pulled from Google sheets using an API and extracts entries where the House matches that of the user.
  - The tabulate module has been imported and used to display the housemates in a tabular structure. 

![Google Sheet](./docs/google-sheet.png)
![Housemates](./docs/housemates.png)

  - This final view is also time delayed to display for 7 seconds before the console clears and the landing page is displayed again. 

***
## Feature Enhancements

 - There are no current features that I believe are oustanding on the game however I would like to revisit the code in future to see if there is further opportunities for refactoring. 
       
***
## Testing 

### User Story Testing

 - All user stories identified have been tested against the final design with the outcome of this testing set out below. 
 - The game has also been tested by family and friends with positive feedback. 

![User Story Testing](./docs/user-testing.png)

### Features Testing
 - All design features have been manually tested with the outcome of this testing set out below. 
 - Screenshots have also been included in the Features section above to show the validation output for the various inputs requested from the user. 
 - Testing was completed in my local terminal and also in Heroku post deployment. 

![Features Testing](./docs/feature-testing.png)

### Browser Testing
  - The site was developed and tested using Google's Chrome browser. 
  - The site has also been tested on Safari and functions as intended. 

![Browser Testing](./docs/browser-testing.png)
 
### Code Validation Testing 

  - The site code has been passed through the following online validation tools: 

  ![Code Validations](./docs/code-validations.png)

__HTML Validation__
  
  - As some updates were made to the HTML file included in the Code Institute template, I passed it through the W3C validator. 
  - There are no errors for the site when passed through the validator. 

  ![W3C validator](./docs/html.png)

__CSS Validation__
  - As some updates were made to the CSS included in the Code Institute template, I passed it through the W3C validator. 
  - There are no errors for the site when passed through the validator.

  ![CSS validator](./docs/css.png)

__Python Validation__

  - No errors were found in any of the three python files when passing through the Pep8 online validator. 
   
  Run File
  ![Run File](./docs/run-pep.png)
  Questions File 
  ![Questions File](./docs/questions-pep.png)
  Logo File
  ![Logo File](./docs/logo-pep.png)

### Fixed Bugs   
  - The following key bugs arose and were fixed during the development of the game: 

    1. Question loop: 
          - Issue: Originally, I had the following code to run through the question loop: 
            
                def generate_questions(): 
                      clear_display()
                      answers = []
                      for q in questions:  
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

                          return answers

              However, in testing I noticed that the questions would stop after two questions and not complete the loop. Subsequently, I also had an issue with the question loop running twice. 
          - Solution: After some trial and error, I realised that in removing the return answers at the end of the code block the full loop would run. After reiviewing my code, I also realised I was calling the function twice, once from within the preceding function and then again within the main function. Once removed from the main function this issue was resolved.
          - Resource: Self-resolved. 

    2. Upload of background imaage:
          - Issue: As part of deployment, the original background image I had saved to an assets folder was not loading in Heroku upon deployment. 
          - Solution: After some research, I discovered that there can be issues with deploying images as static assets in Heroku and decided to change to link to a web addess of the image which resolved the issue. 
          - Resource: Self-resolved. 

    3. Text not centering:  
          - Issue: I noticed that on some lines the text was not centering which I had wanted to implement to improve aesthetics and UX.  
          - Solution: Again after some trial and error I noticed that the text would not center where /n had been used to create a line break. After restructuring the print statements I was able to get the centering to work for all statements I wanted centered. 
          - Resource: Self-resolved. 
    
    4. Updating the House for re-sorting:
          - Issue: Initially, I was pushing the various student inputs and House to the Google spreadsheet after the first round of questions with option to re-sort. I was then struggling to find a suitable way to update the House for a re-sort and ensure that the update was for the correct student. 
          - Solution: After a lot of trial and error with functions I concluded on a simpler solution and moved the update spreadsheet function to the end after the user had confirmed that they were happy with the House determination. It is now only at this stage that student details are pushed to the Google sheet which also means that if a user quits the game their details are not stored and do not need to be identified and deleted from the sheet. 
          - Resource: Self-resolved. 

    5. Generation of Housemates table: 
          - Issue: For a while, I was struggling with how to generate a subset of the Google spreadsheet based on House in order to generate the Housemates table for the user. 
          - Solution: After some research, I looked at trying to use the pandas module but then found that if I extracted all data and converted back from a list to a list of dictionaries and then used list comprehension I could then pull the information where the House key had a specific value and push this into a new dataset as the basis for the table. 
          - Resources: [Stackoverflow](https://stackoverflow.com/questions/63508906/get-all-keys-with-specific-value-in-dictionary-python), 
                       [i2Tutorials](https://www.i2tutorials.com/convert-list-of-lists-to-list-of-dictionaries/)

### Unfixed Bugs
- The two bugs that remain unfixed are: 

  - Allows input before question finished: Currently the game allows the user to enter input prior to being requested. I tried to implement code to block this and only allow a specified window for the user to enter input into the terminal but was unable to find a workable solution to date. Initial research on [Stackoverflow](https://stackoverflow.com/questions/29289945/how-to-temporarily-disable-keyboard-input-using-python) seemed feasible but I was unable to succesfully import the msvcrt module. I also tried to implement the keyboard module in an attempt to utilise the wait and send functions to achieve this affect but was unable to import this module either without installing as sudo which based on some research has potential wider implications. On this basis I preceded without implementing this functionality. 

   - Validation limitation: Currently the validation functions for name and country inputs will accept a name that is a mix of both letters and numbers. I had changed this function from using the isnumeric function to the isalpha function which ensured only letters were accepted however I then noticed that this would not accept an entry with a space so for example if somebody entered their first and last name or a country with two words e.g. South Africa. Of the two options I felt not allowing this would be a more frustrating experience for the user and reverted to using isnumeric as the basis for a validation check. 

***
## Deployment

- Prior to deployment in Heroku, to ensure the dependencies used in Gitpod were installed in Heroku, I ran the pip3 freeze > requirements.txt command in Gitpod. 

- As a python based project, the site was deployed to Heroku following the below deployment steps: 
   - Log in to Heroku (or create an account if required).
   - Click 'Create a new app'.
   - Enter a name for the app (must be unique). I selected sorting-hat-22. 
   - Select your region. For me, this is Europe being based in Ireland. 
   - Select "Create app".
   - In the new page for the app, select the Settings tab from the menu at the top of the main screen. 
   - In the Settings page, go to the 'Config Vars' section and select "Reveal Config Vars".
   - In the 'Key' field enter a name of 'CREDS' and copy and paste the contents of the creds.json file from Gipod into the 'Value' field in order to connect Heroku to the API with Google sheets. 
   - Select 'Add'; in this line enter 'PORT' in the 'Key' field and a 'Value' of 8000 to ensure compatability between teh Code Institute template being used and vaious Python libraries. 
   - Then scroll to the 'Buildpacks' section of teh Settings page and select 'Add Buildpack'.
   - Select 'Python' and save the changes. 
   - Then add 'node.js' as a further buildpack. 
   - Ensure Python is above Node.js in the buildpack order or if not, reorder.
   - Now select the 'Deplpy' section from the menu at the top of the page. 
   - Select GitHub as the deployment method and 'Connect to GitHub'.
   - Find the right repository (here sorting_hat) via the Search functionality and then select 'Connect'.
   - Scroll down to the new 'Manual Deploy' section and select 'Deploy Branch'
   - Wait until the deployment is finished running and select "View".

The live link can be found here: [The Sorting Hat](https://sorting-hat-22.herokuapp.com/) 

***
## Languages & Libraries

### Languages Used
  - Python
  - HTML5
  - CSS3

### Python Libraries & Modules Utilised
  - Tabulate to create housemates table 
  - Colorama to add color to logos
  - OS to enable clear display function
  - Statistics to facilitate mode of answers to be calculated
  - Time to enable sleep functionality
  - gspread and google.oauth2.service_account to connect to Google sheets
  - Datetime to facilitate determination of current year

***
## Credits  

### Media & Content
 - Background image from [The Wizarding World of Harry Potter](https://www.wizardingworld.com/features/try-out-our-new-harry-potter-video-call-backgrounds).
 - Sorting Hat image from [HiClipArt](https://p1.hiclipart.com/preview/458/460/43/harry-potter-black-witch-hat.jpg)
 - HP Logo from [Wikipedia](https://en.wikipedia.org/wiki/File:HP_-_Harry_Potter_wordmark.svg)
 - House Logo text from [Font Space](https://www.fontspace.com/category/harry-potter)
 - Blank iMac from [QWC](https://eshop.macsales.com/blog/40844-how-to-recover-from-a-white-screen-when-booting-a-mac/)
 - Lightning bolt from [Clipart Library](http://clipart-library.com/harry-potter-lightning-bolt.html)
 - House information from [Harry Potter Fandom](https://harrypotter.fandom.com/wiki/Hufflepuff)
 - Some question content from [Brainfall](https://brainfall.com/quizzes/which-hogwarts-house-would-you-be-in/)

### Tools & Online Resources Utilised
 - The following tools and resources have been utilised in the creation of this project: 
     - Code Institute & Love Sandwiches Demonstration: For guidance and inspiration for this site. 
     - GitHub & Gitpod: For development of the site. 
     - [ASCII Generator](https://ascii-generator.site/) to generate ASCII versions of logos.
     - [Image Color Picker](https://imagecolorpicker.com/en) 
     - [Stackoverflow](): For general guidance and research - specific examples used in final build set out below. 
     - [Slack](https://slack.com/intl/en-ie/): For general guidance and research on project considerations. 
     - [Python Tutor](https://pythontutor.com/): For testing code throughout development
     - [W3C HTML Validator](https://validator.w3.org/)
     - [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
     - [Pep8online Validator](http://pep8online.com/)
     - [Heroku](https://id.heroku.com/login)
     - [Lucidchart](https://www.lucidchart.com): To create a flow chart of the game logic
     - [Google](www.google.com): For spreadsheet and API to connect to Python

     Specific Online Resources utilised as references: 
      - https://stackoverflow.com/questions/23623288/print-full-ascii-art - to insert ASCII images into Python
      - https://www.codespeedy.com/check-if-user-input-is-a-string-or-number-in-python/ - to check name input for digits instead of letters
      - https://pypi.org/project/colorama/ - to add color to the ASCII images

### Code Utilisation
 - The following elements of code have specifically been inspired from the following sources: 
    - Code Institute for the deployment terminal 
    - [Rachel Rock](https://github.com/rockymiss) for the folllowing: House spreadsheet update, student update, name validation for blank entry and terminal border. 
    - [David Bowers](https://github.com/dnlbowers) for the following: Clear display functionality and styling to centre the terminal for final deployment. 
    - [Stackoverflow](https://stackoverflow.com/questions/33069253/looping-through-multiple-choice-questions) for guidance on iterating through a bank of questions. 

### People
 - In addition a big thank you to the following people for their assistance or inspiration in this project:
     - David Bowers and Rachel Rock both provided inspiration to me from their Python projects particularly in relation to styling, centring the terminal, adding a background, adding delays in the code and clearing the display all adding to a better UX. 
     - Kasia Bogucka: Our cohort facilitator for keeping us all on track and answering all and any of the many questions!
     - My cohort: For our weekly checkins and tips

