from flask import Flask, render_template, request
from flask_mysqldb import MySQL #has to install the package: sudo pip install flask-mysqldb (https://askubuntu.com/questions/1159738/from-flask-mysqldb-import-mysql-gives-import-error-importerror-no-module-name)

app = Flask(__name__)



'''
@app.route('/<string:page_name>/',methods=['GET','POST']) #POST allow user inputs
def render_static(page_name):
    return render_template('%s.html' % page_name,result=result) #note: multiple variables like "result" can be passed
'''


#configure mysql
##ref: https://www.youtube.com/watch?v=6L3HNyXEais #use safe_load instead of load (https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation)


db=yaml.safe_load(open('db.yaml'))
##in the db.yaml file there has to be a space between the key and the text (otherwise it won't be parsed properly)

app.config['MYSQL_HOST']=db['mysql_host']
app.config['MYSQL_USER']=db['mysql_user']
app.config['MYSQL_PASSWORD']=db['mysql_password']
app.config['MYSQL_DB']=db['mysql_db']
mysql= MySQL(app)


@app.route('/',methods=['GET','POST']) #POST allow user inputs
def index():
    if request.method=='POST':
        #fetch the form data
        query=request.form
        name=userDetails['name']
        email=userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES(%s,%s) ",(name,email))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


if __name__ == "__main__":
    app.run()