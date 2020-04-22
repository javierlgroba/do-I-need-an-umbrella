from datetime import datetime
from bottle import route, run, static_file, template
from aemetumbrella import get_precip_info

@route('/resources/<filename>')
def server_static(filename):
    return static_file(filename, root='resources/')

@route('/')
def display_umbrella():
    now = datetime.now()
    pretty_now_day = now.strftime("20%y-%m-%d")
    pretty_now_hour = now.strftime("%H")

    umbrella = get_precip_info(pretty_now_day, pretty_now_hour)
    
    return template('umbrellatemplate', umbrella=umbrella)

run(host='0.0.0.0', port=8080, debug=False)
