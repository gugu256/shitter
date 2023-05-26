from flask import Flask, request, render_template
import random
from datetime import datetime
from tinydb import TinyDB, Query
from replit import db as debe

db = TinyDB('database.json')
 
app = Flask("Shitter")
users = TinyDB("users.json")
users_table = users.table('users')

@app.route('/', methods=["GET"])
def home():
  if request.remote_addr in open("ipdb").read():
    pass
  else:
    open("ipdb", "a").write(str(request.remote_addr) + "\n")
  return return_website()

def return_website():
  posts = list(reversed(TinyDB('database.json').all()))
  postscode = ""
  htmlcode = open("index.html").read()
  for post in range(0, len(posts)):
    try:

      postscode += '<a href="https://shitter.ch/post/'+ posts[post]["id"] +'"> <li style="font-size: 20px; border: 2px solid #BCB1AE; border-radius: 5px; margin-top: 70px; margin-right: 70px; margin-bottom: 10px; margin-left: 70px; padding: 30px; overflow: hidden;"><u>' + posts[post]["pseudo"] + "<br /><br /></u>" + posts[post]["content"] + "<br /><br />❤️" + str(posts[post]["likes"]) + "<br /><p style='font-size: 12; font-color: grey;'> <span id='postdate' style='font-size: 8'>" + posts[post]["date"] +"</span></a></p></li>" 
    except KeyError:
      postscode += "<li style="">" + posts[post]["content"] + "</li><br />" 
  htmlcode = htmlcode.replace("{{POSTS}}", postscode)
  return htmlcode

def redirect():
  return '<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0; url=\'https://shitter.ch/\'" /></head><body></body></html>'

@app.route("/404")
def error404():
    htmlcode = open("404.html").read()
    return htmlcode

@app.route("/gotosignup")
def gotosignup():
    htmlcode = open("signup.html").read()
    return htmlcode

@app.route("/gotomakepost")
def gotomakepost():
    htmlcode = open("makepost.html").read()
    return htmlcode

@app.route("/gotomainpage")
def gotomainpage():
    htmlcode = open("index.html").read()
    return htmlcode 

@app.route("/about")
def about():
    htmlcode = open("about.html").read()
    return htmlcode

@app.route("/leaderboard")
def leaderboard():
    htmlcode = open("posts.html").read()
    users = debe.keys()
    leaderboarddb = {}
    for user in users:
        leaderboarddb[user] = debe[user]
    sorted_keys = sorted(leaderboarddb.keys(), key=lambda x: leaderboarddb[x], reverse=True)
    htmlcode += "<h2><li><b><u>" + sorted_keys[0] + "</u></b> is on the top of the podium with a total of " + str(leaderboarddb[sorted_keys[0]]) + " posts !</li></h2>"
    for usr in range(1, len(sorted_keys)):
        htmlcode += "<li><u>" + sorted_keys[usr] + "</u> : " + str(leaderboarddb[sorted_keys[usr]]) + " posts </i>"
    htmlcode = htmlcode.replace("{{CSS}}", "<style>" + open("style.css").read() + "</style>")
    htmlcode += "</body>"
    htmlcode += "<html><footer><p>Created by Platypus Studio and Krayse</p></html></footer>"
    return htmlcode

@app.route("/postsdb")
def ips():
  return open("database.json").read()

def stylize(text):
  
  text = text.replace("<script>", 'User tried to hack shitter.ch with this code : </b>\\n\\n')
  text = text.replace("<img>", 'User tried to hack shitter.ch with a weird image')
  text = text.replace("\\n", "<br />")
  text = text.replace("[b]", "<b>")
  text = text.replace("[/b]", "</b>")
  text = text.replace("[i]", "<i>")
  text = text.replace("[/i]", "</i>")
  text = text.replace("[u]", "<u>")
  text = text.replace("[/u]", "</u>")
  text = text.replace("[h1]", "<h1>")
  text = text.replace("[/h1]", "</h1>")
  text = text.replace("[h2]", "<h2>")
  text = text.replace("[/h2]", "</h2>")
  text = text.replace("[h3]", "<h3>")
  text = text.replace("[/h3]", "</h3>")
  text = text.replace("[h4]", "<h4>")
  text = text.replace("[/h4]", "</h4>")
  text = text.replace("[h5]", "<h5>")
  text = text.replace("[/h5]", "</h5>")
  text = text.replace("[h6]", "<h6>")
  text = text.replace("[/h6]", "</h6>")
  text = text.replace("[p]", "<p>")
  text = text.replace("[/p]", "</p>")
  text = text.replace("[br]", "<br/>")
  text = text.replace("[img]", '<img width="200px" src="')
  text = text.replace("[/img]", '"></img>')
  text = text.replace("[yt]", '<iframe width="500" height="300" src="https://youtube.com/embed/')
  text = text.replace("[/yt]", '" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>')
  text = text.replace("[a]", '<a href="')
  text = text.replace("[/a]", '"></a>')
  text = text.replace("[blue]", "<font color='blue'>")
  text = text.replace("[/blue]", "</font>")
  text = text.replace("[red]", "<font color='red'>")
  text = text.replace("[/red]", "</font>")
  text = text.replace("[yellow]", "<font color='yellow'>")
  text = text.replace("[/yellow]", "</font>")
  text = text.replace("[lime]", "<font color='lime'>")
  text = text.replace("[/lime]", "</font>")
  text = text.replace("[green]", "<font color='green'>")
  text = text.replace("[/green]", "</font>") 
  return text

@app.route("/newpost/", methods=["POST"])
def add_post():
  canPost = False
  author = request.form["pseudo"]
  if author == "":
    author = "Anonymous"
  else:
    pass
  while True:
      id = random.randint(1,99999999)
      if len(str(id)) == 1:
                id = "0000000" + str(id)
      if len(str(id)) == 2:
                id = "000000" + str(id)
      if len(str(id)) == 3:
                id = "00000" + str(id)
      if len(str(id)) == 4:
                id = "0000" + str(id)
      if len(str(id)) == 5:
                id = "000" + str(id)
      if len(str(id)) == 6:
                id = "00" + str(id)
      if len(str(id)) == 7:
                id = "00" + str(id)
      else:
                id = id
                pass
      if str(id) in open("database.json").read():
          pass
      else:
          break
  #quoicoubeh
  print("test 1 passed")
  blacklist = open("blacklist.txt").read()
  blacklist = blacklist.splitlines()
  for word in blacklist:
      if word in request.form["content"].lower():
          canPost = False
          print("test 2.1 passed")
      else:
          pass
          print("test 2.2 passed")
          canPost = True
  if canPost:
    print("text 3 passed")
    db.insert({"pseudo": author, "content": stylize(request.form["content"]), "date": datetime.today().strftime('%Y/%m/%d %H:%M'), "likes": 0, "id":str(id)})
  else:
      pass
  return redirect()

@app.route("/post/<id>")
def post_detail(id):
    html_code = open("postdetail.html").read()
    Post = Query()
    result = db.search(Post.id == id)

    if result:
        pseudo = result[0]['pseudo']
        content = result[0]['content']
        print(f"Pseudo: {pseudo}\nContent: {content}")
    else:
        print("Aucun post avec cet ID n'a été trouvé.")
    
    html_code = html_code.replace("{postid}", id)
    html_code = html_code.replace("{author}", pseudo)
    html_code = html_code.replace("{content}", content)
    html_code = html_code.replace("{link}", id)
    html_code = html_code.replace("{likes}", str(result[0]['likes']))
    print(html_code)
    return html_code

@app.route('/like/<id>')
def like(id):
    Post = Query()
    result = db.search(Post.id == id)
    likes = result[0]["likes"]
    nouveau_nombre_likes = likes + 1
    db.update({'likes': nouveau_nombre_likes}, Post.id == id)
    html_code = post_detail(id)
    return html_code
    

if __name__ == '__main__':
  app.run(host='0.0.0.0')