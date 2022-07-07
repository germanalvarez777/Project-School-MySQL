import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'escuela',
        'USER': 'root',
        'PASSWORD': 'rootroot'
    }
}

'''MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'escuela_db',
        'USER': 'adm_odontologia',
        'PASSWORD': 'Qwerty123#'
    }
}'''