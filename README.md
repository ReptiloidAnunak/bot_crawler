

# 🧿 Zyuzublik Parser Bot

This project is a simple Telegram bot that allows users to upload Excel files with websites to parse "zyuzubliks" (or other products). The bot stores the data in a SQLite database and can optionally parse prices to calculate the average price per source.

## 📦 Features

- Upload Excel files with product URLs and XPATH selectors for prices
- Store the data in a local SQLite database
- Display uploaded table content back to the user
- *(Optional)* Parse product prices and calculate the average price per source

## 💡 Excel File Format

The file must contain the following columns:

| title               | url                                                                                 | xpath                                           |
|--------------------|--------------------------------------------------------------------------------------|------------------------------------------------|
| Chocolate Postcard | http://шоколадная-лавка.рф/index.php?route=product/product&path=61&product_id=136   | /html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/span |

**Note:** Price values may contain spaces, currency symbols, etc. – the parser takes this into account.

## 🚀 Getting Started

### 🌐 Clone the Repository

```bash
git clone https://github.com/ReptiloidAnunak/bot_crawler.git
```
## 🚀 Installing Docker (if not already installed)

If you don't have Docker installed, follow the steps below to install it on your system.

### 🖥️ Windows

1. **Download Docker Desktop for Windows**:  
   Go to [Docker's official website](https://www.docker.com/products/docker-desktop) and download the Docker Desktop installer for Windows.

2. **Run the installer**:  
   After downloading, run the installer and follow the on-screen instructions.

3. **Enable WSL 2 (Windows Subsystem for Linux)**:  
   Docker Desktop for Windows requires WSL 2 to run Linux containers. Follow the instructions from Docker to install and configure WSL 2. You can find the guide [here](https://docs.microsoft.com/en-us/windows/wsl/install).

4. **Start Docker**:  
   After installation, open Docker Desktop from the Start Menu, and it will automatically start running. You might need to sign in with a Docker Hub account (create one if you don’t have one).

5. **Verify Installation**:  
   Open a terminal (PowerShell or Command Prompt) and run the following command to verify Docker is installed correctly:

   ```bash
   docker --version
   
### 🤖 Simple Telegram Bot Setup with `.env`

This project shows how to securely load your Telegram Bot token from a `.env` file using Python.



### 🔐 Setting Up Your Bot Token

Create (or paste) a `.env` file in the root of your project and add your Telegram bot token like this:

```env
TOKEN=your_telegram_bot_token_here
```

## 👁‍ Test
To test the bot, you can use the file tests/example.xls and send it to the bot in Telegram.
This is a minimal viable product that reliably handles user input. Future versions may implement features such as currency detection, user authentication, payment integration, and more.