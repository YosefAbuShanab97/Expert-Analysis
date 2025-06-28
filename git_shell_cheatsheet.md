# Generate SSK key for Authentification

### For Unix-based systems in Shell or Terminal
#### Type the following to create new key for Git

`ssh-keygen`

then follow the instructions

### Get the public key to store it in GitHub in Unix-based Systems

`cat .ssh/id_rsa.pub`

### Creating and Using SSH-Keys on Windows 
follow https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/GitHub-SSH-Windows-Example



# Working with local repository in shell (or powershell)

## Clone repository from Github
Navigate in Shell to the folder that should store your git repo. Then type
`git clone <ssh-address-of-github-repository>`
	
## Pull newest version from Github
Navigate in Shell to the folder that stores your git repo. Then type
`git pull`

## Get the status of your local repository
Navigate in Shell to the folder that stores your git repo. Then type
`git status`

- The red files are the ones you changed, but did not mark for committing yet
- The green files are the ones you changes and already marked for committing

## Mark for committing Files 
Navigate in Shell to the folder that stores your git repo. Then type
`git add <Filename>` for one file
`git add .` for all files in the current folder 

## Commit to git 
Navigate in Shell to the folder that stores your git repo. Then type
`git commit -m "<message>"`

- only files that are previously marked for committing are commited
- specify a specific commit message, e.g., "changed function getData()"
	
## Push to server
Navigate in Shell to the folder that stores your git repo. Then type
`git push`

- Only comitted files are pushed on the server
- Sometimes you need to pull first, as someone else pushed their code to the server

