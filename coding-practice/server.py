from flask import Flask, render_template, session, request
import jinja2

MESSAGES = {
            "cheery": "Oh, happy day!",
            "honest": "Today is probably a mixed bag.",
            "dreary": "Oh, bother..."
}

app = Flask(__name__) # TODO: always need this for any flask stuff? 
app.secret_key = "blahhhhhhhh"
app.jinja_env.undefined = jinja2.StrictUndefined # for debugging purposes, 
                                # throw error if undefined variable in jinja

@app.route('/')
def show_homepage():
    return render_template('homepage.html')


@app.route('/form')
def show_form():
    """ Show form to user; send to next template to render. """

    # GET request for name attribute; store in session:
    session["name"] = request.args.get("name") # overwrites former name, if any

    return render_template('form.html', session=session)


@app.route('/results')
def show_results():
    """ Show results to user. """

    # cycle through checkbox args (DNE if unchecked); store in session:
    for arg in request.args:
        session["message_type"].append(arg)
        
    return render_template('results.html', session=session, messages=MESSAGES)



#-----------------------------------------------------------------------------#
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
