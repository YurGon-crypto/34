import requests
import json
from multiprocessing import Pool


def download_comments(subreddit):
    url = f"https://api.pushshift.io/reddit/comment/search/?subreddit={subreddit}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['data']
    else:
        print(f"Failed to download comments for subreddit {subreddit}. Status code: {response.status_code}")
        return None


def main():
    subreddit = "YOUR_SUBREDDIT_NAME"

    num_threads = 4


    with Pool(num_threads) as pool:
        results = pool.map(download_comments, [subreddit] * num_threads)


    all_comments = [comment for result in results if result for comment in result]


    all_comments.sort(key=lambda x: x['created_utc'])


    output_file = f"{subreddit}_comments.json"
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(all_comments, json_file, ensure_ascii=False, indent=2)

    print(f"Downloaded {len(all_comments)} comments. Stored in {output_file}")


if __name__ == "__main__":
    main()
