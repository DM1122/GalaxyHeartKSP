import requests

URL = "https://spacedock.info/api/mod/"


def main(request):
    # Get mod selection from request  
    if request.args and "id" in request.args:
        idd = request.args["id"]
    else:
        return "Missing id!"

    # build new request and get response from spacedock
    res = requests.get(url=URL+f"{idd}")

    data = res.json()

    if data["error"]:
        return data["reason"]
    else:
        version = data["versions"][0]["game_version"]

    return version


if __name__ == "__main__":
    main("test")