__version__ = "0.0.1"


def register_plugin(registry) -> None:
    """
    Plugin hook discovered by stactools.

    stactools scans the `stactools` namespace package and calls
    register_plugin(registry) when present.
    """
    from stactools.nisar.commands import create_nisar_command

    registry.register_subcommand(create_nisar_command)
