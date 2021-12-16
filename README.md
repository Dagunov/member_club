# member_club
 Test project for yalantis golang school

## Features
 1. Project is deployed on [heroku](https://members-club-mmah.herokuapp.com/).
 2. Project has [tests](#tests) that cover its main functionality.
 3. Logging is enabled - all basic log messages, as well as all incoming requests and outgoing responses, are logged to the *general.log* file.

## Deploy for yourself
 **This chapter will cover required steps to deploy your own member_club locally and on heroku.**
 ### Downloading source code
  To do so, you can use [GitHub Desktop](https://desktop.github.com/), [git command line tool](https://git-scm.com/downloads) or just [download .zip archive](https://github.com/Dagunov/member_club/archive/refs/heads/main.zip) and unpack it on your PC.
  If you choose to use git command line tool, then run following command in target directory:

    git clone https://github.com/Dagunov/member_club.git new_folder_name

  Where **new_folder_name** is name of the folder that will be created automatically.  
 ### Deploying locally
  As soon as you download source code, you can proceed.
  #### Requirements
   1. [Python](https://www.python.org/downloads/). This project was created with [python-3.9.9](https://www.python.org/downloads/release/python-399/), but last available version should be ok.
   2. Python Django package. To install it you can run next command in your terminal (provided you have python in your PATH):

    pip install Django
  #### Steps
   1. Modify project to run locally.
   The only step necessary is to change in file *settings.py* (which is in folder member_club) this line:

         DEBUG = False

   To this line:

         DEBUG = True

   If you do not wish to run project on heroku later and won't install *django-heroku* package, you should find and comment out this two lines of code:

         import django_heroku

   and

         django_heroku.settings(locals())
   2. Run project.
   Run next command in the project root folder to start your local server:

         py manage.py runserver
   Your site should be accessible at <http://127.0.0.1:8000/>.
   If you wish to change port or else, you can run next command to view available flags:

         py manage.py runserver --help
 ### Deploying on heroku
  #### Requirements
   1. [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) if you do not have (not local) git repository.
   2. [git command line tool](https://git-scm.com/downloads), also if you do not have (not local) git repository.
  #### Steps
   1. If you changed something while running project locally (like commenting lines in *settings.py*), you need to undo that. **DEBUG** variable value is, however, up to you.
   2. If you have git repository or want to create it, login to [github](https://github.com/) and create your new repository, then add all files from project folder to it **OR** use [GitHub Desktop](https://desktop.github.com/) to create and push all files into repository.
   3. Login to [Heroku](https://www.heroku.com) and create a new app (try not to forget its name).
   4. If you have files in remote github repository, in your app settings (on Heroku) open **Deploy**, scroll to **Deployment method** and choose **GitHub**. Then follow steps described there.
   5. If you have chosen to operate with Heroku CLI, also go to **Deploy** and scroll to **Deployment method**, make sure that you are on **Heroku Git** option and follow steps described there.
   6. Congratulations! Your site should be online. To visit it, scroll up on heroku and press **Open app** button.


## Tests
 **This chapter will cover required steps to run tests in this project.**
  1. You should complete [all steps](#deploying-locally) necessary to deploy project locally, including [downloading the source code](#downloading-source-code).
  2. While you are in the root folder, run next command:

        py manage.py collectstatic

  3. Now you can run this command to run all tests:

        py manage.py test

  3. To view tests, locate *tests.py* file in the *page* folder.