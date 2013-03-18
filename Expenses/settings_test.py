from settings import *
import os
SOUTH_TESTS_MIGRATE = False
SKIP_SOUTH_TESTS = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_PATH,'testdatabase'),
    }
}

INSTALLED_APPS += \
    (
        'django_jenkins',
    )

PROJECT_APPS = (
    'backend',
)

JENKINS_TASKS = (
    'django_jenkins.tasks.dir_tests',
    'django_jenkins.tasks.django_tests',
    'django_jenkins.tasks.with_coverage',
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.run_pyflakes',
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.run_sloccount',
)

PYLINT_RCFILE = os.path.join(PROJECT_PATH, 'pylint.rc')