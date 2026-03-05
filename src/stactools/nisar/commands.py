import click


def create_nisar_command(cli: click.Group) -> click.Command:
    """
    Registers the `nisar` command on the main stactools CLI.
    """

    @cli.command("nisar", short_help="NISAR tools (namespace placeholder)")
    def nisar() -> None:
        click.echo("stactools-nisar plugin loaded")

    return nisar
