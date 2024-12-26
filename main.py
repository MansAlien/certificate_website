from fasthtml import common as fh

from apps.auth.routes import login_routes, signup_routes
from apps.home.routes import home_register_routes

hyper = fh.Script(src="/static/js/_hyperscript.min.js")
app, rt = fh.fast_app(hdrs=(hyper,))

home_register_routes(app)
login_routes(app)
signup_routes(app)

fh.serve()
