from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem
from django.utils.translation import gettext_lazy as _

""" 
Creditos

Autor = Gerardo Beltran Pulido
version = "1.0.0
correo = "gerbel06@gmail.com
Estado = "Dev
Fecha = "2021-06-04


"""


""" Se crea la configuracion del menu de django suits"""


class SuitConfig(DjangoSuitConfig):
    layout = 'vertical'

    menu = [
        ParentItem(
            label=_('Estudiantes'),
            children=[
                ChildItem(
                    label=_('Cursos'),
                    url='/api/curso/',
                ),
                ChildItem(
                    label=_('Estudiantes'),
                    url='/api/estudiante/',
                ),
                ChildItem(
                    label=_('Direcciones'),
                    url='/api/direccion/',
                )
            ],
            icon='fa fa-briefcase',
        )
    ]
    verbose_name = 'Django'
    menu_show_home = False

    def ready(self):
        super(SuitConfig, self).ready()
        # DO NOT COPY FOLLOWING LINE
        # It is only to prevent updating last_login in DB for demo app
        self.prevent_user_last_login()
    def prevent_user_last_login(self):
        """
        Disconnect last login signal
        """
        from django.contrib.auth import user_logged_in
        from django.contrib.auth.models import update_last_login
