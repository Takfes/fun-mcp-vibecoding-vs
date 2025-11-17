#!/usr/bin/env bash

# Start local MCP Hub using the repo-managed config.
# Configure secrets via environment variables before running.

mcp-hub --port 3000 --config "$HOME/.config/mcphub/mcp.json" --watch
