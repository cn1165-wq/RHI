import argparse

from core.drawing.view_generator import generate_views
from core.geometry.step_reader import read_step
from core.rules.rule_engine import apply_rules
from exporters.dxf_exporter import export_dxf


def main():
    parser = argparse.ArgumentParser(description="RHI drawing generation entry point")
    parser.add_argument("--input", required=True, help="Input 3D model file")
    parser.add_argument("--output", required=True, help="Output file path")
    parser.add_argument("--rules", default="config/enterprise_rules.yaml", help="Rule config path")
    args = parser.parse_args()

    model = read_step(args.input)
    views = generate_views(model)
    data = apply_rules(views, args.rules)
    export_dxf(data, args.output)

    print(f"Input file: {args.input}")
    print(f"Output file: {args.output}")
    print(f"Rules: {args.rules}")


if __name__ == "__main__":
    main()
