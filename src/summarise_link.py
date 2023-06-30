


class WebPageSummariser():
    def __init__(self):
        page_content = None
        

    def load_and_summarise_page_content(self):

        # This will be the top function which calls other functions below
        # Ends by putting extracted info into self.page_content

        pass


    def extract_link(self):
        # This will extract the link from the message 
        pass


    def get_content_from_link(self):
        # This will use the request tool to fetch the content
        
        # NOTE: may need intermediate step to identify different *types* of link
        # e.g. article vs pubmed vs youtube vs arxiv, etc and decide appropriate
        # (or just use agent which can decide appropriately)

        pass

    def summarise_content(self):
        # This will summarise the content using an LLM

        # NOTE: may need intermediate step to remove the html tags
    

