from django.apps import AppConfig
from django.conf import settings
from django.core.checks import Error, register
from django.template import Engine, TemplateDoesNotExist


class BigRedButtonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bigredbutton'

    @register()
    def check_session_engine(app_configs, **kwargs):
        errors = []
        if session_engine := getattr(settings, "SESSION_ENGINE"):
            engine_name = session_engine.split('.')[0]
            engine = Engine.get_default()
            try:
                engine.find_template(f"bigredbutton/{engine_name}_list.html")
            except TemplateDoesNotExist:
                errors.append(
                    Error(
                        (
                            "There is no session list template for your "
                            f"selected session engine '{engine_name}'."
                        ),
                        hint=(
                            "Ensure that your selected session engine has a "
                            "corresponding template: "
                            "'bigredbutton/{session_engine}.html"
                        ),
                        id="bigredbutton.E001",
                    ),
                )
        return errors
