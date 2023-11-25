from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        """Переопределям метод для записи хэшированного пароля в БД"""

        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        """Аналогично"""

        for attr, value in validated_data.items():
            if attr == "password":
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = "__all__"
