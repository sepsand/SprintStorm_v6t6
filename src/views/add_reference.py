"""
Blueprint for handling the addition of new references.
"""

from flask import request, render_template, redirect
from src.app import app
from src.db import book, article

@app.route("/add_reference", methods=["GET", "POST"])
def add_reference():
    """
    Route for handling adding a new reference.
    """
    if request.method == "GET":
        return render_template("add_reference.html")

    if request.method == "POST":
        key = request.form['key']
        author = request.form['author']
        title = request.form['title']
        year = request.form['year']
        if request.form["reftype"] == "book":
            publisher = request.form['publisher']
            address = request.form['address']

            book.insert_one({
                "key": key,
                "author": author, 
                "title": title, 
                "year": year, 
                "publisher": publisher,
                "address": address
                })

        if request.form["reftype"] == "article":
            journal = request.form['journal']
            volume = request.form['volume']
            pages = request.form['pages']

            article.insert_one({
                "key": key,
                "author": author, 
                "title": title, 
                "year": year, 
                "journal": journal,
                "volume": volume,
                "pages": pages
                })

        return redirect("/view_reference")

    return None

@app.route("/choose_reference", methods=["GET"])
def choose_reference():
    """
    Route for choosing reference type.
    """
    choice = request.args.get('ref')

    return render_template("add_reference.html", choice=choice)
