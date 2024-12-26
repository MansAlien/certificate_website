from fasthtml import common as fh


def home_get():
    header = fh.Nav(
        fh.Ul(
            fh.Li( fh.A( fh.Strong("NRCT"), href="/", cls="contrast"))
        ),
        fh.Ul(
            fh.Li(fh.A("About", href="#", cls='contrast')),
            fh.Li(fh.A("Services", href="#", cls='contrast')),
            fh.Li(fh.A("products", href="#", cls='contrast')),
        ),
        style={"padding":"30px", "background-color": "black", },
        id="header"
    )
    home = fh.Title("Home"),fh.Div(
        fh.Form(
            fh.Input(id="file", type="file", name="file"),
            fh.Button("upload", type="submit", style={"width": "20%"}),
            action="/upload", method="post",
        ),
        style={"border":"solid 1px black", "margin":"10px", "padding":"10px"}
    )
    return fh.Div(
        header,
        fh.Container( 
            home,
            id="content",
        )
    )

