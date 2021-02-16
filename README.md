# Documentation

This documentation refers to the coding assignment provided by Logic.


## How to run the application.
To begin with, the Front-End part of the application is written in HTML and CSS using Javascript JQuery to communicate with the Back-End point. 
The Back-End point is written in Python Flask, so in order to run the code, one has to install both Python and Flask. In order to do so, please follow the instructions below:
* Download the latest version of Python from [here](https://www.python.org/downloads/) based on your OS. Follow the instructions for a successful installation from [here](https://realpython.com/installing-python/).
* Install Flask. You can follow the instructions from [here](https://flask.palletsprojects.com/en/1.1.x/installation/).
* Cd the appropriate path in the Terminal and execute app.py by writing python3 app.py in your Terminal or in the IDE you prefer. 
* Follow the [path](http://127.0.0.1:5000/) to see the webpage and test it in your browser.


## The application and the functions.
There are 3 python files in the application. The first one is *__init__.py*, which is needed to clarify that this is a package and so we can import inside *app.py* the other python file, which is *quicksort.py*. 


* Quicksort.py : This python file includes the code for the Quicksort. Quicksort is a divide-and-conquer algorithm, breaking the problem into smaller sum-problems. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively. 
Quicksort is a comparison sort, meaning that it can sort items of any type for which a "less-than" relation is defined.

How it works: 
Set the base case.
	if start >= end:
		return list

Randomly randomly select an element as the pivot.
(pivot_idx = randrange(start, end + 1)) 
(pivot_element = list[pivot_idx])

Swap it to the end of the list.
(list[end], list[pivot_idx] = list[pivot_idx], list[end]).

Iterate through the list and track all the “lesser than” elements by swapping them with the iteration index and incrementing a lesser_than_pointer.
	less_than_pointer = start
for i in range(start, end):
       		if list[i] < pivot_element:
           	print("Swapping {0} with {1}".format(list[i], pivot_element))
           	list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
           	less_than_pointer += 1

Swap the pivot element with the element located at lesser_than_pointer.
	list[end], list[less_than_pointer] = list[less_than_pointer], list[end]

With the list partitioned into two sub-lists, repeat the process on both halves until base cases are met.
quicksort(list, start, less_than_pointer - 1)
quicksort(list, less_than_pointer + 1, end)


* App.py : This python file includes the code for the application to run. This is a Flask application that has 2 routes (@app.route). 
The first one is the Homepage (@app.route("/", ) that includes a basic function and renders to the HomePage which includes the form (index.html).

The second one is (@app.route("/api/sort", methods=[“POST”]. This includes the main function used to sort the user’s input and returns a JSON file with the user’s input sorted.
The function def sort_the_words() receives a JSON request, which includes a JSON list. 
Then it capitalizes every word in the JSON list and appends it to a new list called final_list. This is happening because the sorting algorithm treats uppercase and lowercase letters differently, displaying first the uppercased ones.
Continuing the function checks if the user provided an array of strings by checking the length of the array. 
If the length is less than 2, that means that the user wrote 1 or 0 words, so the quicksort cannot be performed. In this case (else:) the function returns a 400 error and displays a relevant message to the website.
If the user’s input is valid (len(final_list) >= 2) then quicksort algorithm is performed on the list. 
Finally a JSON response is created (json_list) and returned to the website.


Inside the templates folder, there is the index.html file.
* Index.html : This is the file that includes the HTML code for the website. It has a form with a textarea where the user can provide the words that need sorting and a button to submit the form. It also includes a div element that is hidden and shows only when the sorted list returns as a JSON list and displays the sorted list and a paragraph that displays the error message in case an error occurs.

* script : The JQuery code that sends and receives the JSON request/response to/from the api/sort Endpoint. 
Upon clicking the SubmitButton the function retrieves the input from the textarea. The words are trimmed so that unnecessary spaces are removed and then are appended to the list_of_words. The SubmitButton is disabled and its text is changed to “Waiting for Results”.
Then the list_of_words is converted to a JSON list (json_list) and through AJAX it’s sent to the api/sort Endpoint with ‘POST’ method.
In case of a successful retrieval (success) of the sorted JSON list, the function shows the hidden div element and displays inside it the words of the sorted list (json_list) one by one.
In case of a failed retrieval (error) it displays in the paragraph (<p>)  with id = “message” the message of the error that occurred (error.responseText).
Either way, the complete part, will re-enable the button and change the text of the button back to “Submit your List”

* Inside the static/css folder there is a style.css file that includes some of the CSS of the webpage. Some CSS is also included inside index.html.