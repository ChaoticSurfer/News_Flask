from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from admin import admin
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(admin, url_prefix='/admin')


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news_db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

db = SQLAlchemy(app)

'''არსებობს პრობლემა სხვისი სერვერიდან ანუ უცხო სერვერის ლინკიდან(src) სურათის
 ჩატვირთვაზე მომავალში გამოვასწორებ ან მომიწევს ფოტოების ჩამოწერა, თუმცა არ მინდოდა
  ჩემი კომპის დატვირთვა არანაირად და მინიმალისტურად ვგეგმავ გამოსვლას'''


class news_piece(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.Text)
    date_time = db.Column(db.DateTime)
    photo_url_main = db.Column(db.String(400))

    def __init__(self, id, title, content, date_time, photo_url_main):
        self.id = id
        self.title = title
        self.content = content
        self.date_time = date_time
        self.photo = photo_url_main


@app.route('/about-me')
def about_me():
    return render_template('about-me.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        seearch_words = request.form.get('search')
        if seearch_words:
            passed = news_piece.query.filter(news_piece.content.contains(seearch_words)).order_by(
                news_piece.date_time).all()
            return render_template('index.html', news=passed)
        else:
            all_pieces = news_piece.query.order_by(news_piece.date_time).all()
            return render_template('index.html', news=all_pieces)
    else:
        all_pieces = news_piece.query.order_by(news_piece.date_time).all()
        return render_template('index.html', news=all_pieces)

      
#   needs flask-cors  ...response....headers.add("Access-Control-Allow-Origin", "*") or upp^



# Error Handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', e=e)


app.register_error_handler(404, page_not_found)

if __name__ == '__main__':
    app.run(debug=True)
