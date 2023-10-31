from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from dataclasses import dataclass, asdict

# Create your views here.


@dataclass
class Team:
    name: str
    desc: str
    members: list[str]


community_team = Team(
    "Community",
    "Team associated with planning group events, extra programs, and birthdays.",
    ["Jordan", "Joby", "Aj", "Micah", "Caleb"],
)
documentation_team = Team(
    "Documentation",
    "Team involved with mock interviews, recording events, and managing a social media account.",
    [
        "Conner",
        "Kaleigh",
        "Blair",
        "Mina",
        "Jay",
        "Joshua",
        "Kayleah",
    ],
)
procurement_team = Team(
    "Procurement",
    "Team tasked with managing a budget and providing food for lunch and events.",
    ["Adrian", "Bryce", "Big John", "Blaine", "Wyatt"],
)
management_team = Team(
    "Management",
    "Team associated with chores, taking inventory of supplies, and hosting stand-up events.",
    ["Owen", "Jeremiah", "Nick", "Ab", "Abigail", "Mathew"],
)


def landing_page(request: HttpRequest) -> HttpResponse:
    return render(request, "base.html")


def team_page(request: HttpRequest, team_name) -> HttpResponse:
    if team_name == "community":
        return render(request, "team.html", asdict(community_team))
    if team_name == "documentation":
        return render(request, "team.html", asdict(documentation_team))
    if team_name == "procurement":
        return render(request, "team.html", asdict(procurement_team))
    if team_name == "management":
        return render(request, "team.html", asdict(management_team))
