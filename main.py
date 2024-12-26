from fasthtml.common import Link, Script, Style, fast_app, serve

from apps.auth.routes import login_routes, signup_routes
from apps.home.routes import home_register_routes, upload_routes
from db_setup import db, initialize_db

# Call the initialization function
initialize_db()

# links
favicon = Link(rel="icon", href="/static/img/favicon.ico", type="image/x-icon")
font_awesome_css = Link(rel="stylesheet", href="/static/css/all.min.css")
pico_css = Link(rel="stylesheet", href="/static/css/pico.min.css")
font_awesome_js = Script(src="/static/js/all.min.js")
flowbite = Script(src="/static/js/flowbite.min.js")
hyper = Script(src="/static/js/_hyperscript.min.js")
tailwind_cdn = Script(src="/static/js/tailwind_cdn.js")

app, rt = fast_app(live=True, hdrs=(favicon, tailwind_cdn, font_awesome_css, font_awesome_js, flowbite, hyper ))

home_register_routes(app)
upload_routes(app)
login_routes(app)
signup_routes(app)

serve()
