import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from pathlib import Path
import json

console = Console()


def display_game_result(result):
    """Display game result with Rich formatting."""
    table = Table(title="Game Result", show_header=True)
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Outcome", "VICTORY" if result.victory else "DEFEAT")
    table.add_row("Rounds Played", str(result.rounds_played))
    table.add_row("Investigators Survived", ", ".join(result.investigators_survived))
    table.add_row("Investigators Defeated", ", ".join(result.investigators_defeated))
    table.add_row("Damage Taken", str(result.damage_taken))
    table.add_row("Horror Taken", str(result.horror_taken))

    console.print(table)
    console.print(f"\nLog saved to: {result.log_path}")


def display_investigator(investigator):
    """Display investigator info."""
    panel = Panel(
        f"[bold]{investigator.name}[/bold] - {investigator.title}\n"
        f"Class: {investigator.class_name}\n"
        f"WIL: {investigator.willpower} | INT: {investigator.intellect} | "
        f"COM: {investigator.combat} | AGI: {investigator.agility}\n"
        f"HP: {investigator.health}/{investigator.health_max} | "
        f"SAN: {investigator.sanity}/{investigator.sanity_max}",
        title="Investigator"
    )
    console.print(panel)


def display_scenario(scenario):
    """Display scenario info."""
    console.print(Panel(
        f"[bold]{scenario.scenario_name}[/bold]\n"
        f"Current Agenda: {scenario.current_agenda.name}\n"
        f"Current Act: {scenario.current_act.name}",
        title="Scenario"
    ))
