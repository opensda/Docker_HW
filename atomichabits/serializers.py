from rest_framework import serializers

from atomichabits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    def validate_time_to_complete(self, value):
        if value > 120:
            raise serializers.ValidationError('Время выполнения привычки должно быть не более 120 сек.')
        return value

    def validate_frequency(self, value):
        if value > 7:
            raise serializers.ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')
        return value


    related_habit = serializers.CharField(required=False)
    award = serializers.CharField(required=False)
    is_pleasant = serializers.BooleanField(required=False)



    def validate(self, data):
        related_habit = data.get('related_habit')
        award = data.get('award')
        is_pleasant = data.get('is_pleasant')

        if related_habit and award:
            raise serializers.ValidationError('Связанную привычку и вознаграждение нельзя выбирать одновременно')

        elif is_pleasant and related_habit or award:
            raise serializers.ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')

        elif related_habit and is_pleasant is False:
            raise serializers.ValidationError(
            'В связанные привычки могут попадать только привычки с признаком приятной привычки.')


        return data

    class Meta:
        model = Habit
        fields = "__all__"