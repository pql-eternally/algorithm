import asyncio
import pynecone as pc


class ChainState(pc.State):
    count = 0
    show_progress = False

    def toggle_progress(self):
        self.show_progress = not self.show_progress

    async def increment(self):
        # Think really hard.
        await asyncio.sleep(0.5)
        self.count += 1


def index():
    return pc.cond(
        ChainState.show_progress,
        pc.circular_progress(is_indeterminate=True),
        pc.heading(
            ChainState.count,
            on_click=[
                ChainState.toggle_progress,
                ChainState.increment,
                ChainState.toggle_progress,
            ],
            _hover={"cursor": "pointer"},
        ),
    )
