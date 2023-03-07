"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

from .q02_counter_app import index as counter_page, State as CounterState

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    """The app state."""

    pass


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Welcome to Pynecone!", font_size="2em"),
            pc.box("Get started by editing ", pc.code(filename, font_size="1em")),
            pc.link(
                "Check out our docs!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": "rgb(107,99,246)",
                },
            ),
            spacing="1.5em",
            font_size="2em",
        ),
        padding_top="10%",
    )


def custom():
    return pc.text("Custom Router")


def nested_page():
    return pc.text("Nested Page")


class PostState(pc.State):
    @pc.var
    def post_id(self):
        return self.get_query_params().get("pid", "no pid")

    @pc.var
    def current_page(self):
        return self.get_current_page()

    @pc.var
    def token(self):
        return self.get_token()


def post():
    """A page that updates based on the route."""
    return pc.vstack(
        pc.text(PostState.post_id),
        pc.text(PostState.current_page),
        pc.text(PostState.token),
    )


class ColorPicker(pc.Component):
    library = "react-colorful"
    tag = "HexColorPicker"
    color: pc.Var[str]

    @classmethod
    def get_controlled_triggers(cls) -> dict[str, pc.Var]:
        return {"on_change": pc.EVENT_ARG}


class ColorPickerState(pc.State):
    color: str = "#db114b"


def color_picker_page():
    color_picker = ColorPicker.create
    return pc.box(
        pc.vstack(
            pc.heading(ColorPickerState.color),
            color_picker(
                on_change=ColorPickerState.set_color
            ),
        ),
        background_color=ColorPickerState.color,
        padding="5em",
        border_radius="1em",
    )


async def api_test(item_id: int):
    return {"my_result": item_id}


# Add state and page to the app.
app = pc.App(state=ColorPickerState)
app.add_page(index)
# app.add_page(counter_page, route="/counter")
app.add_page(custom, route="/custom-router")
app.add_page(nested_page, route="/nested/page")
app.add_page(post, route="/post/[pid]")
app.add_page(color_picker_page, route="/color-picker")
app.api.add_api_route("/api-test/{item_id}", api_test)
app.compile()
