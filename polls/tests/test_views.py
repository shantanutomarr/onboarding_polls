import pytest
from django.test import RequestFactory

from .. import views

pytestmark = pytest.mark.django_db


class TestIndexView:
    def test_anonymous_user(self):
        req = RequestFactory().get('/')
        resp = views.index(req)

        assert resp.status_code == 200, 'Should be callable by anyone'
