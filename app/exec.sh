#!/bin/bash
source /app/eo-s1-workflow-venv/bin/activate
cd /app/workflows
PYTHONPATH='.' luigi --module process_s1_scene Cleanup "$@" --removeSourceFile --local-scheduler
