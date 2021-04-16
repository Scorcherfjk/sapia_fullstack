from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,
                                     required=False,
                                     allow_null=True,
                                     allow_blank=True)

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'password',)
        read_only_fields = ('id',)

    def save(self, **kwargs):
        password = self.validated_data.pop('password', None)
        instance = super().save(**kwargs)

        if password:
            instance.set_password(password)
            instance.save()

        return instance
