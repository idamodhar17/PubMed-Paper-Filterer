import pandas as pd

# format paper in required way 
def format_papers(papers):
    articles = []
    for paper in papers:
        try:
            # extract pubmed id
            pubmed_id = paper["MedlineCitation"]["PMID"]
            
            # extract title
            title = paper["MedlineCitation"]["Article"]["ArticleTitle"]
            
            # extract publication date
            pub_date = paper["MedlineCitation"]["Article"]["Journal"]["JournalIssue"]["PubDate"]
            pub_date_str = " ".join([str(pub_date.get(key, "")) for key in ["Year", "Month", "Day"]]).strip()
            
            # extract authors
            authors = paper["MedlineCitation"]["Article"].get("AuthorList", [])
            non_academic_authors = []
            company_affiliations = []
            corresponding_author_email = None
            
            for author in authors:
                affiliation_info = author.get("AffiliationInfo", [])
                if affiliation_info:
                    # check for affiliations and classify
                    for aff in affiliation_info:
                        affiliation = aff.get("Affiliation", "").lower()
                        if any(kw in affiliation for kw in ["university", "institute", "college", "school", "lab"]):
                            continue
                        else:
                            non_academic_authors.append(f"{author.get('ForeName', '')} {author.get('LastName', '')}")
                        if any(kw in affiliation for kw in ["pharmaceutical", "biotech", "corp", "company"]):
                            company_affiliations.append(affiliation)

                # extract corresponding emails
                if corresponding_author_email is None and affiliation_info:
                    email = next(
                        (word for word in aff.get("Affiliation", "").split() if "@" in word), None
                    )
                    if email:
                        corresponding_author_email = email

            articles.append({
                "PubmedID": pubmed_id,
                "Title": title,
                "Publication Date": pub_date_str,
                "Non-academic Author(s)": ", ".join(non_academic_authors),
                "Company Affiliation(s)": ", ".join(company_affiliations),
                "Corresponding Author Email": corresponding_author_email or "Not Available",
            })

        except KeyError as e:
            print(f"Missing field in article data: {e}")
            continue

    return pd.DataFrame(articles)

# validate the search query
def validate_query(query):
    if not query or not isinstance(query, str):
        raise ValueError("Query must be a non-empty string.")
    if len(query) < 3:
        raise ValueError("Query must be at least 3 characters long.")
    return query

# log errors ro the console or a log file
def log_error(error_message):
    print(f"[ERROR]: {error_message}")

# save the data to csv
def save_results_to_csv(df, filename="results.csv"):
    try:
        df.to_csv(filename, index=False)
        print(f"Results saved to {filename}")
    except Exception as e:
        print(f"Error saving to CSV: {e}")
