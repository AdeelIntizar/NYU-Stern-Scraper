# **NYU-Stern-Scraper**  
A scraper built using **Selenium** and **Chromedriver** to extract data from the NYU Stern platform.  

**Scraping is very important for data extraction, as it helps in collecting useful information from websites automatically. Instead of copying data manually, a scraper can do the job faster and more efficiently.**  

## **NYU Stern**  
The **Leonard N. Stern School of Business (NYU Stern)** is the business school of **New York University (NYU)**, a prestigious private research university in **New York City**. It was founded in **1900** as the **School of Commerce, Accounts and Finance**.  

## **NYU Stern Scraper**  
This scraper extracts crucial information about faculty members and all associated members of **NYU Stern**.  

### **Associated Members URL**  
[NYU Stern Faculty Members](https://www.stern.nyu.edu/experience-stern/about/departments-centers-initiatives/academic-departments/economics/people/)  

### **Scraping Content:**  
- Name  
- Description  
- Email  
- Personal Website Link  
- Image URL  

### **Program Functionality:**  
The scraper parses the website and extracts information for:  
- **Full-Time Faculty Members**  
- **Affiliated Faculty Members**  
- **Emeriti Faculty**  
- **Adjunct Faculty**  
- **Visiting Scholars**  
- **In Memoriam**  

It gathers valuable information about these people and stores it in a **CSV file**.  

## **How to Run the Program**  
1. Clone the repository:  
   ```sh
   git clone https://github.com/AdeelIntizar/NYU-Stern-Scraper.git
2. Install Google Chromedriver:
   ```sh
   https://developer.chrome.com/docs/chromedriver/downloads
Make sure to install the compatible version for your Chrome browser. 
   
3. Install required Python libraries:  
   ```sh
   pip install -r requirements.txt
4. Adjust the Chromedriver path in the script if necessary.  
5. Run the scraper:  
   ```sh
   python scraper.py  
#Now you are good to go!   

