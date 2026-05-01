from rest_framework import generics
from django.http import HttpRequest, HttpResponse
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.utils import IntegrityError
import json

from .models import Festival, Band
from .serializers import FestivalSerializer, BandSerializer


class FestivalListCreate(generics.ListCreateAPIView):
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer


class BandListCreate(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer


class FestivalDetails(generics.RetrieveAPIView):
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer
    lookup_field = "id"


class RegisterUser(View):
    def post(self, req: HttpRequest):
        try:
            data = json.loads(req.body)
            username = data["username"]
            password = data["password"]

            User.objects.create_user(
                username=username, email=f"{username}@local", password=password
            )

            res = HttpResponse("created user successfully")
            res.status_code = 201
        except KeyError as err:
            res = HttpResponse(f"{err} is missing")
            res.status_code = 404
        except IntegrityError:
            res = HttpResponse(f"unable to create user {username}")
            res.status_code = 404

        return res


class LoginUser(View):
    def post(self, req: HttpRequest):
        try:
            data = json.loads(req.body)
            username = data["username"]
            password = data["password"]

            user = authenticate(req, username=username, password=password)

            if user is not None:
                login(req, user)
                res = HttpResponse(f"user {username} logged in")
                res.status_code = 201
            else:
                res = HttpResponse(f"unable to log in user {username}")
                res.status_code = 401
        except KeyError as err:
            res = HttpResponse(f"{err} is missing")
            res.status_code = 404

        return res


def logout_user(req: HttpRequest):
    logout(req)

    res = HttpResponse("user logged out")
    res.status_code = 201

    return res
