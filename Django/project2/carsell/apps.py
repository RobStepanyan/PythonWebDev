from django.apps import AppConfig


class CarsellConfig(AppConfig):
    name = 'carsell'

    def ready(self):
        import users.signals