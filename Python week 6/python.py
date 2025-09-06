#!/usr/bin/env python3
"""
Ubuntu Image Fetcher
"A person is a person through other persons." - Ubuntu philosophy

This program connects you to the work of others across the web,
embodying the Ubuntu principles of community and respect.
"""

import requests
import os
from urllib.parse import urlparse


def main():
    """
    Main function that orchestrates the Ubuntu image fetching process.
    Embodies Ubuntu principles of community connection and respect.
    """
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Get URL from user - connecting to the community
    url = input("Please enter the image URL: ")
    
    try:
        # Create directory if it doesn't exist - preparing space for shared resources
        os.makedirs("Fetched_Images", exist_ok=True)
        
        # Fetch the image - respectfully connecting to the web community
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Extract filename from URL or generate one - honoring the source
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        if not filename:
            filename = "downloaded_image.jpg"
            
        # Save the image - preserving the shared resource
        filepath = os.path.join("Fetched_Images", filename)
        
        with open(filepath, 'wb') as f:
            f.write(response.content)
            
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\nConnection strengthened. Community enriched.")
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
        print("Ubuntu teaches us that not all connections succeed, but we remain respectful.")
    except Exception as e:
        print(f"✗ An error occurred: {e}")
        print("In the spirit of Ubuntu, we handle challenges with grace.")


if __name__ == "__main__":
    main()


# Challenge Solutions (Bonus Implementation)
# =============================================

def fetch_multiple_images():
    """
    Challenge 1: Handle multiple URLs at once
    Demonstrates Ubuntu principle of community - serving many at once
    """
    print("Ubuntu Multi-Image Fetcher")
    print("Enter URLs separated by commas, or press Enter when done:\n")
    
    urls = []
    while True:
        url_input = input("Enter image URL (or press Enter to start downloading): ").strip()
        if not url_input:
            break
        urls.extend([url.strip() for url in url_input.split(',')])
    
    if not urls:
        print("No URLs provided. Ubuntu spirit encourages sharing!")
        return
    
    os.makedirs("Fetched_Images", exist_ok=True)
    successful = 0
    
    for i, url in enumerate(urls, 1):
        print(f"\n[{i}/{len(urls)}] Fetching: {url}")
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path) or f"image_{i}.jpg"
            filepath = os.path.join("Fetched_Images", filename)
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            print(f"✓ Successfully fetched: {filename}")
            successful += 1
            
        except Exception as e:
            print(f"✗ Failed to fetch: {e}")
    
    print(f"\n🌍 Ubuntu mission complete: {successful}/{len(urls)} images fetched")
    print("Community enriched through shared resources!")


def safe_download_with_checks():
    """
    Challenge 2: Implement safety precautions for unknown sources
    Embodies Ubuntu principle of wisdom and protection of community
    """
    print("Ubuntu Secure Image Fetcher")
    print("A tool that protects our community while staying connected\n")
    
    url = input("Please enter the image URL: ")
    
    try:
        os.makedirs("Fetched_Images", exist_ok=True)
        
        # Safety check 1: Validate URL format
        parsed_url = urlparse(url)
        if not parsed_url.scheme in ['http', 'https']:
            print("✗ Safety check failed: Only HTTP/HTTPS URLs are allowed")
            return
        
        # Safety check 2: Check headers first
        print("🔍 Performing Ubuntu safety checks...")
        response = requests.head(url, timeout=5)
        response.raise_for_status()
        
        # Safety check 3: Validate content type
        content_type = response.headers.get('content-type', '').lower()
        if not content_type.startswith('image/'):
            print(f"⚠️  Warning: Content type '{content_type}' may not be an image")
            proceed = input("Continue anyway? (Ubuntu teaches informed choices) [y/N]: ")
            if proceed.lower() != 'y':
                print("Ubuntu wisdom: Better safe than sorry!")
                return
        
        # Safety check 4: Check file size
        content_length = response.headers.get('content-length')
        if content_length:
            size_mb = int(content_length) / (1024 * 1024)
            if size_mb > 10:  # 10MB limit
                print(f"⚠️  Large file detected: {size_mb:.1f}MB")
                proceed = input("Download large file? (Ubuntu values mindful resource use) [y/N]: ")
                if proceed.lower() != 'y':
                    print("Ubuntu wisdom: Mindful consumption benefits all!")
                    return
        
        # If all checks pass, download the image
        print("✅ Safety checks passed - proceeding with Ubuntu confidence")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path) or "secure_download.jpg"
        filepath = os.path.join("Fetched_Images", filename)
        
        with open(filepath, 'wb') as f:
            f.write(response.content)
            
        print(f"✓ Securely fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\nUbuntu principle upheld: Connection with wisdom and respect.")
        
    except Exception as e:
        print(f"✗ Safety-conscious error handling: {e}")
        print("Ubuntu teaches us to fail gracefully and learn from challenges.")


def fetch_with_duplicate_prevention():
    """
    Challenge 3: Prevent downloading duplicate images
    Demonstrates Ubuntu value of resourcefulness and avoiding waste
    """
    import hashlib
    
    print("Ubuntu Smart Image Fetcher")
    print("Avoiding duplicates - Ubuntu principle of mindful resource use\n")
    
    url = input("Please enter the image URL: ")
    
    try:
        os.makedirs("Fetched_Images", exist_ok=True)
        
        # Download to check for duplicates
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Calculate hash of the content
        content_hash = hashlib.md5(response.content).hexdigest()
        
        # Check existing files for duplicates
        existing_files = []
        if os.path.exists("Fetched_Images"):
            for existing_file in os.listdir("Fetched_Images"):
                filepath = os.path.join("Fetched_Images", existing_file)
                if os.path.isfile(filepath):
                    with open(filepath, 'rb') as f:
                        existing_hash = hashlib.md5(f.read()).hexdigest()
                        if existing_hash == content_hash:
                            existing_files.append(existing_file)
        
        if existing_files:
            print(f"🔍 Ubuntu wisdom: This image already exists as {existing_files[0]}")
            print("Avoiding duplicate - Ubuntu values efficient resource use!")
            return
        
        # Save new unique image
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path) or f"unique_image_{content_hash[:8]}.jpg"
        filepath = os.path.join("Fetched_Images", filename)
        
        with open(filepath, 'wb') as f:
            f.write(response.content)
            
        print(f"✓ Successfully fetched new image: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\nUbuntu principle: Unique contributions enrich our community!")
        
    except Exception as e:
        print(f"✗ Error in Ubuntu duplicate prevention: {e}")


def advanced_header_checker():
    """
    Challenge 4: Check important HTTP headers before saving
    Demonstrates Ubuntu principle of informed decision-making
    """
    print("Ubuntu Header-Aware Image Fetcher")
    print("Making informed decisions - Ubuntu wisdom in action\n")
    
    url = input("Please enter the image URL: ")
    
    try:
        os.makedirs("Fetched_Images", exist_ok=True)
        
        print("🔍 Ubuntu analysis: Checking HTTP headers...")
        response = requests.head(url, timeout=5)
        response.raise_for_status()
        
        # Important headers to check
        headers_to_check = {
            'content-type': 'Content Type',
            'content-length': 'File Size',
            'last-modified': 'Last Modified',
            'server': 'Server Type',
            'cache-control': 'Cache Policy'
        }
        
        print("\n📋 Ubuntu Header Analysis:")
        print("-" * 40)
        
        for header, description in headers_to_check.items():
            value = response.headers.get(header, 'Not provided')
            print(f"{description}: {value}")
        
        # Validate important headers
        content_type = response.headers.get('content-type', '').lower()
        if not content_type.startswith('image/'):
            print(f"\n⚠️  Ubuntu caution: Content type '{content_type}' may not be an image")
        
        content_length = response.headers.get('content-length')
        if content_length:
            size_mb = int(content_length) / (1024 * 1024)
            print(f"📏 Ubuntu info: File size is {size_mb:.2f} MB")
        
        # Ask user to proceed based on header analysis
        print(f"\n🤔 Based on Ubuntu analysis, proceed with download?")
        proceed = input("Continue? [Y/n]: ")
        
        if proceed.lower() in ['n', 'no']:
            print("Ubuntu wisdom: Informed decisions protect our community!")
            return
        
        # Download the actual content
        print("\n⬇️  Proceeding with Ubuntu-informed download...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path) or "header_checked_image.jpg"
        filepath = os.path.join("Fetched_Images", filename)
        
        with open(filepath, 'wb') as f:
            f.write(response.content)
            
        print(f"✓ Header-validated fetch complete: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\nUbuntu principle: Knowledge empowers wise community action!")
        
    except Exception as e:
        print(f"✗ Error in Ubuntu header analysis: {e}")


# Uncomment below to test challenge solutions:
# fetch_multiple_images()
# safe_download_with_checks()
# fetch_with_duplicate_prevention()
# advanced_header_checker()