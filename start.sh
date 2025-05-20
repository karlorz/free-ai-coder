#!/bin/bash

# Start Jupyter Enterprise Gateway
uv run jupyter enterprisegateway --port 8889 &

# Wait for a few seconds to allow the gateway to start
sleep 2

# Start Streamlit app
uv run streamlit run app.py --server.port=8000