import reflex as rx


def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "vikusS3dev",
            height="40px",
        ),
        position="sticky",
        bg="black",
        padding_x="16px",
        padding_y="8px",
        z_index="999",
    )