
import environ

env = environ.Env()
environ.Env.read_env()

DATABASES ={
    'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'athenasapi',
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASS'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
    }
}