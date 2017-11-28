from rest_framework.serializers import(
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    EmailField,
    CharField,
    ValidationError,

)

from django.contrib.auth import get_user_model
from django.db.models import Q
User = get_user_model()


class UserDetailSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]


class UserCreateSerializer(ModelSerializer):
    email = EmailField(label="Email Adress")

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']

        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(ModelSerializer):
    username = CharField(allow_blank=True, required=False)
    token = CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'token'
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password")
        if not username:
            raise ValidationError("A username  is required to login.")
        user = User.objects.filter(
            Q(username=username)
        ).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exists() and user.count() == 1:
            user_obj = user.first()
            print("Login ok")
        else:
            raise ValidationError("This username is not valid")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect password")
        data['token'] = "Some"
        print("Login")

        return data