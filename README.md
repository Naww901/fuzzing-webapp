# README

## Overview

This project is Ruby on Rails web application that was built with the intention of demonstrating the usefulness of fuzzing as a tool to utilize in cybersecurity. 

To run the webapp locally:

1. First make sure that postgres is running on the machine with the command `brew services start postgresql`.
2. Then, from `fuzzing-webapp` directory, install all gem dependencies associated with the project by running `bundle install`.
3. Next, run the migration using `rails db:migrate db:reset`
4. Finally, the command `rails start` or `rails s` will begin runnning the application locally. The default address of the app is http://localhost:3000/welcome

After the webapp is running, the welcome page is where you will find the file upload functionality. This is what we will use the **fuzzer** (upload_fuzzer.py) to check for any vulnerabilities relating to sanitization of the uploaded file types. 

Inside the `fuzzing-webapp/fuzzer` folder you will find the upload_fuzzer.py python script which is what is used to check against the SecList list of file extensions. Simply running the python file will yield results on what extensions are currently supported by this webapp. Currently, this build of the webapp is properly working, to only allow for a handful of file extensions. 

## Demo:

https://github.com/Naww901/fuzzing-webapp/assets/128878159/cbd63389-729b-4cd4-8572-23106ca519e0
