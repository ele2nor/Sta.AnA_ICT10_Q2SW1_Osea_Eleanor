# Seatwork 2
from pyscript import document

def candidate_checker(event=None):
    club_members = [
        "chi kawa",
        "chloe bennett",
        "dawn brown",
        "giselle uri",
        "lina paige",
        "luna poppy",
        "harie bowe",
    ]

    f_name = document.getElementById("first_name").value
    l_name = document.getElementById("last_name").value
    candidate = f"{f_name} {l_name}".strip()

    member_checker = candidate.lower() in [
        member.lower() for member in club_members
    ]

    messages = {
        True: f"CONGRATS {candidate}! You are in the varsity!",
        False: f"Sorry {candidate} but you didnt get into the varsity.",
    }

    document.getElementById("result_area").innerHTML = messages[member_checker]
    