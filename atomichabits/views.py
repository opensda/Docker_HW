from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from atomichabits.models import Habit
from atomichabits.paginators import HabitPaginator
from atomichabits.permissions import IsOwner
from atomichabits.serializers import HabitSerializer


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated]

    # Выводим пользователю только его объекты и публичные
    def get_queryset(self):
        user = self.request.user
        public_objects = Habit.objects.filter(is_public=True)
        user_objects = Habit.objects.filter(user=user)
        return public_objects | user_objects


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    # permission_classes = [IsOwner]


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    # permission_classes = [IsAuthenticated]


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    # permission_classes = [IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    # permission_classes = [IsOwner]
