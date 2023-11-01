from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView


class SessionMixin:
    def get_queryset(self):
        return self.request.user.session_set.filter(expire_date__gt=now()).order_by('-updated_at')


class SessionList(LoginRequiredMixin, SessionMixin, ListView):
    context_object_name = 'sessions'

    def get_template_names(self):
        sessions_app = settings.SESSION_ENGINE.split('.')[0]
        return [f"bigredbutton/{sessions_app}_list.html"]

    def get_context_data(self, **kwargs):
        kwargs['session_key'] = self.request.session.session_key
        return super().get_context_data(**kwargs)


class SessionDelete(LoginRequiredMixin, SessionMixin, DeleteView):
    def get_object(self):
        return super().get_queryset().exclude(session_key=self.request.session.session_key)

    def get_success_url(self):
        success_url = reverse_lazy('list_sessions')
        if urlname := getattr(settings, "BIGREDBUTTON_DELETE_SUCCESS_URL_NAME", "list_sessions"):
            success_url = reverse_lazy(urlname)
        return success_url
