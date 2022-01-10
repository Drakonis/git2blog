# git2blog

git2blog takes a git repository's messages and converts it into a blog-like format

```
git2blog.py <target repository>
```

# Creating a blog
First initialize a git repository with
```
git init <repository name>
```
then write a commit with
```
git commit --allow-empty
```
then run
```
git2blog.py <repository name>
```

# Example blog
Clone the following repository and run the script to produce a example blog
```
https://github.com/Drakonis/git2blog-example
```

### Using guix

To enter a development environment run the following:

```
guix shell
```
