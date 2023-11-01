from datetime import timedelta

from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from django.test import Client, TestCase


class ViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', '', 'secret')
        self.client = Client()
        self.client.login(username=self.user.username, password='secret')
        ua = (
            "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) "
            "AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 "
            "Safari/7534.48.3"
        )
        self.user.session_set.create(
            session_key='ABC123',
            user=self.user,
            ip='127.0.0.1',
            expire_date=now() + timedelta(days=1),
            user_agent=ua,
        )

    def test_list(self):
        with self.assertWarnsRegex(UserWarning, r"The address 127\.0\.0\.1 is not in the database"):
            response = self.client.get(reverse('list_sessions'))
        content = response.content.decode("utf-8")
        self.assertTemplateUsed(response, "bigredbutton/qsessions_list.html")
        self.assertNotContains(response, 'ABC123')  # Security
        self.assertIn('Safari', content)
        self.assertInHTML('Active Sessions', content)
        self.assertInHTML('Mobile Safari on Apple iPhone', content)

    def test_delete(self):
        self.assertEqual(self.user.session_set.count(), 2)
        response = self.client.post(reverse('delete_other_sessions'))
        self.assertEqual(self.user.session_set.count(), 1)
        self.assertRedirects(response, reverse('list_sessions'), fetch_redirect_response=False)
