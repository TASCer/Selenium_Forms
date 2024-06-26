![TASCS LOGO](./assets/logo.png)

# Selenium Website Testing
My Selenium solution used to schedule testing of my various website's html links and forms.

##### Using Python 3.11
##### *Depdendancies noted in requirements.txt*

#### TESTS

1. Goes through all links in menu bar
2. Completes the two html forms to send request e-mail(s)

   a. CONTACT form has captcha, not ran on production. Hardcoded in TEST

4. Visits HOA page to get the last date and time rental data was updated 
4. Visits BLOG site and counts blogs on first page 

src folder contains: 

        1. Python files needed to run tests

assets folder contains:

        1. Logo file for README

misc folder contains: 

        1. Windows batch file for launching Scheduled Tasks 
