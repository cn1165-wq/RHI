def export_dxf(data, output_path: str):
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write("0\nSECTION\n2\nHEADER\n0\nENDSEC\n0\nEOF\n")
    print(f"DXF output written to: {output_path}")
