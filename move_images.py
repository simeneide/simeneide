import os
import shutil

### RUNNING THROUGH ALL POSTS AND CHANGE IMAGE DIR TO /ASSETS FOR HUGO COMPATIBILITY

content_dir = "content/post/"
posts = [s for s in os.listdir(content_dir) if (".md" in s)& (s!="_index.md")]

for filename in posts:
    text = open(content_dir + filename).read()
    open(content_dir + filename, "w").write(text.replace('![](assets', '![](/assets'))
    

    
### MOVE ALL ASSETS TO /ASSETS
source = 'content/post/assets/'
dest1 = 'static/assets/'
files = os.listdir(source)

for f in files:
        shutil.move(source+f, dest1)