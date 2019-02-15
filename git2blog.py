import os,shutil,pygit2,time, sys
def buildblog():
    repo = pygit2.Repository(os.path.abspath(sys.argv[1])+'/.git')
    last = repo[repo.head.target]
    text=''
    fmodel = open('models/'+'blog'+'.html','r+')
    fmain = open('main.html','w+')
    if not os.path.exists('posts'):
        os.makedirs('posts')
    ftxt = fmodel.read()
    for commit in repo.walk(last.id, pygit2.GIT_SORT_TIME):
        id=str(commit.id)
        fpost = open('posts/'+id+'.html','w+')
        author=commit.author.name
        message=commit.message
        date=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(commit.commit_time))
        string='<h2>'+id+'</h2>\n<h5>'+date+'</h5>\n<p>'+message+'</p>'
        fpost.write(string)
        fpost.close()
        text=text+string+'\n'
    ftxt=ftxt.format(text=text)
    fmain.write(ftxt)
    fmain.close()
    fmodel.close()
def index():
    dirlist=os.listdir('posts')
    text=''
    fmodel = open('models/'+'index'+'.html','r+')
    fpost = open('index'+'.html','w+')
    ftxt = fmodel.read()
    for dirfile in dirlist:
        text=text+'<h1><a href="posts/'+dirfile+'">'+dirfile+'</a></h1>\n'
    ftxt=ftxt.format(text=text)
    fpost.write(ftxt)
    fpost.close()
    fmodel.close()
def main():
    buildblog()
    index()
if __name__ == "__main__":
    main()
