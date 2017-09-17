# teilex

## about

a application to deal with dictionaries encoded in tei


### first steps

This projects uses modularized settings (to keep sensitiv information out of version control or being able to use the same code for developement and production). Thefore you'll have to append all `manage.py` commands with a `--settings` parameter pointing to the settings file you'd like to run the code with. For developement just append `--settings={nameOfYouProject}.settings.dev` to the following commands, e.g. `python manage.py makemigrations --settings=teilex.settings.dev`

6. Run `makemigrations`, `migrate`, and `runserver` and check [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## next steps

Build your custom awesome Web App.

## Tests

To get needed software you can run

    pip install -r requirements_test.txt

To run the tests execute

    python manage.py test --settings=teilex.settings.test
