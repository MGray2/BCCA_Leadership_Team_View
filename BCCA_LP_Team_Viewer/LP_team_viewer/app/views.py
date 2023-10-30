from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from dataclasses import dataclass

# Create your views here.


@dataclass
class Team:
    name: str
    desc: str
    members: list


def landing_page(request: HttpRequest) -> HttpResponse:
    return render(request, "teams.html")


def management_page(request: HttpRequest) -> HttpResponse:
    return render(request, "management.html")


def procurement_page(request: HttpRequest) -> HttpResponse:
    return render(request, "procurement.html")


def documentation_page(request: HttpRequest) -> HttpResponse:
    return render(request, "documentation.html")


def community_page(request: HttpRequest) -> HttpResponse:
    return render(request, "community.html")
