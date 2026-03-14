# Security Features Discord Bot

A powerful Discord bot designed to interact with GitHub repositories and provide security-focused commands. This bot helps developers monitor vulnerabilities, check security policies, and manage repository security settings directly from Discord.

## Features

- **Vulnerability Scanning**: Check for known vulnerabilities in repositories
- **Security Policy Verification**: Verify security policies and best practices
- **Dependency Analysis**: Analyze project dependencies for security issues
- **License Compliance**: Check license compliance of dependencies
- **Security Alerts**: Monitor and display GitHub security alerts
- **Repository Insights**: Get security insights about GitHub repositories
- **Audit Logging**: Track security-related actions in Discord

## Requirements

- Python 3.9+
- discord.py
- PyGithub
- python-dotenv
- aiohttp

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jackeerthana/security-discord-bot.git
cd security-discord-bot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your credentials:
```env
DISCORD_TOKEN=your_discord_bot_token
GITHUB_TOKEN=your_github_personal_access_token
```

4. Run the bot:
```bash
python main.py
```

## Commands

### Security Commands
- `/scan-repo [owner/repo]` - Scan a repository for vulnerabilities
- `/check-vulnerabilities [owner/repo]` - Check for known vulnerabilities
- `/analyze-dependencies [owner/repo]` - Analyze project dependencies
- `/security-policy [owner/repo]` - Verify security policy existence
- `/license-check [owner/repo]` - Check license compliance

### Repository Commands
- `/repo-info [owner/repo]` - Get repository security information
- `/security-alerts [owner/repo]` - Display security alerts
- `/contributors [owner/repo]` - List repository contributors

### Configuration
- `/set-repo [owner/repo]` - Set default repository for commands
- `/list-repos` - List monitored repositories

## Configuration

Edit `config.json` to customize:
- Bot prefix
- Default scanning depth
- Alert thresholds
- Logging settings

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and feature requests, please open an issue on GitHub.