define player = Character('我')
define hitomi = Character('Hitomi', image='hitomi_catear')
image bg black = Color('#000000ff')

transform chr_display:
    yoffset 200

init python:
    import requests
    def set_select(key: str) -> None:
        api_url = 'localhost'
        requests.get(f'https://{api_url}/rescuelimbo/increase?key={key}')
