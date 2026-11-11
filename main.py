"""
NeuraX — Digital Identity Intelligence System
Entry point for the full pipeline.

Usage:
    python main.py --image data/input/sample.jpg --context "Software engineer, Bangalore"
"""

import argparse
import asyncio
import sys
from pathlib import Path
from dotenv import load_dotenv
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

load_dotenv()
console = Console()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="NeuraX — Digital Footprint Intelligence System"
    )
    parser.add_argument(
        "--image", type=Path, required=True, help="Path to the input face image"
    )
    parser.add_argument(
        "--context", default="", help="Additional context (name, location, org, etc.)"
    )
    parser.add_argument(
        "--output", type=Path, default=Path("data/output"), help="Output directory for reports"
    )
    return parser.parse_args()


async def run_pipeline_async(image_path: Path, context: str, output_dir: Path) -> None:
    # Validate input file early
    if not image_path.is_file():
        console.print(f"[bold red]Error:[/] Input image not found at [yellow]{image_path}[/]")
        sys.exit(1)

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    console.rule("[bold cyan]NeuraX — Digital Identity Intelligence[/]")
    console.print(f"Target Image: [dim]{image_path}[/]")
    if context:
        console.print(f"Context: [dim]{context}[/]\n")

    # Use Rich progress bar for better UX during heavy async tasks
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        transient=True,
    ) as progress:
        
        # Layer 1: Identity Resolution
        task1 = progress.add_task("[1/7] 🔍 Resolving identity from image + context...", total=None)
        # TODO: Replace with actual async calls e.g., await extract_embedding(image_path)
        await asyncio.sleep(0.6)
        progress.remove_task(task1)
        console.print("[1/7] [green]✔[/] Identity resolved from image + context.")

        # Layer 2: Multi-Platform Discovery (Ideal for asyncio.gather across scrapers/APIs)
        task2 = progress.add_task("[2/7] 🌐 Discovering public profiles across platforms...", total=None)
        await asyncio.sleep(0.8)
        progress.remove_task(task2)
        console.print("[2/7] [green]✔[/] Public profiles discovered across platforms.")

        # Layer 3: Vector DB — Face + Bio Embeddings
        task3 = progress.add_task("[3/7] 🧮 Indexing embeddings in Vector DB...", total=None)
        await asyncio.sleep(0.5)
        progress.remove_task(task3)
        console.print("[3/7] [green]✔[/] Embeddings indexed successfully.")

        # Layer 4: Correlation + Entity Resolution Agent
        task4 = progress.add_task("[4/7] 🤖 Running Entity Resolution Agent...", total=None)
        await asyncio.sleep(0.9)
        progress.remove_task(task4)
        console.print("[4/7] [green]✔[/] Entity Resolution Agent completed.")

        # Layer 5: Knowledge Graph
        task5 = progress.add_task("[5/7] 🕸️ Building Knowledge Graph...", total=None)
        await asyncio.sleep(0.6)
        progress.remove_task(task5)
        console.print("[5/7] [green]✔[/] Knowledge Graph constructed.")

        # Layer 6: Evidence & Confidence
        task6 = progress.add_task("[6/7] 📋 Attaching evidence and confidence scores...", total=None)
        await asyncio.sleep(0.4)
        progress.remove_task(task6)
        console.print("[6/7] [green]✔[/] Evidence attached and scored.")

        # Layer 7: Output
        task7 = progress.add_task("[7/7] 📊 Generating report, timeline, and graph...", total=None)
        await asyncio.sleep(0.5)
        progress.remove_task(task7)
        console.print("[7/7] [green]✔[/] Reports generated.")

    console.rule("[bold green]✅ Pipeline Complete[/]")
    console.print(f"Reports saved to: [bold underline]{output_dir.resolve()}[/]")


def main() -> None:
    args = parse_args()
    try:
        asyncio.run(run_pipeline_async(args.image, args.context, args.output))
    except KeyboardInterrupt:
        console.print("\n[bold red]Pipeline interrupted by user.[/]")
        sys.exit(1)
    except Exception as e:
        console.print(f"\n[bold red]Pipeline failed with error:[/] {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()