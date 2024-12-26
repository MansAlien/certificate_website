from fasthtml import common as fh


def home_get():
    home = fh.Title("Home"),fh.Div(
        fh.P("This is the home page"),
    )
    return home

