import pytest
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from mixer.backend.django import mixer
from django.http import Http404

from .. import views

pytestmark = pytest.mark.django_db


class TestIndexView:
    def test_anonymous_user(self):
        req = RequestFactory().get('/')
        resp = views.index(req)

        assert resp.status_code == 200, 'Should be callable by anyone'
