from dataacquisition.views.first_view import Command, introduction_page


def introduction_process() -> Command:
    command = introduction_page()
    return command
