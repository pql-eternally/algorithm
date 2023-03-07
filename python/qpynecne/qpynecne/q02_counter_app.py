import pynecone as pc


class State(pc.State):
    count: int = 0
    text: str = "Hello World"
    color: str = "red"
    value: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def flip_color(self):
        if self.color == "red":
            self.color = "blue"
        else:
            self.color = "red"


def index():
    return pc.hstack(
        pc.button(
            "Decrement",
            color_scheme="red",
            border_radius="1em",
            on_click=State.decrement,
        ),
        pc.heading(State.count, font_size="2em"),
        pc.button(
            "Increment",
            color_scheme="green",
            border_radius="1em",
            on_click=State.increment,
        ),
        pc.button(
            "Fancy Button",
            border_radius="1em",
            box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
            background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
            box_sizing="border-box",
            color="white",
            _hover={
                "opacity": 0.85,
            },
        ),
        pc.badge(
            State.text,
            color_scheme=State.color,
            on_click=State.flip_color,
            font_size="1.5em",
            _hover={
                "cursor": "pointer",
            },
        ),
        pc.slider(
            on_change_end=State.set_value,
            color_scheme=pc.cond(
                State.value > 50, "green", "pink"
            ),
        )
    )
