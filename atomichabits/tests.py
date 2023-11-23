import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from atomichabits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        """Добавляем привычку в БД для тестирования"""
        self.user = User.objects.create(email='test@example.com')
        client = APIClient()
        client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(place="test_place", action="test_action", user=self.user)


    def test_get_habit_list(self):
        response = self.client.get(reverse("atomichabits:habit_list"))


        self.assertEqual(response.status_code, status.HTTP_200_OK)

        print(response.json())

        # self.assertEqual(
        #     response.json(),
        #     {
        #         "count": 1,
        #         "next": None,
        #         "previous": None,
        #         "results": [
        #             {
        #                 "id": self.habit.id,
        #                 "user": self.habit.user,
        #                 "place": self.habit.place,
        #                 "time": self.habit.time,
        #                 "action": self.habit.action,
        #                 "is_pleasant": self.habit.is_pleasant,
        #                 "related_habit": self.habit.related_habit,
        #                 "frequency": self.habit.frequency,
        #                 "award": self.habit.award,
        #                 "time_to_complete": self.habit.time_to_complete,
        #                 "is_public": self.habit.is_public,
        #             }
        #         ],
        #     },
        # )

    def test_habit_create(self):
        data = {
            "place": "test_place_create",
            "action": "test_action_create",
        }

        response = self.client.post(reverse("atomichabits:habit_create"), data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_update(self):
        data = {
            "place": "test_place_update",
            "action": "test_action_update",
        }

        url = reverse("atomichabits:habit_update", args=[self.habit.pk])
        response = self.client.put(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_deletion(self):
        url = reverse("atomichabits:habit_delete", args=[self.habit.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_time_to_complete_validation(self):

        data = {
            "place": "test_time_to_complete_validation",
            "action": "do something",
            "time_to_complete": 150
        }

        response = self.client.post(reverse("atomichabits:habit_create"), data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(
            response.json(),
            {"time_to_complete": ["Время выполнения привычки должно быть не более 120 сек."]},
        )

    def test_frequency_validation(self):

        data = {
            "place": "test_frequency_validation",
            "action": "do something",
            "frequency": 8
        }

        response = self.client.post(reverse("atomichabits:habit_create"), data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(
            response.json(),
            {"frequency": ["Нельзя выполнять привычку реже, чем 1 раз в 7 дней."]},
        )

    def test_rel_habit_and_award_validation(self):

        data = {
            "place": "test_rel_habit_and_award_validation",
            "action": "do something",
            "award": "eat something",
            "related_habit": 1
        }

        response = self.client.post(reverse("atomichabits:habit_create"), data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(
            response.json(),
            {"non_field_errors": ["Связанную привычку и вознаграждение нельзя выбирать одновременно"]},
        )

    def test_is_pl_and_award_or_rel_h_validation(self):

        data = {
            "place": "test_is_pl_and_award_or_rel_h_validation",
            "action": "do something",
            "award": "eat something",
            "is_pleasant": True
        }

        response = self.client.post(reverse("atomichabits:habit_create"), data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(
            response.json(),
            {"non_field_errors": ["У приятной привычки не может быть вознаграждения или связанной привычки."]},
        )

    def test_rel_habit_and_is_pleasant_validation(self):

        data = {
            "place": "test_rel_habit_and_is_pleasant_validation",
            "action": "do something",
            "related_habit": 1,
            "is_pleasant": False
        }

        response = self.client.post(reverse("atomichabits:habit_create"), data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(
            response.json(),
            {"non_field_errors": ["В связанные привычки могут попадать только привычки с признаком приятной привычки."]},
        )
