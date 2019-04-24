The goal of this project was to create a travel app that combines some country information with visa information and UNESCO designated sites.

To make the project, I began by scraping four websites using BeautifulSoup and Selenium: The CIA World Factbook, the State Department's travel pages, UNESCO'S cultural heritage practices and UNESCO'S cultural heritage sites. All of these followed the same formula. I would first save all the URLS of individual countries or locations into a text file, then run a different program to loop over the URLS and get the information I wanted. At the end, I had four CSV files.

Once I had my CSVs, I used Microsoft Access to combine my travel (State Dept. info) file and my factbook (CIA) file, since both of those only had each country listed once. I then used a python file Professor McAdams wrote to turn those CSVs into a list of dictionaries, which I imported into a python file I was writing to run Flask on.

I created a form for my launch page that would let a user search and see if a country matches any of the countries in my master CSV, since there are only one of each. If there is a match, it reroutes to a detail page using the country's unique code.

On each detail page, I had the script search through my other two CSVs dictionaries, which included UNESCO information and multiple sites per country. If the name of the country page matched a name within the site location in either of the two dictionaries, it gathered that dictionary. This allowed me to include as many heritage locations as there may have been.

I created a detail page template and used variables to auto-feed the information in my CSV files. I then designed my own CSS file and used some basic JavaScript to make the page look nice. I used Bootstrap for my form on the launch page. 
