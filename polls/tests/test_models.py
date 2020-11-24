import pytest
from mixer.backend.django import mixer
from django.utils import timezone

pytestmark = pytest.mark.django_db


class TestQuestion:
    def test_create(self):
        obj = mixer.blend('polls.Question')
        assert obj.pk == 1, "Should create a Question object"

    def test_was_published_recently(self):
        obj = mixer.blend('polls.Question', pub_date=timezone.now())
        result = obj.was_published_recently()
        assert result == True, "Should turn out to be published recently"

    def test_str_(self):
        obj = mixer.blend('polls.Question', question_text="What's your name?")
        result = obj.__str__()
        assert result == "What's your name?", "Should return string \
          representation of question text"

    def test_choice_relation(self):
        question = mixer.blend('polls.Question')
        choice = mixer.blend("polls.Choice", question=question)
        result = question.choice_set.get(id=1)
        assert result == choice, "Should return the related choice object"


class TestChoice:
    def test_create(self):
        obj = mixer.blend('polls.Choice')
        assert obj.pk == 1, "Should create a Choice object"

    def test_str_(self):
        obj = mixer.blend('polls.Choice', choice_text="James Bond")
        result = obj.__str__()
        assert result == "James Bond", "Should return string \
          representation of Choice text"
