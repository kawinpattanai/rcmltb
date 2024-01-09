# Source: Tg:MaheshChauhan/DroneBots Github.com/Vasusen-code

from re import findall


def get_link(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = findall(regex, string)
    try:
        return link if (link := [x[0] for x in url][0]) else False
    except Exception:
        return False
