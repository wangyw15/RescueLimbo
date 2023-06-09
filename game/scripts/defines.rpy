define player_name = '黎明'
define player = Character('player_name', dynamic=True)
define hitomi = Character('Hitomi', image='hitomi')
image bg black = Color('#000000ff')
image overlay black = Color('#000000ff')
image overlay dark = Color('#000000bb')

transform chr_display:
    offset (100, 1150)
    zoom 0.85

transform pic_display:
    offset(-400, -350)

init python:
    def set_select(key: str):
        api_url = 'https://rescuelimbo.wangyw15.top'
        if renpy.emscripten:
            renpy.emscripten.run_script(f"fetch('{api_url}/rescuelimbo/increase?key={key}')")
        else:
            import requests
            requests.get(f'{api_url}/rescuelimbo/increase?key={key}')

    def fullscreen():
        if renpy.emscripten:
            renpy.emscripten.run_script('document.body.requestFullscreen()')
