# mcphub Configuration (Redacted)

This folder contains a redacted, repo-safe copy of your local `~/.config/mcphub` configuration. It is intended to help you version and share your MCP Hub setup **without** committing any real API keys, tokens, or other secrets.

## Files

- `mcp.json` – MCP Hub server configuration with placeholders and environment variable references instead of real secrets.
- `start_mcp_hub.sh` – Helper script to start `mcp-hub` on port 3000.
- `start_ngrok.sh` – Helper script to expose the local MCP Hub via `ngrok`.

## Secrets and Environment Variables

All sensitive values (API keys, tokens, client secrets, etc.) have been replaced with environment-variable placeholders, for example:

- `BRAVE_API_KEY` → `${BRAVE_API_KEY}`
- `FIRECRAWL_API_KEY` → `${FIRECRAWL_API_KEY}`
- `GITHUB_PERSONAL_ACCESS_TOKEN` → `${GITHUB_PERSONAL_ACCESS_TOKEN}` (if you enable the GitHub server)
- `NOTION_API_TOKEN` → `${NOTION_API_TOKEN}` (if you enable the Notion server)
- `N8N_API_URL` / `N8N_API_KEY` → `${N8N_API_URL}` / `${N8N_API_KEY}`
- `YUTU_CREDENTIAL_PATH` / `YUTU_CACHE_TOKEN_PATH` → filesystem paths to your local credential files
- `YOUTUBE_API_KEY`, `YOUTUBE_CLIENT_ID`, `YOUTUBE_CLIENT_SECRET`, `YOUTUBE_REFRESH_TOKEN` → corresponding YouTube credentials (if you enable the YouTube server)

These environment variables must be set **outside** of version control, e.g. in your shell profile, a local `.env` file, or your editor/terminal configuration.

Example (bash/zsh):

```bash
export BRAVE_API_KEY="your-brave-api-key"
export FIRECRAWL_API_KEY="your-firecrawl-api-key"
export GITHUB_PERSONAL_ACCESS_TOKEN="your-github-token"
export NOTION_API_TOKEN="your-notion-token"
export N8N_API_URL="https://your-n8n-instance.com"
export N8N_API_KEY="your-n8n-api-key"
export YUTU_CREDENTIAL_PATH="$HOME/.config/yutu/client_secret_yutu.json"
export YUTU_CACHE_TOKEN_PATH="$HOME/.config/yutu/youtube.token.json"
```

## Using This Config

1. Copy `mcp.json` into your local config directory if needed:

   ```bash
   mkdir -p "$HOME/.config/mcphub"
   cp mcphub/mcp.json "$HOME/.config/mcphub/mcp.json"
   ```

2. Set the required environment variables (as shown above) with your **real** keys and tokens.

3. Start the MCP Hub:

   ```bash
   cd /path/to/this/repo
   chmod +x mcphub/start_mcp_hub.sh mcphub/start_ngrok.sh
   ./mcphub/start_mcp_hub.sh
   ```

4. (Optional) Expose the hub via ngrok:

   ```bash
   ./mcphub/start_ngrok.sh
   ```

## Safety Notes

- Do **not** commit actual API keys, tokens, or private URLs to this repo.
- If you add new MCP servers that require secrets, follow the same pattern: add env-var placeholders in `mcp.json` and set real values only in your local environment.
