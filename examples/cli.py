#!/usr/bin/env python3
"""
Example CLI implementation showing patterns for argument parsing,
error handling, and output formatting.
"""

import click
import json
import sys
from typing import Dict, Any, Optional
from pathlib import Path


@click.command()
@click.argument('input_path', type=click.Path(exists=True, path_type=Path))
@click.option('--output', '-o', type=click.Path(path_type=Path), 
              help='Output file path')
@click.option('--format', '-f', type=click.Choice(['json', 'csv', 'table']),
              default='table', help='Output format')
@click.option('--verbose', '-v', is_flag=True, help='Verbose output')
@click.option('--dry-run', is_flag=True, help='Show what would be done')
def analyze(input_path: Path, output: Optional[Path], format: str, 
           verbose: bool, dry_run: bool):
    """Analyze a directory or file and generate a report."""
    
    try:
        # Input validation
        if not input_path.exists():
            click.echo(f"Error: {input_path} does not exist", err=True)
            sys.exit(1)
            
        if verbose:
            click.echo(f"Analyzing: {input_path}")
            
        # Perform analysis
        results = perform_analysis(input_path, verbose=verbose, dry_run=dry_run)
        
        # Output results
        output_results(results, output, format, verbose)
        
        if verbose:
            click.echo("Analysis complete!")
            
    except KeyboardInterrupt:
        click.echo("\nAnalysis interrupted by user", err=True)
        sys.exit(130)
    except Exception as e:
        click.echo(f"Error during analysis: {e}", err=True)
        if verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


def perform_analysis(path: Path, verbose: bool = False, 
                    dry_run: bool = False) -> Dict[str, Any]:
    """Perform the actual analysis logic."""
    
    if dry_run:
        if verbose:
            click.echo("DRY RUN: Would analyze files...")
        return {"dry_run": True, "path": str(path)}
    
    # Simulate analysis with progress bar
    files = list(path.rglob("*.py")) if path.is_dir() else [path]
    
    results = {
        "path": str(path),
        "total_files": len(files),
        "analysis": {}
    }
    
    with click.progressbar(files, label="Analyzing files") as file_list:
        for file_path in file_list:
            # Simulate analysis work
            results["analysis"][str(file_path)] = {
                "lines": 42,  # Mock data
                "functions": 3,
                "complexity": 2.5
            }
    
    return results


def output_results(results: Dict[str, Any], output_path: Optional[Path], 
                  format: str, verbose: bool):
    """Output results in the specified format."""
    
    if format == 'json':
        output_json(results, output_path)
    elif format == 'csv':
        output_csv(results, output_path)
    else:
        output_table(results, output_path)


def output_json(results: Dict[str, Any], output_path: Optional[Path]):
    """Output results as JSON."""
    json_str = json.dumps(results, indent=2)
    
    if output_path:
        output_path.write_text(json_str)
        click.echo(f"Results saved to {output_path}")
    else:
        click.echo(json_str)


def output_csv(results: Dict[str, Any], output_path: Optional[Path]):
    """Output results as CSV."""
    # This is a simplified example
    csv_lines = ["file,lines,functions,complexity"]
    
    for file_path, data in results.get("analysis", {}).items():
        csv_lines.append(f"{file_path},{data['lines']},{data['functions']},{data['complexity']}")
    
    csv_content = "\n".join(csv_lines)
    
    if output_path:
        output_path.write_text(csv_content)
        click.echo(f"Results saved to {output_path}")
    else:
        click.echo(csv_content)


def output_table(results: Dict[str, Any], output_path: Optional[Path]):
    """Output results as a formatted table."""
    
    table_lines = [
        "File Analysis Results",
        "=" * 50,
        f"Total files: {results.get('total_files', 0)}",
        f"Path: {results.get('path', 'Unknown')}",
        "",
        "Files analyzed:",
    ]
    
    for file_path, data in results.get("analysis", {}).items():
        table_lines.append(f"  {file_path}: {data['lines']} lines, {data['functions']} functions")
    
    table_content = "\n".join(table_lines)
    
    if output_path:
        output_path.write_text(table_content)
        click.echo(f"Results saved to {output_path}")
    else:
        click.echo(table_content)


if __name__ == '__main__':
    analyze()
