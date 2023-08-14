# Shitter.ch

Shitter is an anonymous, no-account free and open source social media created by **canard**, **gugu256** and **rapha1004**

Its goal is to provide a place for people to talk without censor & without an algorithm controlling what they see and think.

They are only basic features like:

- Posting
- Replying to to posts
- Commenting
- Liking

And thats it!

## API

Shitter.ch has a basic read-only API with 4 endpoints:

- `shitter.ch/api/posts`     returns the whole JSON database of all the posts
- `shitter.ch/api/lastpost`  returns the JSON of the last post
- `shitter.ch/api/recent/5`  returns the last 5 posts in JSON format (you are free to change the number if you want to get more or less posts)
- `shitter.ch/api/post/<id>` returns the JSON format of a specific post using it's id.

Feel free to experiment with it !