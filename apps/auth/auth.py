from fasthtml import common as fh

from components.forms import login_form, signup_form


# Login page
def login_get():
    return fh.Section(
        fh.Div(
            fh.H1("Login", style={"margin-top": "20%"}),
            login_form(),
            style={"max-width": "400px", "margin": "auto", "padding": "20px"}
        )
    )

# Signup page
def signup_get():
    return fh.Section(
        fh.Div(
            fh.H1("Sign Up", style={"margin-top": "20%"}),
            signup_form(),
            style={"max-width": "400px", "margin": "auto", "padding": "20px"}
        )
    )

