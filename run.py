from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def template_test():
    return render_template('template.html', my_string="Wheeeee!", my_list=[0,1,2,1,6,7,8,3,4,5])


if __name__ == '__main__':
    app.run(debug=True)