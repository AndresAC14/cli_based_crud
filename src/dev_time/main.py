import typer

cli = typer.Typer()


@cli.command()
def create_project(name: str):
    """
    Create a new project by given name.
    """
    print(f"Hello {name}")


@cli.command()
def summary():
    pass

def main():
    """Main entrypoint of the CLI"""
    cli()

if __name__ == "__main__":
    main()