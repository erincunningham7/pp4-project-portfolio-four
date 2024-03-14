# Adopt Me

Adopt Me is a fictional advertisement website for dog adoption purposes. The app is designed to allow registered to easily make advertisements and manage them.
The live link can be found here: [Live Site - Adopt Me](https://pp4-adopt-me-7acd5b9ef50f.herokuapp.com/)

## Deployment

### Version Control

The Adopt Me website was created using Gitpod and pushed to github to the remote repository ‘pp4-project-portfolio-four’.

The following git commands were used religiously throughout the website's development to push code to the remote repo:

```git add .``` - This command was used to add the changed file(s) to the staging area before they were committed to the local repository.

```git commit -m “commit message”``` - This command was used to commit the changes to the remote repo queue ready for the last step in the process.

```git push``` - This command was used to push all of the committed code to the repository on github.

### Heroku Deployment

The site was deployed to Heroku. The steps for deployment are as followed:

- Go to Heroku website and create a registered account
- Click the 'new' button in the top right corner
- Select 'create new app'
- Enter the application name
- Select region and click the create app button
- Navigate to the settings tab and click on 'reveal config vars'
- Add the following config vars:
  - SECRET_KEY: (Your secret key)
  - DATABASE_URL: (This should already exist with add on of postgres)
  - CLOUNDINARY_URL: (cloudinary api url)
- Navigate to the deploy tab
- Click the deploy tab
- Scroll down to 'connect to GitHub' and sign in to your Github account
- Using the search box, find the Github repository you want to deploy and click the 'connect' button
- Scroll down to the manual deploy section and choose the main branch
- Click deploy

The app should now be deployed.

The live link can be found here: [Live Site](https://pp4-adopt-me-7acd5b9ef50f.herokuapp.com/)

### Run Locally

Open Github and go to the GitHub repository you would like to clone to use locally:

- Click on the 'code' button
- Click on HTTPS
- Copy the repository link
- Open your IDE (git must be installed for the following steps)
- Type git clone copied-git-url into the IDE terminal

The project will now have been cloned on your local machine for use.

### Fork Project

Forks are usually used to either propose changes to someone else's project or to use someone else's project as a base for your own website idea.

- Open Github

- Go to the GitHub Repository you want to fork

- On the top right corner of the page underneath the header, click the 'fork' button

- This will create a copy of the project in your GitHub repository
