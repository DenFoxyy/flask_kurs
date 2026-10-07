from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # return render_template(
    #     "index.html",
    #     # navn="Denys",
    #     # klasse="VG2",
    #     # fag="Informasjonsteknologi"
    # )
    alder = 17
    return render_template("index.html", alder=alder)

@app.route('/om')
def om():
    return render_template("om.html")


@app.route("/fag")
def fag():
    fagliste = ["Python", "Flask", "HTML", "CSS"]
    return render_template("fag.html", fag=fagliste)

@app.route("/spill")
def spill():
    spillliste = ["Roblox", "Minecraft", "GTA5", "Apex Legends"]
    return render_template("spill.html", spill=spillliste)

@app.route('/post')
def post():
    return render_template("post.html")

@app.route('/registrering', methods=['GET', 'POST'])
def registrering():
    if request.method == "POST":
        navn = request.form["navn"]
        fag = request.form["fag"]
        epost = request.form["epost"]
        alder = request.form["alder"]
        kommentar = request.form["kommentar"]
        return render_template(
            "resultat.html",
            navn=navn,
            fag=fag,
            epost=epost,
            alder=alder,
            kommentar=kommentar
        )
    return render_template("registrering.html")
  # return f"Hei, {navn}"
    # return render_template("registrering.html")


@app.route("/kurs", methods=["GET", "POST"])
def kurs():
    kursliste = ["Python", "Flask", "JavaScript", "Linux"]
    if request.method == "POST":
        kurs = request.form.get("kurs")
        nivaa = request.form.get("nivaa")
        godtar = request.form.get("godtar")
        interesser = request.form.getlist("interesser")
        return render_template(
            "kursresultat.html",
            kursliste=kursliste,
            kurs=kurs,
            nivaa=nivaa,
            godtar=godtar,
            interesser=interesser,
        )
    return render_template("kurs.html", kursliste=kursliste)
if __name__ == '__main__':
    app.run(debug=True)
