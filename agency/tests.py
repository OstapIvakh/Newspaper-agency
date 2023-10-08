from django.test import TestCase
from django.urls import reverse

from agency.models import Topic, Redactor, Newspaper

TOPIC_LIST_URL = reverse("agency:topic-list")
NEWSPAPER_LIST_URL = reverse("agency:newspaper-list")
REDACTOR_LIST_URL = reverse("agency:redactor-list")

HOME_URL = reverse("agency:index")

CREATE_URL = reverse("agency:newspaper-create")


class ModelTestCase(TestCase):
    def setUp(self):
        self.redactor = Redactor.objects.create(
            username="testuser",
            first_name="John",
            last_name="Doe",
            years_of_experience="1"
        )
        self.topic = Topic.objects.create(name="IT industry")
        self.newspaper = Newspaper.objects.create(
            title="Title test",
            content="Some text",
            topic=self.topic,
            publish_date="2023-10-08T12:00:00Z"
        )
        self.newspaper.publishers.add(self.redactor)

    def test_redactor_str_method(self):
        expected_str = f"{self.redactor.username} ({self.redactor.first_name} {self.redactor.last_name})"
        self.assertEqual(str(self.redactor), expected_str)

    def test_topic_str_method(self):
        self.assertEqual(str(self.topic), self.topic.name)

    def test_newspaper_str_method(self):
        self.assertEqual(str(self.newspaper), self.newspaper.title)

    def test_retrieve_newspaper(self):
        response = self.client.get(NEWSPAPER_LIST_URL)
        self.assertEqual(response.status_code, 200)
        newspaper = Newspaper.objects.all()
        self.assertEquals(
            list(response.context["newspaper_list"]),
            list(newspaper),
        )
        self.assertTemplateUsed(response, "agency/newspaper_list.html")

    def test_retrieve_topic(self):
        response = self.client.get(TOPIC_LIST_URL)
        self.assertEqual(response.status_code, 200)
        topic = Topic.objects.all()
        self.assertEquals(
            list(response.context["topic_list"]),
            list(topic),
        )
        self.assertTemplateUsed(response, "agency/topic_list.html")

    def test_retrieve_redactor(self):
        response = self.client.get(REDACTOR_LIST_URL)
        self.assertEqual(response.status_code, 200)
        redactor = Redactor.objects.all()
        self.assertEquals(
            list(response.context["redactor_list"]),
            list(redactor),
        )
        self.assertTemplateUsed(response, "agency/redactor_list.html")