print("working on hw 3") ##

#lists
pages = [
    {
    "filename": "content/index.html",
    "output": "docs/index.html",
    "title": "index",
    },
    {
    "filename": "content/about.html",
    "output": "docs/about.html",
    "title": "about",
    },
    {
    "filename": "content/gallery.html",
    "output": "docs/gallery.html",
    "title": "gallery",
    },
    {
    "filename": "content/contribute.html",
    "output": "docs/contribute.html",
    "title": "contribute",
    },
]



#functions
def main():
    print("maine xecuted") ##
    
    # Create full base with header and footer 1
        #no return, no arguments
    #open basic base
    base_template = open("templates/base.html").read()
    # Read in the header and footer
    header_footer = open("templates/headerfooter.html").read()
    # Use the string replace
    full_base = base_template.replace("{{content}}", header_footer)
    open("templates/fullbase.html", "w+").write(full_base)
    
    
    #concatenate each page 
    
    for page in pages:
        title= page["title"]
        # assign base 2
            #argument is title, return base
        
        base = None
        #index gets basic base, others get full base    
        if title == "index":
            base = open("templates/base.html").read()
            print("base is open") ##
        else:
            base = open("templates/fullbase.html").read()
            print("full base is open") ##
            
            
        #replace placeholder in each page with content 3
            # argument is title, base. no return
        # Read in the content of each HTML page
        content = open("content/" + title + ".html").read()
        # Use the string replace
        finished_page = base.replace("{{content}}", content)
        open("docs/" +title+ ".html", "w+").write(finished_page)
        print("finished")##
        
       


#run    
    
if __name__ == "__main__":
    main()
