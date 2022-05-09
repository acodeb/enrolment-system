# Class enrolment system

## Problem

- Use python to develop a class enrolment system for students for a university in New York USA
- You may use frameworks
- You may persist data to a database like PostgreSQL on a docker container or in a data structure
- The users of the system will consist of both school administrators and students
- School administrators will create student identities
- Students will be able to enroll themselves into classes

## Restraints:

- School administrators can create and modify student records but never delete them
- Each class has a fixed number of credits
- Some harder classes might be 4 credits while easier ones could be 2 or 3 credits
- Each student is only allowed to be enrolled in a maximum of 20 credits for each semester
- A class takes place every year in a single semester
- There is a minimum of 10 credits to be considered full time; anything less is part time
- There are two semesters per academic year:
  - Fall - August to January
  - Spring - February to July

## Requirements:

Create a good set of REST APIs that can fulfill the following requirements:

[X] Add a new student
  - Store only the following information about a student
    - Phone Number
    - First Name
    - Last Name
    - Nationality
    - Gender
[X] Modify a student
- Create a new semester
- Enroll a student into a class for a particular semester
- Get the list of classes for a particular student for a semester
- Get the full history of classes enrolled
- Get the list of students enrolled in a class for a particular semester
- Remove a student from a class
- Get a list of classes and the details of part time students enrolled for a specified semester and year
  - Add the ability to filter by first or last name beginning with a specified character
  - Add the ability to filter by international students
  - Add the ability to filter by gender

## Non Functional Considerations

- Performance and scalability considerations of your code will be evaluated.
  - Make sure the data structures that you use are chosen for scale and efficiency. For example, think about which APIs might be called more often than others with what parameters, and make sure those can handle the load efficiently.
- Use a suitable authentication method for API access e.g. JWT
- Don't overthink the non functional considerations.
- You can make assumptions.

## You will be evaluated on:

- Production readiness of the application
- Code quality
- Testing
- A README containing information on how to build, run and test the code

## Hints:

- Don't overthink the problem
- Don’t spend too long on the problem
  - We understand you are busy with your day to day life, therefore we recommend spending around 3 hours
- Don’t overlook testing
- You can make assumptions
  - Document them in your README
