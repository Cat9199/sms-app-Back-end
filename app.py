#===================modules===================
from flask import Flask ,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os

#==============configration==================
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config["UPLOAD_FOLDER"] = "static/postimg/"
app.config["UPLOAD_FOLDER_CSV"] = "static/CSV/"
#=================SQLschema===================

#------------------user--------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    phone_num = db.Column(db.Integer)
    password =  db.Column(db.String(80), nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    messages_Send = db.Column(db.Integer)
    Av_sms = db.Column(db.Integer)
    Av_whatsapp = db.Column(db.Integer)
    Av_email = db.Column(db.Integer)
    Last_login_time = db.Column(db.String(80), nullable=False)
    def __repr__(self):
        return f'<User {self.username}>'
#---------------------message--------------
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    User_add = db.Column(db.String(80), nullable=False)
    Message_title = db.Column(db.String(800), nullable=False)
    send_date = db.Column(db.DateTime(timezone=True),server_default=func.now())
    img = db.Column(db.LargeBinary)


    def __repr__(self):
        return f'<User {self.Message_title}>'

class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)

#===================APPfunction==================
@app.route("/")
def home():
    return render_template('index.html')
# @app.route("/upload")
# def func():
#     return render_template('other.html')
# @app.route('/upload', methods=['POST'])
# def upload():
    
#     pic = request.files['pic']
#     if not pic:
#         return 'No pic uploaded!', 400

#     # filename = pic.filename

#     # img = Img(img=pic.read(), name=filename)
#     # db.session.add(img)
#     # db.session.commit()
#     pic.save(app.config['UPLOAD_FOLDER'] + pic.filename)
#     return 'file uploaded successfully'


# @app.route('/csv', methods=['POST'])
# def csv():
    
#     pic = request.files['pic']
#     if not pic:
#         return 'No pic uploaded!', 400

#     # filename = pic.filename

#     # img = Img(img=pic.read(), name=filename)
#     # db.session.add(img)
#     # db.session.commit()
#     pic.save(app.config['UPLOAD_FOLDER_CSV'] + pic.filename)
#     return 'file uploaded successfully'

# # @app.route('/<int:id>')
# # def get_img(id):
# #     img = Img.query.filter_by(id=id).first()
# #     if not img:
# #         return 'Img Not Found!', 404

# #     return Response(img.img, mimetype=img.mimetype)


# @app.route('/image')
# def image():
#     images=Img.query.all() 
#     return render_template('image.html', images=images)






#=====================APProutes================
