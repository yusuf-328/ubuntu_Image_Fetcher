import requests
import os
from urllib.parse import urlparse
import hashlib

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Accept multiple URLs
    urls = input("Please enter image URL(s) (separate multiple with commas): ").split(",")

    # Create directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)

    for url in [u.strip() for u in urls if u.strip()]:
        try:
            # Fetch the image
            response = requests.get(url, timeout=10, headers={"User-Agent": "UbuntuFetcher/1.0"})
            response.raise_for_status()

            # Extract filename from URL
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)

            if not filename or "." not in filename:
                # Generate unique filename using hash if not provided
                filename = f"image_{hashlib.md5(url.encode()).hexdigest()[:8]}.jpg"

            filepath = os.path.join("Fetched_Images", filename)

            # Prevent duplicates
            if os.path.exists(filepath):
                print(f"⚠ Skipped (duplicate): {filename}")
                continue

            # Check important headers
            content_type = response.headers.get("Content-Type", "")
            if not content_type.startswith("image/"):
                print(f"✗ Not an image: {url}")
                continue

            # Save the image
            with open(filepath, "wb") as f:
                f.write(response.content)

            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")

        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error for {url}: {e}")
        except Exception as e:
            print(f"✗ Unexpected error for {url}: {e}")

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()