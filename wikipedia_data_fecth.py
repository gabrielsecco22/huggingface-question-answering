import json
import wikipediaapi

def collect_wiki_data(topics, save_to_file=True):
    # Initialize a Wikipedia session
    wiki_wiki = wikipediaapi.Wikipedia('en')
    # Collect information from Wikipedia
    data = []
    for topic in topics:
        page = wiki_wiki.page(topic)
        if page.exists():
            article_data = {
                'title': page.title,
                'summary': page.summary,
                'sections': []
            }
            for section in page.sections:
                article_data['sections'].append({
                    'title': section.title,
                    'content': section.text
                })
            data.append(article_data)

    if save_to_file:
        # Save the collected data to a file in data folder.
        for article in data:
            with open(f'data/{article["title"]}.txt', 'w') as f:
                print(f"Writing {article['title']} to file")
                f.write(f"Title: {article['title']}")
                f.write(f"Summary: {article['summary']}")
                f.write("Sections:")
                for section in article['sections']:
                    f.write(f"   - {section['title']}: {section['content']}")
                f.close()
    return data


def save_wiki_data(topics):
    data = collect_wiki_data(topics)
    # Save the collected data to a file in data folder.
    with open('data/_all_data.txt', 'w') as f:
        f.write(json.dumps(data))

def main():
    # Define a list of topics or search queries
    topics = ['Artificial intelligence', 'Machine learning', 'Data science', 'Neural networks', 'Deep learning', 'Natural language processing', 'Computer vision', 'Reinforcement learning', 'Supervised learning', 'Unsupervised learning', 'Semi-supervised learning', 'Recommender systems', 'Data mining', 'Big data', 'Data engineering', 'Data visualization', 'Data analysis', 'Data wrangling', 'Data modeling', 'Data munging', 'Data architecture', 'Data collection', 'Data governance', 'Data quality', 'Data security', 'Data integrity', 'Data enrichment', 'Data transformation', 'Data fusion', 'Data lake', 'Data warehouse', 'Data mart', 'Data silo', 'Data asset', 'Data asset framework', 'Data asset management', 'Data asset metadata', 'Data asset owner', 'Data asset quality']
    save_wiki_data(topics)


if __name__ == "__main__":
    main()