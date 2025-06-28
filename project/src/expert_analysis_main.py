# import the Class WebsiteScraping from website_scraping_class
from project.src.website_scraping_class import WebsiteScraping


def main():
    # Create an object of the WebsiteScraping class
    nasdaq100_scraping = WebsiteScraping()

    condition = True

    while condition is True:

        print('------------------------')
        print('What do you want to do?\n'
              'Please select a number:\n'
              '1. Show the Nasdaq 100 stocks as a table and sort them by consensus rating in descending order.\n'
              '2. Show the historical consensus rating for a stock as a boxplot.\n'
              '3. Show the historical consensus rating for one or more stocks as a boxplot.\n'
              '4. Show the historical consensus rating for a stock compared to all other Nasdaq 100 stocks.\n'
              '5. Show the best or worst stocks for a given date.\n'
              '6. Download the historical expert analysis for a specific stock as a CSV file.\n'
              '7. Download the historical expert analyses for all Nasdaq 100 stocks as a CSV file.\n'
              '8. exit!')

        input_number = input().strip()

        if input_number == '1':
            nasdaq100_scraping.sort_according_the_consensus_rating()

        elif input_number == '2':
            nasdaq100_scraping.check_consensus_rating_for_one_stock()

        elif input_number == '3':
            nasdaq100_scraping.check_consensus_rating_for_several_stocks()

        elif input_number == '4':
            nasdaq100_scraping.check_consensus_rating_compare_with_other_stocks()

        elif input_number == '5':
            nasdaq100_scraping.classify_stocks_by_consensus_rating()

        elif input_number == '6':
            print('Enter the name of the Stock!')
            stock_name = input().strip().lower()
            nasdaq100_scraping.historical_analysis_for_one_stock(stock_name)

        elif input_number == '7':
            nasdaq100_scraping.historical_analysis_for_all_stocks()

        elif input_number == '8':
            condition = False


if __name__ == '__main__':
    main()
