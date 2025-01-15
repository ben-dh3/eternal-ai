# Use ZerePy framework with EternalAI API

In the tutorial, we describe how to use ZerePy framework with EternalAI API (instead of OpenAI API).

## Prerequisites

* Python 3.10 or higher
* Poetry 1.5 or higher

## Step 1

Clone the repository.

```
https://github.com/blorm-network/ZerePy
```

## Step 2

Go to the `zerepy` directory and install dependencies.

```
cd zerepy && poetry install --no-root
```

This will create a virtual environment and install all required dependencies.

## Step 3

Activate the virtual environment.

```
poetry shell
```

## Step 4

Run the application.

```
poetry run python main.py
```

You will see the following output in your terminal.

```
--------------------------------------------------------------------
👋 Welcome to the ZerePy CLI!
Type 'help' for a list of commands.
--------------------------------------------------------------------

✅ Successfully loaded agent: ExampleAgent

Start the agent loop with the command 'start' or use one of the action commands.

AVAILABLE CONNECTIONS:
- twitter: ❌ Not Configured
- openai: ❌ Not Configured
- anthropic: ❌ Not Configured
ZerePy-CLI (ExampleAgent) >
```

## Step 5

In the previous step, the `ExampleAgent`is loaded by default, we will need to load `eternalai-example` agent for using with EternalAI API.

First, list all available agents.

```
ZerePy-CLI (ExampleAgent) > agents
```

You will see the following agents in your terminal.

```
Available Agents:
- eternalai-example
- example
```

Next, load the `eternalai-example` agent.

```
ZerePy-CLI (ExampleAgent) > load-agent eternalai-example

✅ Successfully loaded agent: EternalAI
```

## Step 6

Configure EternalAI connection.

```
ZerePy-CLI (EternalAI) > configure-connection eternalai
```

Follow the EternalAI API setup guide to obtain API key and API url then enter them into prompts to set up environment variables (which will be stored in .env file).

```
🤖 EternalAI API SETUP

📝 To get your EternalAI API credentials:
1. Go to https://eternalai.org/api
2. Generate an API Key
3. Use API url as https://api.eternalai.org/v1/

Enter your EternalAI API key:

Enter your EternalAI API url:
```

Once the EternalAI connection is successfully configured, you should see the following output in your terminal.

```
HTTP Request: GET https://api.eternalai.org/v1/models "HTTP/1.1 200 OK"

✅ EternalAI API configuration successfully saved!
Your API key has been stored in the .env file.

✅ SUCCESSFULLY CONFIGURED CONNECTION: eternalai
```

## Step 7

Configure Twitter connection.

```
ZerePy-CLI (EternalAI) > configure-connection twitter
```

Follow the Twitter authentication setup guide to obtain API Key (consumer key) and API Key Secret (consumer secret)  then enter them into prompts to sett up environment variables (which will be stored in .env file).

```
Starting Twitter authentication setup

🐦 TWITTER AUTHENTICATION SETUP

📝 To get your Twitter API credentials:
1. Go to https://developer.twitter.com/en/portal/dashboard
2. Create a new project and app if you haven't already
3. In your app settings, enable OAuth 1.0a with read and write permissions
4. Get your API Key (consumer key) and API Key Secret (consumer secret)
--------------------------------------------------------------------

Please enter your Twitter API credentials:
Enter your API Key (consumer key):
Enter your API Key Secret (consumer secret):
Starting OAuth authentication process...

1. Please visit this URL to authorize the application:
2. After authorizing, Twitter will give you a PIN code.
3. Please enter the PIN code here: 

✅ Twitter authentication successfully set up!
Your API keys, secrets, and user ID have been stored in the .env file.

✅ SUCCESSFULLY CONFIGURED CONNECTION: twitter
```

## Step 8

Add `TWITTER_USERNAME` environment variable to the .env file. (You need to exit the current process prior to adding)

```
TWITTER_USERNAME="your-twitter-username"
```

## Step 9

Rerun the application.

```
poetry shell

poetry run python main.py
 
ZerePy-CLI (ExampleAgent) > load-agent eternalai-example

ZerePy-CLI (EternalAI) > start
```

Your agent should read the timeline and reply to a post as shown below.

```
HTTP Request: GET https://api.eternalai.org/v1/models "HTTP/1.1 200 OK"

🚀 Starting agent loop...
Press Ctrl+C at any time to stop the loop.
--------------------------------------------------------------------
Starting loop in 5 seconds...
5...
4...
3...
2...
1...

👀 READING TIMELINE

💬 GENERATING REPLY to: Merry Christmas and may you have a wonderful New Y...
HTTP Request: GET https://api.eternalai.org/v1/models "HTTP/1.1 200 OK"
model unsloth/Llama-3.3-70B-Instruct-bnb-4bit
HTTP Request: POST https://api.eternalai.org/v1/chat/completions "HTTP/1.1 200 OK"

🚀 Posting reply: '"Wishing you a holiday season filled with joy, love and all your favorite things, and a New Year that's bright and beautiful!"'
Reply posted successfully
✅ Reply posted successfully!

⏳ Waiting 900 seconds before next loop...
```

Onchain transactions for the prompt request and response:

* Prompt request: [https://basescan.org/tx/0x087ae3ece5b19c312d16beaea52dccffab8f3ebc34542d036fe193f54c2ba8c3](https://basescan.org/tx/0x087ae3ece5b19c312d16beaea52dccffab8f3ebc34542d036fe193f54c2ba8c3)
* Response: [https://basescan.org/tx/0x3153addd700bd5a8b76328502ac923744b21f6f5f22bfd38f580185adc805210](https://basescan.org/tx/0x3153addd700bd5a8b76328502ac923744b21f6f5f22bfd38f580185adc805210)[\
  ](https://basescan.org/tx/0x087ae3ece5b19c312d16beaea52dccffab8f3ebc34542d036fe193f54c2ba8c3)
