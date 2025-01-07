from Bio import Entrez
from time import sleep

# fetch papers from pubmed database
def fetch_papers(query: str, max_results: int = 10) -> list:
    Entrez.email='zanwarpratham@gmail.com'
    try:
        # search pubmed
        handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
        search_results = Entrez.read(handle)
        handle.close()

        # fetch details for each article
        id_list = search_results["IdList"]
        handle = Entrez.efetch(db="pubmed", id=",".join(id_list), retmode="xml")
        sleep(1)
        papers = Entrez.read(handle)
        handle.close()

        return papers["PubmedArticle"]
    except Exception as e:
        print(f"Error fetching papers: {e}")
        return []
