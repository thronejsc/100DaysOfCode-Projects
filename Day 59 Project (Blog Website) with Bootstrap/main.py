from flask import Flask, render_template, request
import requests
import smtplib

smtp_email = "tmacgravy21@gmail.com"
password = "aoff xhhf hbel hotm"

app = Flask(__name__)

url = "https://api.npoint.io/48ab47c49e2c5f566c59"
blogs = requests.get(url=url).json()


@app.route('/')
def home():
    return render_template('./index.html', blogs=blogs)


@app.route('/about')
def about():
    return render_template('./about.html')


@app.route('/sample')
def sample_post():
    return render_template('./post.html')


@app.route('/contact', methods=["GET", "POST"])
def contact():
    success_message = None
    if request.method == "POST":
        data = request.form
        send_email(data['name'], data['email'], data['phone'], data['message'])
        success_message = "Successfully sent your message"
    return render_template('./contact.html', message=success_message)


def send_email(name, email, phone, message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=smtp_email, password=password)
        connection.sendmail(from_addr=smtp_email, to_addrs=email, msg=f"Subject:Message from Blog Website\n\nName:{name}"
                                                                      f"\nEmail: {email}\nPhone Number: {phone}\n Message: {message}")


@app.route("/post-<int:num>")
def get_post(num):
    requested_post = None
    for blog in blogs:
        if blog['id'] == num:
            requested_post = blog
    return render_template('./post.html', blog=requested_post)


if __name__ == "__main__":
    app.run(debug=True)