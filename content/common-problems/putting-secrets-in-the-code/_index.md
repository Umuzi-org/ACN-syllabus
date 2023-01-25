---
title: Putting secrets in the code
---

Sometimes learners write stuff like this in the code:

```
API_KEY=jn124ikuhoqfdjakmsd02314
```

Or sometimes they add a secret token to their repo. Eg `token.json` or `client_key.json` or something like that.

As a general rule, if you are not comfortable with having a value spray-painted to the wall of a bathroom stall in black-hat hacker conference, then you shouldn't have it in your code. 

## How Git works

This is really important!! Let's say you add a secret to your code by mistake and you `git commit` it, then you realise your mistake, remove the secret, and add another commit. Are you safe?

No. Not if you pushed your commits.

The reason is: Git keeps track of every commit that there is. You can `checkout` any commit and look at the state of that commit.

Try this out:

```
git log
```

That will give you a log of all the commits. Each commit on your current branch will be listed like this:

```
commit cb8ceb545410c73cea2bf704eb2b75ae8a4586d2   # commit hash
Author: Someone's Name <example@email.com>
Date:   Fri Jan 20 12:45:15 2023 +0200

    the message

```

Once you know the hash of the commit you want to checkout you just do this:

```
git checkout cb8ceb545410c73cea2bf704eb2b75ae8a4586d2
```

So let's say you committed a secret:

```
commit f55b578ec8af1af923484f336e10927d461706bf   
Author: Noobie mc Noobface <example@email.com>
Date:   Fri Jan 20 12:45:15 2023 +0200

    Secrets removed. Now I feel safe and wholesome


commit cb8ceb545410c73cea2bf704eb2b75ae8a4586d2   
Author: Noobie mc Noobface <example@email.com>
Date:   Fri Jan 20 12:45:15 2023 +0200

    Secrets added

```

If anyone who has access to the repo wants access to the secret values they just `git checkout cb8ceb545410c73cea2bf704eb2b75ae8a4586d2`

## Procedure when secrets are added to repo

If you committed your secrets to your local branch and have not pushed yet, you need to revert your commits before pushing. 

If you have already pushed the secrets to Github then the general procedure for fixing the problem is:

1. invalidate the secrets immediately. If you revealed a password, go change the password. If you revealed an API key, go to the service provider and change the key. 
2. If other people were relying on the secret that you revealed (eg multiple people using the same client key) then go apologise and give them access to the new secrets in a secure way
3. change your name, sell all your stuff and move to a small anonymous island off the coast of Costa Rica. Not because you are unsafe, just because you are ashamed. 