class CockpitException(Exception):
    """Base Cockpit exception"""

    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        return super().__str__()
