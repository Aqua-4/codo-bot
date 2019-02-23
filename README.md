# codo-bot
Go ahead! win me the Codogram award ;)

## Steps:

* Start bot in the target folder
1. bot will clone the whole foder(../folder_name) and create copy named codo-temp
2. the copy contains all the git files, the bot uses this to leverage the ops
3. From the target-folder get list of all un-committed files
   * codo-temp
   1. git stash 
   2. get the first uncommited file  read it as text
   3. append 'x' characters to the other file
   4. git commit
   5. git push
   * Do-Recursive    
