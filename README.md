# RHI

RHI is a rule-driven 3D model to drawing generation platform.

## Overview
RHI converts 3D model files such as STEP, STL, IGES, and IFC into internal engineering drawings using configurable enterprise rules. It is designed to support custom annotations, model feature marking, and automated drawing generation for industrial scenarios.

## Project Goal
The project aims to automate the transition from 3D geometry to 2D engineering drawings while preserving company-specific standards.

## Key Capabilities
- Read 3D model files
- Extract geometric structure and key views
- Generate drawing layouts
- Apply enterprise-specific annotation rules
- Mark special features and custom labels
- Export to DXF, SVG, and PDF

## Supported Inputs
- STEP
- STL
- IGES
- OBJ
- IFC

## Supported Outputs
- DXF
- SVG
- PDF

## Tech Stack
- Python
- pythonocc-core
- CadQuery
- ezdxf
- PyYAML
- svgwrite
- reportlab

## Current Status
Prototype stage.

The project currently focuses on building a minimal workflow:
STEP input -> geometry parsing -> drawing generation -> export.

## Architecture
- core/geometry: model parsing and geometry handling
- core/drawing: view generation and drawing logic
- core/rules: rule-based annotation and enterprise tagging
- exporters: drawing export layer
- config: YAML-based rule and template configuration

## Quick Start
1. Install dependencies:
   pip install -r requirements.txt

2. Prepare a model file.

3. Run the app:
   python app/main.py --input examples/sample.step --output output/demo.dxf --rules config/enterprise_rules.yaml

## Roadmap
- MVP: basic STEP import and view generation
- Rule engine: custom enterprise marking
- Multi-view generation: front, section, detail
- Dimension and annotation automation
- Batch file processing
- API service and background job system
- Industrial-scale geometric enhancement with OCCT/C++ later

## Notes
This project is focused on automated drafting and rule-driven drawing generation rather than simple format conversion.
