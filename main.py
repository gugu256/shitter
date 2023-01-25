from flask import Flask, request
import random
from datetime import datetime
from tinydb import TinyDB, Query
from replit import db as debe # MEC ELLE MARCHE PAS CETTE DB
# att je teste un keutru


db = TinyDB('db.json')
 
app = Flask("Shitter")


@app.route('/', methods=["GET"])
def home():
  if request.remote_addr in open("ipdb").read():
    pass
  else:
    open("ipdb", "a").write(str(request.remote_addr) + "\n")
  return return_website()

def return_website():
  posts = list(reversed(db.all()))
  htmlcode = open("index.html").read()
  for post in range(0, len(posts)):
    try:
      htmlcode += "<li><u>" + posts[post]["pseudo"] + "</u> : " + posts[post]["content"] + " ("+ posts[post]["date"] +")" + "</li>" 
    except KeyError:
      htmlcode += "<li>" + posts[post]["content"] + "</li>" 
  htmlcode += "</body></html>"
  return htmlcode

def redirect():
  return '<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0; url=\'https://shitter-uh-yeah-skrrtatata.pancakedev.repl.co/\'" /></head><body></body></html>'

"""@app.route("/newhashtag")
def newhashtag(hashtag):
    """
@app.route("/leaderboard")
def leaderboard():
  htmlcode = open("posts.html").read()
  users = debe.keys()
  leaderboarddb = {}
  for user in users:
    leaderboarddb[user] = debe[user]
  sorted_keys = sorted(leaderboarddb.keys(), key=lambda x: leaderboarddb[x], reverse=True)
  for usr in range(0, len(sorted_keys)):
    htmlcode += "<li><u>" + sorted_keys[usr] + "</u> : " + str(leaderboarddb[sorted_keys[usr]]) + " posts </i>"
  htmlcode += "</body></html>"
  return htmlcode

@app.route("/ips")
def ips():
  return open("ipdb").read()

@app.route("/newpost", methods=["POST"])
def add_post():
  blacklist = open("blacklist.txt").read().splitlines()
  if request.form["pseudo"] in debe.keys():
      debe[request.form["pseudo"]] += 1
  else:
      debe[request.form["pseudo"]] = 1 
  if request.form["content"] == "$patchouli_on_the_qtoub":
    open("db.json", "w+").write('{"_default": {"1": {"pseudo": "Admin", "content": "THE DB WAS PURGED", "date":"'+ datetime.today().strftime('%Y-%m-%d %H:%M') +'"}}}')
    users = debe.keys()
    for user in users:
      del debe[user]
    return redirect()
  else:
    pseudo = request.form["pseudo"]
    content = request.form["content"]
    for forbidden_word in range(0, len(blacklist)):
      content.replace(blacklist[forbidden_word], "*"*len(blacklist[forbidden_word]))
      pseudo.replace(blacklist[forbidden_word], "*"*len(blacklist[forbidden_word]))
    db.insert({"pseudo": pseudo, "content": content, "date": datetime.today().strftime('%Y/%m/%d %H:%M')})
    return redirect()

if __name__ == '__main__':
  app.run(host='0.0.0.0')