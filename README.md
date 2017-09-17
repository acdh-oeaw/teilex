# teilex

## about

a application to deal with dictionaries encoded in tei


### first steps

This projects uses modularized settings (to keep sensitive information out of version control or being able to use the same code for development and production). Therefore you'll have to append all `manage.py` commands with a `--settings` parameter pointing to the settings file you'd like to run the code with. For development just append `--settings={nameOfYouProject}.settings.dev` to the following commands, e.g. `python manage.py makemigrations --settings=teilex.settings.dev`

Run `makemigrations`, `migrate`, and `runserver` and check [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Tests

To get needed software you can run

    pip install -r requirements_test.txt

To run the tests execute

    python manage.py test --settings=teilex.settings.test
