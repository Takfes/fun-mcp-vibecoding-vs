# Pokemon Database with MCP Server Access

Simple dual-database setup (PostgreSQL + MySQL) with DBHub MCP servers for VS Code integration.

## 🚀 Quick Start

### 1. Start the Stack
```bash
docker-compose up -d
```

### 2. Load Pokemon Data
```bash
python src/load_pokemon_data.py
```

### 3. Query via MCP Tools
Use VS Code's MCP tools to query databases:
- PostgreSQL: `mcp_dbhub-pg_execute_sql`  
- MySQL: `mcp_dbhub-mysql_execute_sql`

## 🏗️ Architecture

- **PostgreSQL 15**: Port 5432, DBHub MCP on 8081
- **MySQL 8.0**: Port 3306, DBHub MCP on 8082
- **Python loader**: Downloads Pokemon CSV and populates both databases

## 🔧 MCP Setup

### Docker Compose Configuration
- Two DBHub containers expose MCP servers on ports 8081/8082
- Each connects to respective database using internal Docker networking
- Read-only access enforced for safety

### VS Code MCP Configuration (`.vscode/mcp.json`)
```json
{
  "mcpServers": {
    "dbhub-pg": {
      "command": "npx",
      "args": ["-y", "@bytebase/dbhub", "--transport", "stdio", "--dsn", "postgres://pokemon_user:pokemon_pass@localhost:5432/pokemon_db?sslmode=disable", "--readonly"]
    },
    "dbhub-mysql": {
      "command": "npx", 
      "args": ["-y", "@bytebase/dbhub", "--transport", "stdio", "--dsn", "mysql://pokemon_user:pokemon_pass@localhost:3306/pokemon_db", "--readonly"]
    }
  }
}
```

## 🧹 Cleanup

```bash
# Stop containers, remove data
docker-compose down -v
```
