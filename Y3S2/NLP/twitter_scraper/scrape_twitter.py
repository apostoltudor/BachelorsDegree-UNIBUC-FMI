import json
import time
import argparse
import os
from ntscraper import Nitter

def load_regexes(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error parsing {filepath}: {e}")
        print("Please ensure the JSON file is valid (no trailing commas, etc.).")
        exit(1)
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        exit(1)

def scrape_twitter(regexes_file, output_file, limit_per_term=20):
    regexes_data = load_regexes(regexes_file)
    scraper = Nitter(log_level=1, skip_instance_check=False)
    
    # We will pick terms from the regexes.json
    # It has lists of strings in different categories.
    
    search_terms = []
    for category, terms in regexes_data.items():
        if isinstance(terms, list) and category not in ['regex_patterns_comprehensive', 'placeholders']:
            search_terms.extend(terms)
            
    # Deduplicate terms
    search_terms = list(set(search_terms))
    print(f"Found {len(search_terms)} unique terms to search.")
    
    all_tweets = []
    
    for i, term in enumerate(search_terms):
        print(f"[{i+1}/{len(search_terms)}] Scraping for term: {term}")
        try:
            # ntscraper search
            tweets = scraper.get_tweets(term, mode='term', number=limit_per_term)
            if tweets and 'tweets' in tweets:
                for tweet in tweets['tweets']:
                    all_tweets.append({
                        "term": term,
                        "text": tweet.get('text', ''),
                        "user": tweet.get('user', {}).get('username', ''),
                        "date": tweet.get('date', ''),
                        "link": tweet.get('link', '')
                    })
        except Exception as e:
            print(f"Error scraping term {term}: {e}")
            
        # Polite delay to avoid rate limiting
        time.sleep(2)
        
    print(f"\nTotal tweets scraped: {len(all_tweets)}")
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(os.path.abspath(output_file)), exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_tweets, f, ensure_ascii=False, indent=2)
    print(f"Saved to {output_file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Scrape Twitter based on terms in regexes.json")
    parser.add_argument('--regexes', default='C:\\Users\\Cosmin\\Documents\\NLP\\regexes.json', help='Path to regexes.json (default: ../regexes.json)')
    parser.add_argument('--output', default='scraped_twitter_data.json', help='Output JSON file path (default: scraped_twitter_data.json)')
    parser.add_argument('--limit', type=int, default=20, help='Max tweets per term (default: 20)')
    args = parser.parse_args()
    
    scrape_twitter(args.regexes, args.output, args.limit)
