from flask import Flask, render_template, send_from_directory, session, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(16)

#app.secret_key = print(os.urandom(16))

da_bros = [
     { "name": "Austin", "image": "austin.JPG", "bio": "Media mogul Austin Sabella CPA is the brains and the chin behind the bros. Born in 1993 in the slums of algonquin, austin discovered his love for wrestling playing tummy sticks with his cousin Corey. It quickly became apperent that he was a natural grapler, and Austin through the ranks of IL wresting until a self inflicted injury stopped his career short. Since then Austin has rebranded himself as a prestigous businessman becoming CFO of a media consultancy/Indian staffing firm." },
     { "name": "Ed", "image": "ed.jpeg", "bio": "Formerly the crown jewel of Cary, Illinois, Edward Wolfgang Cleven is a celebrated member of da bros. Once regarded as wildcard and quite the cocksmith, Ed rose through the ranks to be the first da bro in history to not only catch a golden snitch, but subsequently marry her. After trading in his longboard for love, Ed moved to Denver where he now breaks necks and cashes checks with his wife, Annie." },
     { "name": "George and Quinn", "image": "gq.JPG", "bio": "While George and Quinn may have two seperate bodies, they share one soul. It is disputed who is the leader of the dou, but most sources say they are driven by the desires of the un-intimidating Cricket. After a year sabitical from white pussy in 2018, Cricket has come back strong this year, finding himself fully engulfed in the mouth of who some may argue is the prettiest snitch." },
     { "name": "Kevin", "image": "kevin.JPG", "bio": "Kevin came up in the prestiguous suburb of Cary IL. A bit of a lamo, kevin has sworn off intoxicating substances in favor of feverously studying fantasy football. On the rare occasion he comes back to the homeland, you can be sure to find him at 'The Hat' with a hot dog in each hand. He has been quoted as saying 'I love the mouth feel of a fresh sweating Chicago dog'." },
     { "name": "Kyle", "image": "kyle.jpg", "bio": "Kyle, also know to some as the juggernaut, embodies the soul and the appetite of the bros. While his highschool sexual endevors often ended with a puky penis, Kyle has found great success in adulthood on the dating app 'tinder', with over 40 lays. If you ever have a chance to go out with the juggernaut, cherish the time, because he will almost certainly leave you without warning" },
     { "name": "Joey", "image": "joey.jpg", "bio": "The muscle of the group, Joey has a reputation for kicking ass and taking names. At a young age Joey crossed paths with the great and wonderful Tony Ramos, emboding him with the spirit of the warrior. He has since put that power to great use, being one of the most feared men in Carbonale after single handely splading an entire rival fraternaty. Joey has since calmed down, but legend has it every Eve's Eve he will glow with the power of Ramos" },
     { "name": "Rob", "image": "rob.jpeg", "bio": "Rob is a celebrated seaman, sexual maverick, alleged toilet clogger, and pathological liar. Rob had a brief stint at the highschool of Marian Central before leaving after discovering that many of the girls had taken a vow of chastity. He has since gained favor again with the bros, joing the group in 2018 after the group voted 4-3 to let him in. Rob is now a valued member of the group, always down to lend a hand, or tell you about his most recent lay." },
]          


#login 
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/')
def home():
    return render_template("main.html", da_bros=da_bros, title='Da Bros')

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images/Da-Bros", filename)




if __name__ == '__main__':
    app.run(debug=True)