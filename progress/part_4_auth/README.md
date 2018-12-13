*Author: Nolan Cassidy
*Contact address: ncassidy@uoregon.edu
*Description:Functional continuation of project 4, 5 and 6 to include Authorization.


*PART1

*You can access the rest api on port 5001

*https://0.0.0.0:5001/api/register
*This link will allow you to sign up as a user

*https://0.0.0.0:5001/api/token
*This allows the user to sign in and get a makeToken

*You can now copy this token to access the api. For example:
*https://0.0.0.0:5001/listAll?token=YOURTOKENHERE

*PART2

*The original calc.html page now has added in user functionality.
* visit https://0.0.0.0:5002/ to find the brevet calculator
*Here you will find a logout and rememberme button
*if you log out it will take you to the log in screen again.
*the csrf protection was not able to get running
