from apps.auth.auth import login_get, signup_get


def login_routes(app):
    @app.get("/login")
    def login():
        return login_get()

def signup_routes(app):
    @app.get("/signup")
    def signup():
        return signup_get()
