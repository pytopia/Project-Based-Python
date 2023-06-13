<img src="./images/instagram-bot.png" width="700"/>

# Instagram Message Bot
> DIFFICULTY: **INTERMEDIATE**

Millions use instagram to communicate with their friends, own a small business and even do reels to show off their talent. Now automating messages in any platform is just writing a simple code to ‘automatically’ send messages or images to any person or a database, it can be anything. Here we will see one way of sending messages automatically to an instagram user after a timeout. So let’s start the project to Automate Instagram Messages using Python.

In this Python project we use **selenium**, **requests**, **beautifulSoup4** and **time** modules to scrape the website 'https://bestlifeonline.com/one-liner-jokes/' and extract a joke form it to sent to the instagram id.
You need to have a function for login to your instagram account.

## TODO

1. From **selenium** import **webdriver**
2. Import other modules which you need.
3. Open the website with **request** module to scrape the jokes from.
4. Use **beautiful soup** module for html parsing.
5. Choose a random joke number with **random** module.
6. Extract the random joke from the html of the website.
7. Open the **webdriver** module and use it for autonomous control
8. Define a function for login to the instagram.
9. Define a function to find messages button in instagram and the chat of the intended person.
10. Define a function to find the text area in the chat to send message.