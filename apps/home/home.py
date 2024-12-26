from fasthtml import common as fh
from components.table import table_header, table_row


def home_get(conferences):
    # Header section remains the same
    header = fh.Nav(
        fh.Ul(
            fh.Li(fh.A(fh.Strong("NRCT Certificates Website"), href="/", cls="contrast"))
        ),
        fh.Ul(
            fh.Li(fh.A("Home", href="/", cls='contrast')),
            fh.Li(fh.A("Login", href="/login", cls='contrast')),
            fh.Li(fh.A("Signup", href="/signup", cls='contrast')),
        ),
        style={"padding": "30px", "background-color": "black"},
        id="header"
    )

    # Upload section remains the same
    upload = fh.Title("Home"), fh.Div(
        fh.Form(
            fh.Input(id="file", type="file", name="file"),
            fh.Button("Upload", type="submit", style={"width": "20%"}),
            action="/upload", method="post",
        ),
        style={"border": "solid 1px black", "margin": "10px", "padding": "10px"}
    )

    # Table Component
    headers = ["ID", "Name", "Date"]
    t_header = table_header(headers)

    table_com = fh.Div(
        fh.Table(
            fh.Thead(
                t_header,
                cls="text-sm uppercase bg-gray-700 text-gray-400",
            ),
            fh.Tbody(
               *[ fh.Tr(*table_row([conf["id"], conf["name"], conf["date"]] )) for conf in conferences]
            ),
            dir="rtl",
            lang="ar",
        ),
        style={
            "max-height": "450px",
            "overflow-y": "auto",
            "width": "100%",
            "display": "block",
            "position": "relative",
            'padding-right': "10px",
            'padding-left': "10px"
        }

    )

    # Return the complete page
    return fh.Div(
        header,
        fh.Container(
            upload,
            table_com,
            id="content",
        )
    )
