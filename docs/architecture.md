# RHI architecture notes

## Overview
RHI is designed to convert 3D model files into enterprise-standard engineering drawings using configurable rules.

## Core Layers
- Geometry layer: parse and understand model structure
- Drawing layer: create 2D views, sections, and annotations
- Rule layer: apply custom company standard marking
- Export layer: generate DXF, SVG, and PDF outputs

## MVP Stage
The initial version focuses on:
1. reading a STEP file
2. generating basic drawing views
3. applying enterprise rules
4. exporting a DXF placeholder output

## Future Work
- model validation and repair
- dimension generation
- multi-view generation
- API/service-based processing
- industrial-scale CAD kernel enhancement
