### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

  - Syntax,
  - data types,
  - methods (python seems to have more built in methods for each datatypes),
  - comprehension
  - external libraries that make all kind of things.

- Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
  can try to get a missing key (like "c") _without_ your programming
  crashing.

  1. Pythonic way:

     ```python
     myDict = {"a": 1, "b": 2}
     if 'c' not in myDict:
       myDict['c'] = 3
     ```

  2. Javascript:

  ```javascript
  if (!Object.keys(myDict).includes('c')) {
    myDict['c'] = 3;
  }
  ```

- What is a unit test?
  It's a procedure to test the functionality of a particular view or function with an specific task, and check if it performs the task properly passing the results it should throw.

- What is an integration test?
  Ity's a procedure to test the interplay of different pieces of software, each one performing a particular task. The test checks if the parts interact properly, also passing a result that should be correct.

- What is the role of web application framework, like Flask?
  Providing an easy way to conduct the information flow through the different files and sections of functionality, from the backend calculations to the front end display of the information.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  - Sensitive data like passwords and private information: I'd use flask parameters.
  - Search terms, non sensitive data: I'd use URL query params.

- How do you collect data from a URL placeholder parameter using Flask?

  ```python
  data = request.form['data']
  ```

- How do you collect data from the query string using Flask?

  ```python
  data = request.args['data']
  ```

- How do you collect data from the body of the request using Flask?

  ```python
  data = request.args.get('data')
  ```

- What is a cookie and what kinds of things are they commonly used for?
  It's a piece of information stored in the browser, following server language codification and indications. That data is stored to save log ins, shopping carts, and other data to facilitate user's interaction with the app or site. Cookies also gather data about how the user interacts with the site.

- What is the session object in Flask?
  It's a way to store cookies with encryption, and it's syntax makes it very easy to create and modify this data.

- What does Flask's `jsonify()` do?
  It converts different data structures (lists, dictionaries, etc) in json format, to be used in requests and other tasks.
