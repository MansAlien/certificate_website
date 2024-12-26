from fasthtml.common import H1, Div, Form, Input, Label, Span


def login_form():
    form = Form(
        Input(type="login", placeholder="username", autocomplete="username"),
        Input(type="password", placeholder="password", autocomplete="current-password"),
        Input(type="submit", value="submit")
        )
    return Div(form)

def signup_form():
    form = Form(
        Input(type="text", name="first_name", placeholder="First name", required=True, maxlength=20),
        Input(type="text", name="last_name", placeholder="Last name", required=True, maxlength=20),
        Input(type="text", name="username", placeholder="username", required=True, maxlength=20),
        Input(type="email", name="email", id="email", placeholder="Email", autocomplete="email", required=True),
        Input(type="password", id="password", name="password", placeholder="password", required=True,
            **{"aria-invalid":""}),
        Input(
            type="password", 
            id="confirm",
            name="confirm", 
            placeholder="confirm password", 
            required=True,
            **{
                "aria-invalid":"",
                "_": """on keyup 
                        if #password.value != #confirm.value 
                        then set #password's @aria-invalid to "true"
                        then set #confirm's @aria-invalid to "true"
                        else set #confirm's @aria-invalid to "false"
                        then set #password's @aria-invalid to "false"
                        """,
            }
        ),
        Span("", id="password-feedback", style={"color": "red"}),
        Input(type="submit", value="Submit")
    )
    return Div(form)
