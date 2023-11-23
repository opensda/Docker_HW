

""" Валидация связанной привычки и вознаграждения"""

# def post(self, request, *args, **kwargs):
#     related_habit = request.data.get("related_habit")
#     award = request.data.get("award")
#     if related_habit and award:
#         raise serializers.ValidationError('Связанную привычку и вознаграждение нельзя выбирать одновременно')
#
#     return self.create(request, *args, **kwargs)



""" Валидация времени выполнения привычки"""

# def post(self, request, *args, **kwargs):
#     time_to_complete = request.data.get("time_to_complete")
#     if time_to_complete > 120:
#         raise serializers.ValidationError('Время выполнения привычки должно быть не более 120 сек.')


""" Валидация периодичности выполнения привычки"""
# def post(self, request, *args, **kwargs):
#     frequency = request.data.get("frequency")
#     if frequency > 7:
#         raise serializers.ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')


"""В связанные привычки могут попадать только привычки с признаком приятной привычки"""

# def post(self, request, *args, **kwargs):
#     related_habit = request.data.get("related_habit")
#     is_pleasant = request.data.get("is_pleasant")
#
#     print(related_habit)
#     print(is_pleasant)
#     if related_habit is not None and is_pleasant is False or is_pleasant is None:
#         raise serializers.ValidationError(
#             'В связанные привычки могут попадать только привычки с признаком приятной привычки.')
#
#     return self.create(request, *args, **kwargs)




"""У приятной привычки не может быть вознаграждения или связанной привычки"""

# def post(self, request, *args, **kwargs):
#     related_habit = request.data.get("related_habit")
#     is_pleasant = request.data.get("is_pleasant")
#     award = request.data.get("award")
#
#     if is_pleasant and related_habit or award:
#         raise serializers.ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')
#
#     return self.create(request, *args, **kwargs)



class HabitSerializer(serializers.Serializer):
    # Ваши поля сериализатора, например:
    related_habit = serializers.CharField(required=False)
    award = serializers.CharField(required=False)

    def validate(self, data):
        related_habit = data.get('related_habit')
        award = data.get('award')

        if related_habit and award:
            raise serializers.ValidationError('Связанную привычку и вознаграждение нельзя выбирать одновременно')

        return data