from operator import index
from os import name
from flask import Flask, render_template
from  modules import convertTodict

userList = convertTodict("test1.csv")
#freshly converted from to a listed dictionary
#print(f'place of birth fot answer is : {userDict ['Name']}')
print(userList)


usersPairList = []
for p in userList:
    usersPairList.append( (p['Id'], p['Name']) )
#this pair is mainly useful for home/index page purposes

print(usersPairList)



app = Flask(__name__)



@app.route("/")
def index():
    '''background_color = "orange"
    greet = '<h1>Hello, Gators!</h1>'
    link = '<p><a href="user/test/Albert">Click me!</a></p>'
    #print(link.__doc__)'''
    
    return render_template("indexUser.html", pairs=usersPairList, the_title="Users Listing")
'''
@app.route("/user")
def user_root():
    text = '<p>Hello, you made a wrong api request! Click this : </p>'
    #link = '<p><a href="user/Albert">Click me!</a></p>'
    return text


@app.route("/")
def hello():
    #background_color = "blue"
    #greet = '<h1>Hello, Gators!</h1>'
    #link = '<p><a href="user/Albert">Click me!</a></p>'
    return render_template("index.html", pair=pairsList)


@app.route('/user/<name>')
def user(name):
    #background_color = "orange"
    return render_template('testUser.html', name=name, user=userDict, the_title=userDict['Name'])
'''
#@app.route('/users/<name>')
@app.route('/users/<name>.html')
def users(name):
    #background_color = "orange"
    try:
            userDict = userList[int(name ) - 1]
    except:
        return f"<h1>Invalid value for User: {name}</h1>"
        # a little bonus function, imported on line 2 above
    return render_template('testUser.html', name=name, user=userDict, the_title=userDict['Name'])

if __name__ == '__main__':
    #help(c.show)
    #print(names_dict)
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=4999, debug=True