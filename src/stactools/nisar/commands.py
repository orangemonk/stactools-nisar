import click


def create_nisar_command(cli: click.Group) -> click.Command:
    """
    Register the `nisar` command group on the main stactools CLI.

    This is intentionally a group (not a single command) so we can add
    subcommands later, e.g. `stac nisar create-item ...`.
    """

    @cli.group("nisar", invoke_without_command=True, short_help="NISAR tools")
    @click.option(
        "--version",
        is_flag=True,
        help="Print the stactools-nisar plugin version and exit.",
    )
    @click.pass_context
    def nisar(ctx: click.Context, version: bool) -> None:
        try:
            if version:
                from stactools.nisar import __version__

                click.echo(__version__)
                return

            # Stub behavior for namespace-claim release.
            if ctx.invoked_subcommand is None:
                click.echo("stactools-nisar plugin loaded")

        except Exception as e:
            # Avoid dumping stack traces for end users; surface a clean message.
            raise click.ClickException(str(e)) from e

    return nisar
