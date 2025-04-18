

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
cd bot_crawler
```
   
### 🤖 Simple Telegram Bot Setup with `.env`

This project shows how to securely load your Telegram Bot token from a `.env` file using Python.



### 🔐 Setting Up Your Bot Token

Create (or paste) a `.env` file in the root of your project and add your Telegram bot token like this:

```env
TOKEN=your_telegram_bot_token_here
```
## 🐳 Run APP
_Download Docker:_ https://docs.docker.com/engine/install/

```bash
./run_deploy.sh
```


## 👁‍ Test
To test the bot, you can use the file tests/example.xls and send it to the bot in Telegram.
This is a minimal viable product that reliably handles user input. Future versions may implement features such as currency detection, user authentication, payment integration, and more.

##### 🐞 BUGS
There are minor issues with loading the average prices by site — the calculation works fine and usually succeeds on the second attempt.