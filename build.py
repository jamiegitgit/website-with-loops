print("working on hw 3")

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
    print("maine xecuted")
    # Create base with header and footer
    base_template = open("templates/base.html").read()
    # Read in the header and footer
    header_footer = open("templates/headerfooter.html").read()
    # Use the string replace
    full_base = base_template.replace("{{content}}", header_footer)
    open("templates/fullbase.html", "w+").write(full_base)
    # adding header and footer to every page but index
    

    for page in pages:    
        if page["title"] == "index":
            base = open("templates/base.html").read()
            print("base is open")
        else:
            base = open("templates/fullbase.html").read()
            print("full base is open")
            title= page["title"]
            top_header = open ('templates/topheader.html').read()
            bottom_footer = open('templates/bottomfooter.html').read()
            content = open('content/'+ title + '.html').read()
            
            page_w_header_footer = top_header + content + bottom_footer
            open('content/incl_header_footer/' + title + '.html', 'w+').write(page_w_header_footer)
           
            

    #adding top and bottom to each page
    for page in pages:
        
        title= page["title"]
        top_template = open('templates/top.html').read()
        bottom_template = open('templates/bottom.html').read()
        content = open('content/incl_header_footer/'+ title + '.html').read()
        
        complete_page = top_template + content + bottom_template
        open('docs/' + title + '.html', 'w+').write(complete_page)

def old():
    
    # adding header and footer to every page but index
    for page in pages:
        
        if page["title"] != "index":
            title= page["title"]
            top_header = open ('templates/topheader.html').read()
            bottom_footer = open('templates/bottomfooter.html').read()
            content = open('content/'+ title + '.html').read()
            
            page_w_header_footer = top_header + content + bottom_footer
            open('content/incl_header_footer/' + title + '.html', 'w+').write(page_w_header_footer)
            

    #adding top and bottom to each page
    for page in pages:
        
        title= page["title"]
        top_template = open('templates/top.html').read()
        bottom_template = open('templates/bottom.html').read()
        content = open('content/incl_header_footer/'+ title + '.html').read()
        
        complete_page = top_template + content + bottom_template
        open('docs/' + title + '.html', 'w+').write(complete_page)
        
        


#run    
    
if __name__ == "__main__":
    main()
