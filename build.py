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
    
    for page in pages:
        
        if page["title"] != "index":
            title= page["title"]
            top_header = open ('templates/topheader.html').read()
            bottom_footer = open('templates/bottomfooter.html').read()
            content = open('content/'+ title + '.html').read()
            
            page_w_header_footer = top_header + content + bottom_footer
            open('docs/' + title + '.html', 'w+').write(page_w_header_footer)
            print("success")
            #add header and footer
    for page in pages:
        print(page["title"])
        #add top and bottom
    
    # First, get the template files
    top_template = open('templates/top.html').read()
    top_header = open ('templates/topheader.html').read()
    bottom_template = open('templates/bottom.html').read()
    bottom_footer = open('templates/bottomfooter.html').read()

    # Read in index HTML code
    content = open('content/index.html').read()

    # Combine template HTML code with content HTML code
    index_html = top_template + content + bottom_template
    open('docs/index.html', 'w+').write(index_html)

    # Rinse and repeat, but with about me HTML code
    content = open('content/about.html').read()
    aboutme_html = top_template + top_header + content + bottom_footer + bottom_template
    open('docs/about.html', 'w+').write(aboutme_html)

    # And again, this time with gallery HTML code
    content = open('content/gallery.html').read()
    gallery_html = top_template + top_header + content + bottom_footer + bottom_template
    open('docs/gallery.html', 'w+').write(gallery_html)

    # And again, this time with contribute HTML code
    content = open('content/contribute.html').read()
    contribute_html = top_template + top_header + content + bottom_footer + bottom_template
    open('docs/contribute.html', 'w+').write(contribute_html)
    
#run    
    
if __name__ == "__main__":
    main()
