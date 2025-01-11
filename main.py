import argparse
from pubmed_cli.fetch import fetch_papers
from pubmed_cli.utils import format_papers, save_results_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed articles.")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("--max_results", type=int, default=10, help="Maximum number of results to fetch")
    parser.add_argument("-f", "--file", type=str, help="Save results to the specified CSV file")
    
    args = parser.parse_args()

    try:
        if args.debug:
            print("Debug mode is enabled.")
            print(f"Query: {args.query}")
            print(f"Max Results: {args.max_results}")
            if args.file:
                print(f"Output File: {args.file}")

        papers = fetch_papers(args.query, args.max_results)
        print(f"Fetched {len(papers)} papers for query: {args.query}")

        if papers:
            df = format_papers(papers)

            if args.file:
                save_results_to_csv(df, filename=args.file)
        else:
            print("No papers found for the given query.")
    
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

print('Hello World')