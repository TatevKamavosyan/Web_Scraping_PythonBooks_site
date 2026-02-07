import subprocess

def run_pipeline():
    print("🚀 Step 1: Starting Web Scraping...")
    # Աշխատեցնում է քո առաջին ֆայլը
    subprocess.run(["python", "scraping.py"])
    print("✅ Scraping finished. 'Python_Books_Library.xlsx' created.")

    print("\n🧹 Step 2: Starting Data Cleaning...")
    # Աշխատեցնում է քո երկրորդ ֆայլը
    subprocess.run(["python", "scraping_clean.py"])
    print("✅ Cleaning finished. 'Final_Python_Books_Library.xlsx' is ready!")

if __name__ == "__main__":
    run_pipeline()