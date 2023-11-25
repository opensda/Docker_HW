from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from atomichabits.models import Habit


class HabitTestCase(APITestCase):
    def setUp(self):
        self.habit = Habit.objects.create(
            place="test_place", action="test_action", is_pleasant=True
        )

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
            "time_to_complete": 150,
        }

        response = self.client.post(reverse("atomichabits:habit_create"), data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(
            response.json(),
            {
                "time_to_complete": [
                    "Время выполнения привычки должно быть не более 120 сек."
                ]
            },
        )

    def test_frequency_validation(self):
        data = {
            "place": "test_frequency_validation",
            "action": "do something",
            "frequency": 8,
        }

        response = self.client.post(reverse("atomichabits:habit_create"), data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(
            response.json(),
            {"frequency": ["Нельзя выполнять привычку реже, чем 1 раз в 7 дней."]},
        )

    def test_related_habit_validation(self):
        self.habit = Habit.objects.create(place="uuu", action="uuu", is_pleasant=False)

        data = {"place": "home", "action": "do something", "related_habit": 2}

        response = self.client.post(reverse("atomichabits:habit_create"), data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(
            response.json(),
            {"related_habit": ["Связанная привычка должна быть полезной."]},
        )

    def test_rel_habit_and_award_validation(self):
        data = {
            "place": "test_rel_habit_and_award_validation",
            "action": "do something",
            "award": "eat something",
            "related_habit": 1,
        }

        response = self.client.post(reverse("atomichabits:habit_create"), data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(
            response.json(),
            {
                "non_field_errors": [
                    "Связанную привычку и вознаграждение нельзя выбирать одновременно"
                ]
            },
        )

    def test_is_pl_and_award_or_rel_h_validation(self):
        data = {
            "place": "test_is_pl_and_award_or_rel_h_validation",
            "action": "do something",
            "award": "eat something",
            "is_pleasant": True,
        }

        response = self.client.post(reverse("atomichabits:habit_create"), data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(
            response.json(),
            {
                "non_field_errors": [
                    "У приятной привычки не может быть вознаграждения или связанной привычки."
                ]
            },
        )
