
def test_scrape_iotd_gallery():
     	    """
     	    Scrape NASA Image of the Day Gallery
     	    """
     	    # Extra data massage for BeautifulSoup
     	    my_massage = get_massage()
     	
     	    # Open main gallery page
     	    client = WindmillTestClient(__name__)
    	    client.open(url='http://www.nasa.gov/multimedia/imagegallery/iotd.html')
    	
    	    # Page isn't completely loaded until image gallery data
    	    # has been updated by javascript code
    	    client.waits.forElement(xpath=u"//div[@id='gallery_image_area']/img",
    	                            timeout=30000)
    	
    	    # Scrape all images information
    	    images_info = {}
    	    while True:
    	        image_info = get_image_info(client, my_massage)
    	
    	        # Break if image has been already scrapped
    	        # (that means that all images have been parsed
    	        # since they are ordered in a circular ring)
    	        if image_info['link'] in images_info:
    	            break
    	
    	        images_info[image_info['link']] = image_info
    	
    	        # Click to get the information for the next image
    	        client.click(xpath=u"//div[@class='btn_image_next']")
    	
    	    # Print results to stdout ordered by image name
    	    for image_info in sorted(images_info.values(),
    	                             key=lambda image_info: image_info['name']):
    	        print ("Name: %(name)sn"
    	               "Link: %(link)sn" % image_info)