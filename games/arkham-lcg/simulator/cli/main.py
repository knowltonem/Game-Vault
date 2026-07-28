import click
import json
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import sys

# Add parent to path for imports when run as script
sys.path.insert(0, str(Path(__file__).parent.parent))
from engine.game import Game
from cli.display import display_game_result, display_investigator

console = Console()

@click.group()
def cli():
    """Arkham Horror LCG Simulator"""
    pass

@cli.command()
@click.option('--investigator', '-i', required=True, help='Investigator ID (e.g., abel_redcloud, nora_warwick)')
@click.option('--scenario', '-s', required=True, help='Scenario ID (e.g., spreading_flames)')
@click.option('--difficulty', '-d', default='standard', help='Difficulty level (easy, standard, hard)')
@click.option('--rounds', '-r', default=50, help='Maximum number of rounds')
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose logging')
@click.option('--games', '-n', default=1, help='Number of games to simulate')
def simulate(investigator, scenario, difficulty, rounds, verbose, games):
    """Run game simulation(s)."""
    inv_ids = [i.strip() for i in investigator.split(',')]

    if games == 1:
        game = Game(investigator_ids=inv_ids, scenario_id=scenario, difficulty=difficulty)
        result = game.run(max_rounds=rounds)
        display_game_result(result)
    else:
        wins = 0
        total_rounds = 0
        for i in range(games):
            game = Game(investigator_ids=inv_ids, scenario_id=scenario, difficulty=difficulty)
            result = game.run(max_rounds=rounds)
            if result.victory:
                wins += 1
            total_rounds += result.rounds_played

        table = Table(title=f"Monte Carlo Results ({games} games)")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")
        table.add_row("Win Rate", f"{wins}/{games} ({wins/games*100:.1f}%)")
        table.add_row("Avg Rounds", f"{total_rounds/games:.1f}")
        console.print(table)

@cli.command()
def list_investigators():
    """List all available investigators."""
    data_dir = Path(__file__).parent.parent / "data" / "investigators"
    if not data_dir.exists():
        console.print("[red]No investigators found[/red]")
        return

    table = Table(title="Available Investigators")
    table.add_column("ID", style="cyan")
    table.add_column("Name", style="green")
    table.add_column("Class", style="yellow")

    for f in data_dir.glob("*.json"):
        with open(f) as fh:
            data = json.load(fh)
            table.add_row(f.stem, data.get("name", ""), data.get("class", ""))

    console.print(table)

@cli.command()
def list_scenarios():
    """List all available scenarios."""
    data_dir = Path(__file__).parent.parent / "data" / "scenarios"
    if not data_dir.exists():
        console.print("[red]No scenarios found[/red]")
        return

    table = Table(title="Available Scenarios")
    table.add_column("ID", style="cyan")
    table.add_column("Name", style="green")
    table.add_column("Cycle", style="yellow")

    for f in data_dir.glob("*.json"):
        with open(f) as fh:
            data = json.load(fh)
            table.add_row(f.stem, data.get("name", ""), data.get("cycle", ""))

    console.print(table)

@cli.command()
@click.option('--investigator', '-i', required=True, help='Investigator ID')
def show_investigator(investigator):
    """Show detailed investigator information."""
    data_dir = Path(__file__).parent.parent / "data" / "investigators"
    filepath = data_dir / f"{investigator}.json"

    if not filepath.exists():
        console.print(f"[red]Investigator not found: {investigator}[/red]")
        return

    with open(filepath) as f:
        data = json.load(f)

    game = Game(investigator_ids=[investigator], scenario_id="spreading_flames")
    inv = game.game_state.get_investigator(investigator)
    display_investigator(inv)

if __name__ == '__main__':
    cli()
