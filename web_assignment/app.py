from flask import Flask, render_template, request, flash, url_for, jsonify
from quicksort import quicksort
import json

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route("/", )
def home():
    return render_template("index.html")


@app.route("/api/sort", methods=["POST"])
def sort_the_words():

    #Retrieve the JSON request.
    response = request.get_json()

    #Create a new list to put each word uppercased inside. If there are words with capitalized letters, the sorting doesn't work efficiently.
    final_lst = []

    #Putting the words uppercased inside the final_lst.
    for word in response:
        final_lst.append(word.upper())

    #Check if the user has provided words and the number of the words the user provided.
    #If the number is less than 2, show a message that they need to provide at least 2 words.
    if len(final_lst) >= 2:

        #Call the quicksort method on the final_lst in order to sort it.
        quicksort(final_lst, 0, len(final_lst) - 1)

        #Check that the list is indeed correctly sorted by printing it in the terminal.
        print(final_lst)
        print("Your list is : ")
        for l in final_lst:
            print(l)
        
        #Turn the sorted list in a JSON list and return it. 
        json_list = json.dumps(final_lst)

        return json_list

    else:
        #Show the Error Message and return again to the webpage.
        return("Error: I'm sorry! You need to submit at least 2 words!\n Tip: Remember to leave space between your words!", 400)

if __name__ == "__main__":
    app.run(debug=True)

