# Git Timemachine - *the nostalgic git plugin*

---

git-timemachine is a portable python script that shows you a random commit from a given git repository - you can use it
to indulge in some nostalgia for code long gone, or perhaps get inspired by old ideas and methods since abondoned.
Currently it will not show you merge commits - chances are you see enough of those as it is.

It has no dependencies outside of python >= 2.4 and git, and it also works under python3.
You can either run it as a standalone script and pass the path to the git repo you'd like to time travel in,
or you can copy it to a location in your PATH as 'git-timemachine', make it executable, and then invoke `git-timemachine` from any git repo.

`--start` and `--end` flags can be used to limit the date range of the commits you will see.
