from src.summarise_link import WebPageSummariser
from src.combine_content import ContentCombiner


messages = [
    # Put messages which contain links to summarise
]


if __name__ == "__main__":
    
    link_contents = []

    for message in messages:

        summariser = WebPageSummariser()
        summariser.load_and_summarise_page_content()

        link_contents.append(summariser.page_content)

    combiner = ContentCombiner(link_contents)
    combiner.combine_content()

    print(combiner.overall_summary)

