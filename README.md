# Gallery
#### By BensonGathu
## Description
A personal gallery application that you display your photos for others to see.
## User Story
* View different photos that interest me.
* Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
* Search for different categories of photos. (ie. Travel, Food)
* Copy a link to the photo to share with my friends.
* View photos based on the location they were taken.by joining a subscription.
## System Features
* Your Project must contain an Image model with the following properties:
1.Image
2.Image Name.
3.Image Description.
4.Image Location Foreign Key.
5.Image category Foreign Key.
* Your Project must contain location and category that link to the Image model. Remember to make migrations to your database when you change the properties of the model.
* You must implement the save, update and delete methods in both models and make sure you write tests for each method
* Your project must have a search form that when submitted calls a search function in the view function and redirects to a search results page.
* When a user clicks on an Image he/she should be redirected where a larger version of the image is displayed and should also see the details of the Image.
* A user should be able to click a button and have the link to the image copied to the machine’s clipboard. Make sure you write a test for this functionality.
* Your project should have a dashboard that you will use to post photos to the database and manage the photos.
* Your project should be deployed to Heroku when you have finished with the set features. You should provide the link to your project in the description part of your project repository.
## Technical Requirements
* Create a specs markdown file that lists down all the projects specifications.
* All your models should contain unit tests to test the different behaviours. All your test should pass.
* Your project should follow the proper folder structure.
* Your project should be deployed to Heroku.
* Your project should contain proper commit messages.
## Technologies Used
  * Python 3.6.9
  * HTML5, CSS and Bootstrap
  * Django Framework
  * Postgressql
  * Heroku

## Link to live site
[https://gallery96.herokuapp.com/](link)
## License
Copyright (c) [2021] [Benson Gathu]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.