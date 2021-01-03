from flask import send_file
# from StringIO import StringIO
import requests

URL = "https://spacedock.info/api/mod/"
URL_SHIELDS = "https://img.shields.io/static/v1"


def main(request):
    # Get mod selection from request  
    if request.args and "id" in request.args:
        idd = request.args["id"]
    else:
        return "Missing id!"

    # build new request and get response from spacedock
    res = requests.get(url=URL+f"{idd}")

    data = res.json()

    if "error" in data:
        return data["reason"]
    else:
        version = data["versions"][0]["game_version"]

    # make shield
    res = requests.get(url=URL_SHIELDS, params={"label":"", "message":version, "color":"brightgreen"})

    # svg_io = StringIO()
    # svg_io.write(res.content)
    # svg_io.seek(0)
    # return send_file(res.content, mimetype='image/svg+xml')
    print(res)
    print(res.content)
    # send_file(svg_io, mimetype='image/svg+xml')
    # flask.Response(response=response.content, status=response.status_code, headers=response.headers.items())
    return (res.content, res.status_code, res.headers)


    


if __name__ == "__main__":
    main("test")