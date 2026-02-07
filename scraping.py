import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Browser configuration
options = uc.ChromeOptions()
# We use version_main=144 to match your current Chrome version
driver = uc.Chrome(options=options, version_main=144)

try:
    url = "https://pythonbooks.org/for-programming-beginners/"
    print(f"Opening {url}...")
    driver.get(url)
    
    # Wait for the page to load initial elements
    time.sleep(5)

    # Scroll down to ensure all books are rendered
    print("Scrolling to load all books...")
    driver.execute_script("window.scrollTo(0, 2000);")
    time.sleep(3)

    # Locating all book containers based on your HTML screenshot (div class="book-description")
    books = driver.find_elements(By.CLASS_NAME, "book-description")
    print(f"Found {len(books)} books.")

    book_list = []

    for book in books:
        try:
            # Extracting Title from <a class="title">
            title = book.find_element(By.CLASS_NAME, "title").text.strip()
            
            # Extracting Author from <h3 class="author"> and removing "by " prefix
            author_raw = book.find_element(By.CLASS_NAME, "author").text
            author = author_raw.replace("by ", "").strip()
            
            # Append to list with English headers
            book_list.append({
                'Book Title': title,
                'Author': author
            })
            print(f"Scraped: {title}")
        except Exception as e:
            # Skip if any specific book element is missing
            continue

    # Exporting data to Excel
    if book_list:
        df = pd.DataFrame(book_list)
        output_file = "Python_Books_Library.xlsx"
        df.to_excel(output_file, index=False)
        print(f"\nSuccess! Data saved to {output_file}")
    else:
        print("No data found.")

finally:
    print("Process finished.")
    input("Press Enter to close the browser...")
    driver.quit()