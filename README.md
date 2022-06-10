# zetsi

## **Rationale, if you will.**
This Git repository serves as a running record of my learning in computation. Hopefully, by the end of my formal bachelor's degree, I will have both the necessary knowledge to help me succeed, but also a way to share the knowledge I have.

---

## **General Layout Rules (GeLaR):**
*(not me trying to come up with a cool acronym)*

### **Markdown:**

Follow Markdown's [guide](https://www.markdownguide.org/) as found on their website. 

Or, use the [cheatsheet](https://www.markdownguide.org/cheat-sheet/) for a quick glance.

### **Branching:**
Each new day is a new branch, formatted in the same way: 

    mmmdd-yy

For example, February 2, 2022 would be: 

    feb02-22

After however much work is done, files are added, committed, and pushed to `main`.

**To check the current branch:** `git branch`

### **Pushing changes**

**The slow, multistep way:**

```
$ git checkout main
$ git pull
$ git merge feb02-22
$ git push origin main
```
- `git checkout main`: grab the remote repository, in this case, named `main`
- `git pull`: pull remote data from `main` onto local repository
- `git merge feb02-22`: upload local changes made in branch `feb02-22` onto `main`
- `git push origin main`: push changes from local repostory, `origin`, onto remote repository, `main`

**The faster, simpler way:**

    $ git push main origin:feb02-22

*tl;dr:* push changes from `origin` to remote branch `feb02-22` tracked from remote repository `main`.

### **Uploading a branch**

```
$ git push -u origin jun10-22
```
You know, the wiser way to do things where you don't wipe out all your 
previous work. Will save you a heart attack if you introduce a bug.