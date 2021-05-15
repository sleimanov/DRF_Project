from django.apps import AppConfig


class AuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth_'

    def ready(self):  # method just to import the signals
            import auth_.signals