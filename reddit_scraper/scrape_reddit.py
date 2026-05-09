import requests
import json
import re
import time
import os
import random

# Configuration
TARGET_SUBS = [
        # Main Romanian football subreddit (Steaua, Rapid, Dinamo banter).             # Steaua Bucharest specific sub.
              # Dinamo specific sub.
    "RomaniaLibera",       # Less moderated Romanian sub, often has more extreme political views.
    "Balkans_irl",         # Balkan meme sub. Huge Romanian presence, massive amounts of nationalist banter and creative insults.
    "politic"              # General Romanian politics (smaller, but targeted).
]
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1"
]

def load_keywords():
    try:
        with open('regexes.json', 'r', encoding='utf-8') as f:
            lexicon = json.load(f)
        keywords = set()
        for key in lexicon:
            if isinstance(lexicon[key], list) and key != "placeholders":
                keywords.update([str(w).lower() for w in lexicon[key]])
        return keywords
    except Exception as e:
        print(f"Error loading keywords: {e}")
        return set()

def make_request(url, attempt=1):
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            wait_time = attempt * 15
            print(f"  Rate limited (429). Waiting {wait_time}s before retry {attempt}/3...")
            time.sleep(wait_time)
            if attempt < 3:
                return make_request(url, attempt + 1)
        else:
            print(f"  Failed request: {response.status_code}")
            return None
    except Exception as e:
        print(f"  Error: {e}")
        return None

def get_posts(subreddit, limit=50, sort="hot"):
    url = f"https://www.reddit.com/r/{subreddit}/{sort}.json?limit={limit}"
    data = make_request(url)
    return data['data']['children'] if data and 'data' in data else []

def get_comments(post_id, subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/comments/{post_id}.json"
    data = make_request(url)
    if data and isinstance(data, list) and len(data) > 1:
        comments_data = data[1]['data']['children']
        return extract_comment_bodies(comments_data)
    return []

def extract_comment_bodies(children):
    bodies = []
    for child in children:
        if child['kind'] == 't1':
            data = child['data']
            if 'body' in data and data['body'] not in ['[deleted]', '[removed]', None]:
                bodies.append(data['body'])
            if 'replies' in data and data['replies'] != "":
                bodies.extend(extract_comment_bodies(data['replies']['data']['children']))
    return bodies

def scrape():
    print("--- 🕵️ Multi-Subreddit Stealth Scraper ---")
    keywords = load_keywords()

    for sub in TARGET_SUBS:
        print(f"\nScanning r/{sub}...")
        all_scraped = []
        seen_bodies = set()
        output_file = f"reddit_scraper/scraped_{sub}_data.json"
        
        # Get multiple sorts
        posts = get_posts(sub, sort="hot")
        time.sleep(3)
        posts += get_posts(sub, sort="controversial")
        time.sleep(3)
        posts += get_posts(sub, sort="new")
        
        unique_posts = {p['data']['id']: p for p in posts}.values()
        
        for i, post in enumerate(unique_posts):
            post_data = post['data']
            post_id = post_data['id']
            print(f"  [{i+1}/{len(unique_posts)}] Scraping thread: {post_data['title'][:50]}...", end="\r")
            
            comments = get_comments(post_id, sub)
            toxic_count = 0
            
            for comment in comments:
                normalized = comment.lower()
                # Check for keywords or just take them all if the sub is specifically toxic?
                # For these subs, we might want to be more liberal, but let's stick to keywords for now.
                if any(kw in normalized for kw in keywords):
                    if normalized not in seen_bodies:
                        seen_bodies.add(normalized)
                        all_scraped.append({
                            "text": comment,
                            "source": f"reddit/r/{sub}",
                            "post_id": post_id
                        })
                        toxic_count += 1
            
            if toxic_count > 0:
                print(f"  [{i+1}/{len(unique_posts)}] Found {toxic_count} toxic comments.")
            
            time.sleep(random.uniform(3, 5))

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(all_scraped, f, ensure_ascii=False, indent=2)

        print(f"\n--- 🏁 Finished r/{sub} ---")
        print(f"Comments saved: {len(all_scraped)}")
        print(f"Data saved to: {output_file}")
        
        print("\nWaiting 30s before next subreddit to avoid IP ban...")
        time.sleep(30)

if __name__ == "__main__":
    scrape()
