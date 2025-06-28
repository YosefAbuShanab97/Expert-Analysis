# import different modules and libraries.
import numpy as np
import pandas as pd
import re
from project.src.get_soup_function import get_soup
import datetime
import matplotlib.pyplot as plt
import glob
import csv
import os


class WebsiteScraping:

    # The variables defined in the constructor are instance variables, that is, variables that describe that instance.
    def __init__(self):

        # Constructor Variables:

        # The base Url to extract all information about NASDAQ 100 Stocks.
        self.base_url = 'https://www.finanzen.net/'

        # Index and function to extract the number of pages from the specified stock values.
        self.index_url_Name = 'index/'
        self.get_name_function = 'nasdaq_100/fundamental'

        # Index to extract the names of Nasdaq 100 stocks.
        self.index_estimate = "schaetzungen/"

        # Index and function to extract the historical information of Nasdaq 100 Stocks.
        self.historical_index = 'analysen/'
        self.historical_function = '-analysen'

        # List store the number of experts who recommended "Buy", "Sell", "Hold",
        # etc. for the stocks.
        self.listOfValues = []

        # List to store the Name of the Columns of the Stocks Table.
        # "Buy", "Sell", "Hold",...
        self.attribute = []

        # List to store the names of the stocks for Url.
        # https://www.finanzen.net/aktien/activision_blizzard-aktie
        # like: activision_blizzard
        self.list_Names_for_URl = []

        # List to store the names of the stocks not for Url.
        # Like: Activision Blizzard
        self.Stock_Name_not_for_Url = []

        # List to store the page number on which, for example, the names of the shares are divided,
        # for example : ?p=1 ... ?p=12
        self.List_estimate_index = []

    # --------------------------------------------------------------------------------------------------------------

    # Method to automatically save the page number for the specified url in a list.
    def get_page_numbers(self, baseurl_par=None, index_url_name_par=None, index_get_name_par=None):

        try:
            # If the parameter is not entered as a string, an error message is thrown.
            if baseurl_par is not None or index_url_name_par is not None or index_get_name_par is not None:
                if not isinstance(baseurl_par, str) or not isinstance(index_url_name_par, str) or not isinstance(
                        index_get_name_par, str):
                    raise TypeError()

            # When parameters are entered, a strip() function is used to remove the space from the
            # entered parameters.
            if baseurl_par is not None:
                baseurl_par = baseurl_par.strip()
                index_url_name_par = index_url_name_par.strip()
                index_get_name_par = index_get_name_par.strip()

            # If no parameter is specified, a URL is entered by default.
            if baseurl_par is None or index_url_name_par is None or index_get_name_par is None:
                baseurl_par = self.base_url
                index_url_name_par = self.index_url_Name
                index_get_name_par = self.get_name_function

            # Get the Content of the Page get_Soup Function and using BeautifulSoup.
            data_soup = get_soup(baseurl_par + index_url_name_par + index_get_name_par)

            # Search for the class: 'page-content__container' and save it in data_class.
            data_class = data_soup.find("nav", {'class': 'pagination margin-top-1.00'})

            # Find all a tags in data_class.
            links = data_class.findAll("a")

            # Extract the ?p= from the Page.
            extract_page_string = [re.search(r'(\?p=)\d+', link['href']).group(1) for link in links]

            # Extract the numbers from the Page to check the length of the Pages.
            extract_length_page = [re.search(r'\?p=(\d+)', link['href']).group(1) for link in links]

            # Sort the numbers in ascending order and remove the duplicates with set.
            sortierte_zahlen = sorted(set(extract_length_page), key=int)

            # Extract the last number from the list and store it in the variable last_number.
            last_number = int(sortierte_zahlen[-1])

            # Store the first ?p= in the page_str variable.
            page_str = extract_page_string[0]

            # Extract the first number from the sort numbers and store it in the count.
            count = int(sortierte_zahlen[0])

            # Run a forloop with the range of pages and create the ?p= with the numbers and save it in the list.
            for i in range(last_number):
                page_string = page_str + str(count)
                self.List_estimate_index.append(page_string)
                count += 1

        # Here the exception are thrown.
        except TypeError:
            print('please enter the Parameter as string!')

        except Exception as e:
            print("There is just a one page!", f'<{e}>')

    # ---------------------------------------------------------------------------------------------------------------

    # Method to extract the names of the Stocks from NASDAQ 100.
    def get_name_nasdaq100(self, baseurl_par=None, index_url_name_par=None, index_get_name_par=None):

        try:
            # If the parameter is not entered as a string, an error message is issued.
            if baseurl_par is not None or index_url_name_par is not None or index_get_name_par is not None:
                if not isinstance(baseurl_par, str) or not isinstance(index_url_name_par, str) or not isinstance(
                        index_get_name_par, str):
                    raise TypeError()

            # When parameters are entered, a strip() function is used to remove the space from the
            # entered parameters.
            if baseurl_par is not None:
                baseurl_par = baseurl_par.strip()
                index_url_name_par = index_url_name_par.strip()
                index_get_name_par = index_get_name_par.strip()

            # Here the method self.geturl_index() is called to add the number of pages to the list.
            self.get_page_numbers()

            # If no parameter is specified, a URL is entered by default.
            if baseurl_par is None or index_url_name_par is None or index_get_name_par is None:
                baseurl_par = self.base_url
                index_url_name_par = self.index_url_Name
                index_get_name_par = self.get_name_function

            # Here a for loop is run over the self.List_estimate_index, in this list the numbers of the page are
            # stored,i.e. if the stocks are divided on two different pages the numbers are stored in this list.
            for i in self.List_estimate_index:
                # 'i' here is the page number, for example ?p=1.
                data_soup = get_soup(baseurl_par + index_url_name_par + index_get_name_par + i)

                # Search for the class: 'page-content__container' and save it in the data_class.
                data_class = data_soup.find("section", {'class': 'page-content__container'})

                # Search for the Links in data_class and save it in the data_a.
                data_a = data_class.findAll('a')

                # For loop from index 67 to 117 over found links.
                for link in data_a[67:117]:
                    # Convert the link to a string.
                    convert_string = str(link)
                    # Used the search function from the re library to search for specific text
                    # to extract the stock names.
                    found_string = re.search(r'href="/aktien/(.*?)-aktie"', convert_string)

                    # If the searched text is found, the searched text is extracted and stored in the variable
                    # found_string, if not then None is stored.
                    if found_string:
                        string_found = found_string.group(1)
                    else:
                        string_found = None
                    self.list_Names_for_URl.append(string_found)

        # Here the exception are thrown.
        except TypeError:
            print('please enter the Parameter as string!')

        except Exception as e:
            print("There is no Index found!", f'<{e}>')

    # -------------------------------------------------------------------------------------------------------------

    # Method of extracting the expert evaluation of whether to buy, sell or hold the stock
    # for each stock from Finanzen.net.
    def get_info_for_stock(self, stock):

        try:
            # The Lower function is used to convert the parameter to lowercase
            # and the Strip function to remove all leading and trailing spaces from the text.
            stock = stock.lower().strip()

            # Here the get_soup function is used to extract the content of the page.
            data_soup = get_soup(self.base_url + self.index_estimate + stock)
            data_div = data_soup.find("div", {'class': 'grid__item-6 grid__item-12--md'})
            data_td = data_div.findAll('td', {'class': 'table__td'})
            data_h2 = data_div.find('h2')
            stock_name = data_h2.text

            # Here the stock name is searched for and stored in the found_astring variable.
            found_astring = re.search(r'Analysten Empfehlungen zu (.+?)$', stock_name)
            if found_astring:
                result = found_astring.group(1)
                self.Stock_Name_not_for_Url.append(result)

            # List to save the values of buy,sell,hold,overweight,underweight.
            value = []

            # For loop to store the values and column names for a specific stock.
            for i in data_td:
                value.append(i.text)

            # Save Columns Names.
            self.attribute = value[5:]
            # Save Values for each Stock.
            value = value[:5]

            # Store the data in self.listOfValues list.
            self.listOfValues.append(value)

        # If no data is found for the stock, then the exception is thrown and the code continues.
        except Exception as e:
            print('There is No data Found for the Stock:', f'{stock}!', f'<{e}>')

    # --------------------------------------------------------------------------------------------------------------

    # This method takes the stock names as a list as parameter and saves the extracted data
    # about the stocks as a csv file.
    def get_info_for_all_stocks(self, list_stock=None):

        try:
            # Here the method "get_name_nasdaq100()" is called to extract the name of the Nasdaq 100,
            # which is necessary for this method to extract the information of the stocks.
            self.get_name_nasdaq100()

            # If no parameter is specified, a default value is entered for this parameter.
            # The default value is the list of Nasdaq100 stock names.
            if list_stock is None:
                list_stock = self.list_Names_for_URl

            # Extract the information about the whole stock with For loop.
            for i in list_stock:
                self.get_info_for_stock(i)

            # Define DataFrame consisting of columns and data. And these columns and data are filled by
            # the two lists(attribute,listofvalues).
            df_nasdaq100_expert = pd.DataFrame(columns=self.attribute, data=self.listOfValues)

            # New column(Name) is inserted at index 0 in the DataFrame.
            df_nasdaq100_expert.insert(0, 'Name', self.Stock_Name_not_for_Url)

            # New column(Konsensrating) is inserted at index 1 in the DataFrame.
            df_nasdaq100_expert.insert(1, 'Konsensrating', '-')

            # If there is no number in a numeric list, it will be replaced with 'not Number'(Non value).
            df_nasdaq100_expert = df_nasdaq100_expert.replace('', np.nan)
            df_nasdaq100_expert = df_nasdaq100_expert.fillna('  Non Value')

            # Generate a timestamp.
            timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S")

            # Save the CSV file with the timestamp in the File_name.
            file_name = f"expert_analysis_data_of_nasdaq100_timestamp_{timestamp}.csv"

            # Replace the : with a -, because the operating system of the computer does not accept the :
            file_name = file_name.replace(":", "-")
            df_nasdaq100_expert.to_csv(file_name, index=False)
            print("Successfully saved:", file_name)

        # Here the exception are thrown.
        except Exception as e:
            print("The File was not saved successfully!", f'<{e}>')

    # ----------------------------------------------------------------------------------------------------------

    # Method to calculate the consensus rating for each stock.
    def calculate_consensus_rating(self):

        try:
            # Here the method "get_info_for_all_stocks()" is called to extract the expert
            # analysis for the Nasdaq 100 stocks.which is necessary for this
            # method to sort the stocks in ascending order.
            self.get_info_for_all_stocks()

            # Generate a timestamp.
            timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
            file_name = f"expert_analysis_data_of_nasdaq100_timestamp_{timestamp}.csv"
            # Replace the : with a - because the operating system of the computer does not accept the :
            file_name = file_name.replace(":", "-")
            df = pd.read_csv(file_name)

            # Here the iterrows() function is used to run through the whole rows.
            for index, row in df.iterrows():
                buy_value = row['Buy']
                hold_value = row['Hold']
                sell_value = row['Sell']

                # If there are no analysts for a particular stock, then None
                # is entered in the Consensus Rating column.
                if buy_value == "  Non Value":
                    df.at[index, 'Konsensrating'] = None

                # If this is not the case, the consensus rating is calculated.
                else:
                    # div_value is the number of experts advising buy, sell, hold, underweight and overweight.
                    div_value = int(row['Buy']) + int(row['Overweight']) + int(row['Hold']) + int(
                        row['Underweight']) + int(row['Sell'])

                    # If the div_value is 0 we divide by 1.
                    if div_value == 0:
                        consecrating_value = ((int(buy_value) * 5) + (int(hold_value) * 3) + (int(sell_value) * 1)) / 1
                        df.at[index, 'Konsensrating'] = consecrating_value

                    else:
                        consecrating_value = ((int(buy_value) * 5) + (int(hold_value) * 3) + (
                                int(sell_value) * 1)) / int(div_value)

                        # Here the round() function is used to round up the number by 3 commas.
                        df.at[index, 'Konsensrating'] = round(consecrating_value, 3)
            # DataFrame to be saved as a Csv file.
            df.to_csv(file_name, index=False)

        # Here the exception are thrown.
        except Exception as e:
            print('The consensus rating cannot be calculated!', f'<{e}>')

    # -----------------------------------------------------------------------------------------------------------

    # Method to sort the stocks by the highest consensus rating.
    def sort_according_the_consensus_rating(self):

        try:

            # Here the method "calculate_consensus_rating()" is called to calculate the consensus rating of
            # the shares, which is necessary for sorting the shares.
            self.calculate_consensus_rating()

            # Generate a timestamp
            timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
            file_name = f"expert_analysis_data_of_nasdaq100_timestamp_{timestamp}.csv"
            # Replace the : with a - because the operating system of the computer does not accept the:
            file_name = file_name.replace(":", "-")
            # Read the CSV File
            df = pd.read_csv(file_name)

            # Sort the table by the values in the Consensus Rating column in ascending order.
            df.sort_values(by='Konsensrating', ascending=False, inplace=True)
            # dataFrame to be saved as a Csv file.
            df.to_csv(file_name, index=False)

        # Here the exception are thrown.
        except Exception as e:
            print('The stocks cannot be sorted!', f'<{e}>')

    # -------------------------------------------------------------------------------------------------------------

    # Method to check the historical consensus rating for a stock and display it as a boxplot.
    @staticmethod
    def check_consensus_rating_for_one_stock():

        try:
            # Console Input.
            print("Please enter the name of the stock to check the current consensus rating of this stock "
                  "compared to the old consensus rating:")
            # To store the entered value in the value stock_parameter before converting the entered value to lowercase,
            # so that if the stock is not found, a field message is issued with the entered value.
            stock_parameter = input().strip()

            # Remove the spaces from the entered value and convert it to a small letters.
            stock = stock_parameter.lower()

            # A list to save the consensus score of all Csv files of the entered Stock.
            list_for_consents_rating = []

            # The path where the csv files are located.
            directory = 'C:/Users/yosef/expert-analysis/project/data/input_data_in_our_code/' \
                        'input_data_of_expert_analysis_for_the_other_methods/'

            # A for loop over all CSV files.
            for i in glob.glob(directory + '*.csv'):
                # To open the first csv file
                with open(i, 'r') as csv_file:
                    # Save the read csv file in the value Csv_File.
                    csv_file = csv.reader(csv_file)

                    # A for loop over each line in the read csv file.
                    for row in csv_file:
                        # Reads the name of each line and stores it in the stock_name variable.
                        stock_name = row[0].lower()

                        # Reads the consensus rating of each line and stores it in the stock_name variable.
                        consecrating = row[1]

                        # If the stock name matches the entered stock name.
                        if stock_name == stock:
                            # If there is no consensus rating or the consensus rating is a string in one csv
                            # file, then skip.
                            if consecrating == '' or consecrating is str:
                                pass
                            else:
                                # Save the consensus rating of this stock in the list as a float.
                                list_for_consents_rating.append(float(consecrating))

            # If there is no consensus rating for the entered stock and the list of consensus ratings is empty,
            # an error message is displayed.
            if consecrating == '' and len(list_for_consents_rating) == 0:
                print(f'This Stock: {stock} is not found!')

            # Show the consensus rating for this Stock as a boxplot.
            else:
                # Determine the values of the boxplot.
                median = round(np.median(list_for_consents_rating), 3)
                maximum = round(np.max(list_for_consents_rating), 3)
                q1 = round(np.percentile(list_for_consents_rating, 25), 3)
                q3 = round(np.percentile(list_for_consents_rating, 75), 3)
                minimum = round(np.min(list_for_consents_rating), 3)

                # Create a boxplot from the consensus rating list.
                plt.boxplot(list_for_consents_rating)

                # Adding the statistical values to the boxplot.
                plt.text(0.85, median, f'Median: {median}', va='bottom')
                plt.text(0.85, maximum, f'Max: {maximum}', va='bottom')
                plt.text(0.85, minimum, f'Min: {minimum}', va='bottom')
                plt.text(0.85, q1, f'Q1: {q1}', va='top')
                plt.text(0.85, q3, f'Q3: {q3}', va='bottom')

                # Using the length of the list to extract the index of the
                # last value and then extract the current value from the list.
                length = len(list_for_consents_rating)
                current_conses = list_for_consents_rating[length - 1]

                # Display of the current value of the consensus rating of the entered Stock
                # as a parameter in the boxplot as a red diamond.
                konsens_value = current_conses
                plt.plot(1, konsens_value, 'D', color='red', markersize=6)
                plt.annotate(f'{konsens_value}', (1, konsens_value), xytext=(3, 7), textcoords='offset points',
                             color='red')

                plt.boxplot(list_for_consents_rating, showfliers=True)
                # Create title to boxplot.
                plt.title(f"Historical consensus rating of the Stock: {stock_parameter}")
                # Create Name for x-axis.
                plt.xlabel(f'{stock_parameter}')
                # Create Name for y-axis.
                plt.ylabel("Consensus rating")
                # Set the size for the red diamond (Current Consensus rating) to 6.
                size = 6
                # Create a scatter with a single point.
                plt.scatter([1], [konsens_value], marker='D', color='red', s=size, label='Current Consensusrating')
                # Add a legend to the boxplot and set the fontsize of the legend to 8.
                plt.legend(fontsize=8)
                # Show boxplot.
                plt.show()

        # Here the exception are thrown.
        except Exception as e:
            print('This Stock is not Found!', f'<{e}>')

    # -----------------------------------------------------------------------------------------------------------------

    # Method to check the historical consensus rating for a one stock or for several
    # stocks and display it as a boxplot.
    @staticmethod
    def check_consensus_rating_for_several_stocks():

        try:
            # List to save the entered stock name as lowercase, which is necessary for searching in the csv files.
            list_parameter_stock_name_with_lower = []
            # List to save the entered Stock name, which is necessary for naming the X and Y axis.
            list_parameter_stock_name_without_lower = []

            print("Please enter the name of the stock to check the current consensus rating of this stock "
                  "compared to the old consensus rating:")
            stock_parameter = input().strip()
            list_parameter_stock_name_without_lower.append(stock_parameter)

            # Convert the parameter to small letters, to check it with the names of the Stocks in the Csv Files.
            stock_name = stock_parameter.lower().strip()
            list_parameter_stock_name_with_lower.append(stock_name)
            condition = True

            index_list = 0

            while condition is True:

                print('Do you want to search for other Stock (Yes / No)?.')
                yes_or_no = input().lower().strip()

                if yes_or_no == 'yes':

                    print('Please enter the name of the Stock:')
                    name_new_stock_input = input().strip()
                    stock_name_without_lower = name_new_stock_input
                    list_parameter_stock_name_without_lower.append(stock_name_without_lower)
                    name_new_stock = name_new_stock_input.lower()
                    list_parameter_stock_name_with_lower.append(name_new_stock)

                elif yes_or_no == 'no':
                    condition = False

            # A list for a consecrating.
            konsens_rating_of_stock_name_parameter = []

            # The path where the csv files are located.
            directory = 'C:/Users/yosef/expert-analysis/project/data/input_data_in_our_code/' \
                        'input_data_of_expert_analysis_for_the_other_methods/'

            # A for loop over the stocks name in the list list_parameter_stock_name_with_lower.
            for stocks_names in list_parameter_stock_name_with_lower:

                # A for loop over all csv files.
                for i in glob.glob(directory + '*.csv'):

                    # Read the file.
                    with open(i, 'r') as csv_file:
                        csv_file = csv.reader(csv_file)

                        # A for loop over all lines of this csv file.
                        # and save the Stock name and the consecrating in the variables
                        # stock_name and consecrating.
                        for row in csv_file:
                            stock_name = row[0].lower()
                            consecrating = row[1]
                            # if the stock is found then save the consensus rating of that stock in the list.
                            if stock_name == stocks_names:
                                konsens_rating_of_stock_name_parameter.append(float(consecrating))

                # If the stock is not found and there is no consensus rating for that stock then
                # throw an error message.
                if consecrating == '' and len(konsens_rating_of_stock_name_parameter) == 0:
                    print(f'This Stock: {stock_parameter} is not found!')

                else:
                    # Determine the values of the boxplot.
                    median = round(np.median(konsens_rating_of_stock_name_parameter), 3)
                    maximum = round(np.max(konsens_rating_of_stock_name_parameter), 3)
                    q1 = round(np.percentile(konsens_rating_of_stock_name_parameter, 25), 3)
                    q3 = round(np.percentile(konsens_rating_of_stock_name_parameter, 75), 3)
                    minimum = round(np.min(konsens_rating_of_stock_name_parameter), 3)

                    # Create a boxplot from the list.
                    plt.boxplot(konsens_rating_of_stock_name_parameter)

                    # Adding the statistical values to the boxplot.
                    plt.text(0.85, median, f'Median: {median}', va='bottom')
                    plt.text(0.85, maximum, f'Max: {maximum}', va='bottom')
                    plt.text(0.85, minimum, f'Min: {minimum}', va='bottom')
                    plt.text(0.85, q1, f'Q1: {q1}', va='top')
                    plt.text(0.85, q3, f'Q3: {q3}', va='bottom')

                    # Using the length of the list to extract the index of the
                    # last value and then extract the current value from the list.
                    length = len(konsens_rating_of_stock_name_parameter)
                    current_conses = konsens_rating_of_stock_name_parameter[length - 1]

                    # Display of the current value of the consensus rating of the entered Stock
                    # as a parameter in the boxplot as a red diamond.
                    conses_value = current_conses
                    plt.plot(1, conses_value, 'D', color='red', markersize=6)
                    plt.annotate(f'{conses_value}', (1, conses_value), xytext=(3, 7), textcoords='offset points',
                                 color='red')

                    plt.boxplot(konsens_rating_of_stock_name_parameter, showfliers=True)
                    # Create title to boxplot.
                    plt.title(f"Historical consensus rating of the Stock: "
                              f"{list_parameter_stock_name_without_lower[index_list]}")
                    # Create Name for x-axis.
                    plt.xlabel(f'{list_parameter_stock_name_without_lower[index_list]}')
                    index_list += 1
                    # Create Name for y-axis.
                    plt.ylabel("Consensus rating")
                    # Set the size for the red diamond (Current Consensus rating) to 6.
                    size = 6
                    # Create a scatter with a single point.
                    plt.scatter([1], [conses_value], marker='D', color='red', s=size, label='Current Consensusrating')
                    # Add a legend to the boxplot and set the fontsize of the legend to 8.
                    plt.legend(fontsize=8)
                    # Show boxplot.
                    plt.show()
                # To make the list empty to avoid the duplicates.
                konsens_rating_of_stock_name_parameter.clear()

        # Here the exception are thrown.
        except Exception as e:
            print('The boxplot cannot be displayed!', f'<{e}>')

    # --------------------------------------------------------------------------------------------------------------

    # This method displays the consensus rating of the entered stock as a parameter in the boxplot with a red color
    # compared with the current consensus rating all other stocks(Nasdaq 100 stocks).
    @staticmethod
    def check_consensus_rating_compare_with_other_stocks():

        try:
            print("Please enter the name of the stock to check the current consensus rating of "
                  "this stock compared to the consensus rating of the other stocks (Nasdaq 100):")

            # With strip() to remove the leading and trailing blanks.
            stockname_parameter = input().strip()

            # Here the entered parameter is checked to make sure that
            # it does not contain a space and is converted to lowercase.
            stock = stockname_parameter.lower().strip()

            # Here the consensus rating for the entered parameters in this list is saved.
            consensus_rating_list_of_stockname_parameter = []

            # Here the last CSV file is saved to display this CSV file as boxplot.
            last_csvfile = None

            # The path where the csv files are located.
            directory = 'C:/Users/yosef/expert-analysis/project/data/input_data_in_our_code/' \
                        'input_data_of_expert_analysis_for_the_other_methods/'

            # Using this For loop, we go through the entire CSV files and extract the consensus rating for the
            # parameters entered from the entire CSV files and store it in the
            # consecrating_of_stockname_parameter = [] list.
            for i in glob.glob(directory + '*.csv'):
                last_csvfile = i
                with open(i, 'r') as csv_file:
                    csv_file = csv.reader(csv_file)
                    for row in csv_file:
                        stock_name = row[0].lower()
                        consecrating = row[1]

                        # If the entered parameter (stock name) exists in one of the available CSV files,
                        # the consensus rating of this stock will be saved in the
                        # list: Consensus_rating_ofStockname_par = [].
                        if stock_name == stock:
                            consensus_rating_list_of_stockname_parameter.append(float(consecrating))

            # If the entered stock name does not exist in the CSV files or does not have a consensus score,
            # a message will be displayed that this stock either does not have a consensus score or does not
            # exist in the CSV files.
            if consecrating == '' and len(consensus_rating_list_of_stockname_parameter) == 0:
                print(f'This Stock: {[stockname_parameter]} is not found!')

            # And if that registered stock exists and has a consensus score,
            # then the current consensus score of that stock is displayed in a boxplot.
            else:
                # Read the Csv File .
                last_csv_stock = pd.read_csv(last_csvfile)
                # Remove all rows from DataFrame 'last_csv_stock' where Column 'consensus rating' is
                # missing (NaN is).
                # The argument "inplace=True" causes the changes to be made directly in the original
                # DataFrame without creating a new cop
                last_csv_stock.dropna(subset=['Konsensrating'], inplace=True)

                # Create a new figure for the boxplot diagram with a size of 10x6.
                plt.figure(figsize=(10, 6))
                # Create a boxplot chart based on the data in the 'consensus rating' column of
                # the 'last_csv_stock' DataFrame.
                plt.boxplot(last_csv_stock['Konsensrating'], showfliers=True)
                min_val_file = last_csv_stock['Konsensrating'].min()
                max_val_file = last_csv_stock['Konsensrating'].max()
                median_file = last_csv_stock['Konsensrating'].median()
                q1_file = round(last_csv_stock['Konsensrating'].quantile(0.25), 3)
                q3_file = round(last_csv_stock['Konsensrating'].quantile(0.75), 3)

                # place the text for the statistical values in the boxplot.
                plt.text(1, min_val_file, f'Min: {min_val_file}', ha='right', va='bottom')
                plt.text(1, max_val_file, f'Max: {max_val_file}', ha='right', va='top')
                plt.text(1, median_file, f'Median: {median_file}', ha='right', va='center')
                plt.text(1, q1_file, f'Q1: {q1_file}', ha='right', va='top')
                plt.text(1, q3_file, f'Q3: {q3_file}', ha='right', va='bottom')

                # Give a name to the heading for the boxplot and for the X and Y axes.
                plt.title(f"consensus rating of the Stock: {stockname_parameter}")
                plt.xlabel(stockname_parameter)
                plt.ylabel("Consensus rating")

                # Here, the current consensus score of the entered stock is stored
                # in CurrentValue and then displayed as a red diamond in the boxplot.
                length = len(consensus_rating_list_of_stockname_parameter)
                current_value = consensus_rating_list_of_stockname_parameter[length - 1]

                conses_value = current_value
                plt.plot(1, conses_value, 'D', color='red', markersize=6)
                plt.annotate(f'{conses_value}', (1, conses_value), xytext=(3, 7), textcoords='offset points',
                             color='red')
                # Set the size for the red diamond (Current Consensus rating) to 6.
                size = 6
                # Create a scatter with a single point.
                plt.scatter([1], [conses_value], marker='D', color='red', s=size, label='Current Consensusrating')
                # Add a legend to the boxplot and set the fontsize of the legend to 8.
                plt.legend(fontsize=8)
                # Show boxplot
                plt.show()

        # Here the exception are thrown.
        except Exception as e:
            print('The boxplot cannot be displayed!', f'<{e}>')

    # ------------------------------------------------------------------------------------------------------------

    # The method displays both the good and the poor stocks for a given date. Stocks with consensus
    # ratings higher than the average of all stocks are considered good stocks, whereas those with ratings
    # lower than the average of all stocks are considered not good stocks.
    @staticmethod
    def classify_stocks_by_consensus_rating():

        try:
            print('Here you can see the NASDAQ100 stocks with the best conses rating by a certain date *_*!')
            print('Note: Please enter the date in this notation: DD-MM-YYYY!')
            date = input().strip()

            # A list to save the csv files to search in this file for the good and not good stocks.
            list_csv_files = []

            # A List to save the name of the Csv files.
            list_file_names = []

            # A list to show the available dates if an incorrect date is entered.
            list_for_available_dates = []

            # The path where the csv files are located.
            directory = 'C:/Users/yosef/expert-analysis/project/data/input_data_in_our_code/' \
                        'input_data_of_expert_analysis_for_the_other_methods/'

            # Here, the glob function(Modul) is used to search in the directory.
            for file in glob.glob(directory + '*.csv'):
                file_path = file
                # Extract the name of the file and save it in the file_name variable.
                file_name = os.path.basename(file_path)
                # Convert the file name to string.
                file_name_string = str(file_name)

                # If the csv file does not start with h, it means that this csv file is not a historical file,
                # then save it to the list, and split the file name it by the 6 (_).
                if not file_name_string.startswith('h'):
                    date_split = file_name_string.split("_")[6]
                    list_for_available_dates.append(date_split)

            print('---------------------------------------------------------------------------------------------'
                  '---------------------')

            condition = True

            # A while loop offers the possibility, if a date is entered incorrectly, to give the date again.
            while condition is True:

                # Variable to check if the file is found or not.
                file_found = False

                # Here, the glob function(Modul) is used to search for a specific directory.
                for file in glob.glob(directory + '*.csv'):
                    file_path = file
                    # Extract thr file name.
                    file_name = os.path.basename(file_path)
                    # Convert the file name to string.
                    file_name_string = str(file_name)
                    # Split the file name it by the 6 (_).
                    date_split = file_name_string.split("_")[6]

                    # If the entered date is found, offer the possibility of displaying whether the
                    # good or the bad stocks.
                    if date == date_split:
                        print('Do you want to see the good stocks or the bad stocks (good, not good)?')
                        input_answer = input()
                        file_found = True

                        # Create DataFrame from CSV file.
                        nasdaq100_csv_files = pd.read_csv(file, delimiter=',')
                        list_file_names.append(file_name)

                        # Add Csv Files to the list.
                        list_csv_files.append(nasdaq100_csv_files)

                        # Extract the consensus rating column of the first table
                        consensus_rating_first_row = list_csv_files[0]['Konsensrating']

                        # Calculate the average of the consensus rating.
                        average_consensus_rating = round(consensus_rating_first_row.mean(), 3)

                        # Here the columns name and consensus rating are extracted from the csv file and combined.
                        name_column = list_csv_files[0]['Name']
                        consecrating_column = list_csv_files[0]['Konsensrating']
                        combined_both_columns = pd.concat([name_column, consecrating_column], axis=1)

                        list_of_good_stocks = []
                        list_of_not_good_stocks = []

                        # Here, a for loop is over the combined columns, and if the consensus rating
                        # is less than the average,all consensus ratings and the name of the stock are stored
                        # in the List_notGoodStocks, if greater, in the List_GoodStocks.
                        for index, row in combined_both_columns.iterrows():
                            current_value = row['Konsensrating']

                            if current_value > average_consensus_rating:
                                list_of_good_stocks.append((row['Name'], current_value))
                            else:
                                list_of_not_good_stocks.append((row['Name'], current_value))

                        if input_answer == 'good':
                            print('---------------------------------------------------------------------------'
                                  '---------------------------------------')
                            print('We recommend you to buy these stocks:')
                            print('--------------------------------------')
                            # count variable to count the number of good stocks.
                            count = 1
                            # for loop over the good stock list.
                            for i in list_of_good_stocks:
                                # Extract the name and the consensus rating from the list.
                                stock_name = i[0]
                                consensus_rating = i[1]
                                good_stocks = f"{count}.{stock_name}: {consensus_rating}"
                                count = count + 1
                                print(good_stocks)

                            print('---------------------------------------------------------------------------'
                                  '---------------------------------------')
                            print('The average of the consensus rating of all stocks:')
                            print(average_consensus_rating)
                            print('---------------------------------------------------------------------------'
                                  '---------------------------------------')

                            condition = False
                            break

                        if input_answer == 'not good':
                            print('---------------------------------------------------------------------------'
                                  '---------------------------------------')
                            print('We recommend you not to buy these stocks:')
                            print('------------------------------------------')
                            # count variable to count the number of not good stocks.
                            counter = 1
                            # for loop over the good stock list.
                            for i in list_of_not_good_stocks:
                                # Extract the name and the consensus rating from the list.
                                stock_name = i[0]
                                consensus_rating = i[1]
                                not_good_stocks = f"{counter}.{stock_name}: {consensus_rating}"
                                counter = counter + 1
                                print(not_good_stocks)

                            print('---------------------------------------------------------------------------'
                                  '---------------------------------------')
                            print('The consensus rating covers all Stocks:')
                            print(average_consensus_rating)
                            print('-----------------------------------------------------------------------------'
                                  '-------------------------------------')
                            condition = False
                            break

                # If the entered date is not available, the possibility to enter a new date and display
                # a list of available dates.
                if not file_found:
                    print('The Date is not Found!')
                    print('You must select a date from the following dates! *_* :')
                    for i in list_for_available_dates:
                        if i.startswith('h'):
                            pass
                        else:
                            print(i)

                    print('Here you can see the NASDAQ100 stocks with the best conses rating by a certain date *_*!')
                    print('Note: Please enter the date in this notation: DD-MM-YYYY!')
                    date = input().strip()

        # Here the exception are thrown.
        except Exception as e:
            print('The Date is not Found!', f'<{e}>')

    # --------------------------------------------------------------------------------------------------------------

    # This method extracts historical expert analysis for a given stock.
    def historical_analysis_for_one_stock(self, stockname_parameter=None):
        # If no parameter is entered, a default value is entered.
        if stockname_parameter is None:
            stockname_parameter = 'alphabet_a'

        try:
            # A list to use the extracted stock name from the web page for naming the CSV file.
            # like: AMD (Advanced Micro Devices).
            stock_names = []

            # A list for saving positive/negative/neutral.
            span_list = []

            # A list to store all the values in this list, and positive/negative/neutral will
            # be replaced by buy/sell/hold in this list, so this list will contain the final values
            # that we will create as a DataFrame.
            value_list = []

            # A list for saving the Date.
            date = []

            # A list for saving the Name of the Bank.
            bank_name = []

            # A list to convert positive/negative/neutral to buy/sell/hold.
            buy_sell_hold = []

            # A list for saving the Name of the Stock,
            # like: AMD (Advanced Micro Devices) Outperform
            stock_name = []

            # Save the parameter in the variable stock_name_parameter.
            stock_name_parameter = stockname_parameter

            # To make the list empty to avoid the duplicates.
            self.List_estimate_index.clear()

            # Call the geturl_index() method to extract the page numbers.
            self.get_page_numbers(self.base_url, self.historical_index, stock_name_parameter +
                                  self.historical_function)

            # Check the length of the list "self.List_estimate_index" and store it in the variable "length_list".
            length_list = len(self.List_estimate_index)

            # If the historical expert analyses are only present on one page, i.e. the list of pages is empty,
            # the If statement is executed, and if the list is not empty, the Else statement is executed.
            # that solves the problem when the data are only in one page to extract.
            if length_list == 0:
                # Extract the Content of the Url.
                data_soup = get_soup(self.base_url + self.historical_index + stock_name_parameter +
                                     self.historical_function)
                # Here, the valuation is derived from the share: positive/negative/neutral.
                data_leading = data_soup.find("div", {'class': 'page-content__leading'})

                # Extract the name of the stock from the web page to use it for naming the CSV file.
                the_stock_name = data_leading.find("h1", {'class': 'headline headline--h4'})
                the_stock_name = str(the_stock_name)
                found_str = re.search(r'class="headline headline--h4">(.*?) Aktie Analyse', the_stock_name)
                if found_str:
                    extracted_word = found_str.group(1)
                    stock_names.append(extracted_word)

                data_content = data_leading.find("div", {'class': 'horizontal-scrolling'})

                span_extract = data_content.findAll("span")
                # A for loop over all extracted spans to extract positive/negative/neutral spans
                # and store them in the span_list.
                for span in span_extract:
                    convert_tostring = str(span)
                    found_str = re.search(r'class="arrow arrow--(.*?) arrow--analysis"', convert_tostring)
                    if found_str:
                        extracted_word = found_str.group(1)
                        span_list.append(extracted_word)

                # Counter is here as Indes number.
                counter = 0

                # A for loop over all td to extract all information and store it in a New List : values List,
                # replacing the values positive/negative/neutral with buy/sell/hold.
                data_td = data_content.findAll('td')

                for i in data_td:
                    check_name = i.text.strip()
                    if check_name == 'Werbung':
                        pass
                    elif check_name == '':
                        # Here it is checked if the current element from the list: span List is
                        # positive/negative/neutral to replace it with buy/sell/hold and store it in
                        # the list: values_list.
                        if span_list[counter] == 'positive':
                            check_name = 'Buy'
                            value_list.append(check_name)
                        if span_list[counter] == 'neutral':
                            check_name = 'Hold'
                            value_list.append(check_name)
                        if span_list[counter] == 'negative':
                            check_name = 'Sell'
                            value_list.append(check_name)
                        counter += 1
                    else:
                        value_list.append(check_name)

                # A for loop over all elements in the list werte_List to extract the date.
                for date_value in value_list[0::4]:
                    date.append(date_value)

                # A for loop over all elements in the list werte_List to extract the Name of the Bank.
                for bank_value in value_list[3::4]:
                    bank_name.append(bank_value)

                # A for loop over all elements in the list werte_List to extract the buy/sell/hold.
                for recommendation in value_list[1::4]:
                    buy_sell_hold.append(recommendation)

                # A for loop over all elements in the list werte_List to extract the Name of the Stock.
                for stockname in value_list[2::4]:
                    stock_name.append(stockname)

                # To make the list empty to avoid the duplicates.
                self.List_estimate_index.clear()

            else:
                # A for loop over all page numbers to extract all information from different Pages.
                for i in self.List_estimate_index:

                    data_soup = get_soup(self.base_url + self.historical_index + stock_name_parameter +
                                         self.historical_function + i)
                    data_leading = data_soup.find("div", {'class': 'page-content__leading'})

                    # Extract the name of the stock from the web page to use it for naming the CSV file.
                    the_stock_name = data_leading.find("h1", {'class': 'headline headline--h4'})
                    the_stock_name = str(the_stock_name)
                    found_str = re.search(r'class="headline headline--h4">(.*?) Aktie Analyse', the_stock_name)
                    if found_str:
                        extracted_word = found_str.group(1)
                        stock_names.append(extracted_word)

                    # Here, the valuation is derived from the share: positive/negative/neutral.
                    data_content = data_soup.find("div", {'class': 'horizontal-scrolling'})

                    span_extract = data_content.findAll("span")

                    # A for loop over all extracted spans to extract positive/negative/neutral spans
                    # and store them in the span_list.
                    for span in span_extract:
                        convert_tostring = str(span)
                        found_str = re.search(r'class="arrow arrow--(.*?) arrow--analysis"', convert_tostring)
                        if found_str:
                            extracted_word = found_str.group(1)
                            span_list.append(extracted_word)

                    # Counter is here as Indes number.
                    counter = 0

                    # A for loop over all td to extract all information and store it in a New List : values List,
                    # replacing the values positive/negative/neutral with buy/sell/hold.
                    data_td = data_content.findAll('td')

                    for td in data_td:
                        check_name = td.text.strip()
                        if check_name == 'Werbung':
                            pass
                        elif check_name == '':
                            # Here it is checked if the current element from the list: span List is
                            # positive/negative/neutral to replace it with buy/sell/hold and store it in
                            # the list: values_list.
                            if span_list[counter] == 'positive':
                                check_name = 'Buy'
                                value_list.append(check_name)
                            if span_list[counter] == 'neutral':
                                check_name = 'Hold'
                                value_list.append(check_name)
                            if span_list[counter] == 'negative':
                                check_name = 'Sell'
                                value_list.append(check_name)
                            counter += 1
                        else:
                            value_list.append(check_name)

                    # A for loop over all elements in the list werte_List to extract the date.
                    for date_value in value_list[0::4]:
                        date.append(date_value)

                    # A for loop over all elements in the list werte_List to extract the Name of the Bank.
                    for bank_value in value_list[3::4]:
                        bank_name.append(bank_value)

                    # A for loop over all elements in the list werte_List to extract the buy/sell/hold.
                    for recommendation in value_list[1::4]:
                        buy_sell_hold.append(recommendation)

                    # A for loop over all elements in the list werte_List to extract the Name of the Stock.
                    for stockname in value_list[2::4]:
                        stock_name.append(stockname)

                # To make the list empty to avoid the duplicates.
                self.List_estimate_index.clear()

            # Here a DataFrame is created to store the entire values in this DataFrame.
            column_name = ['Date', 'Buy/Sell/Hold', 'Name', 'Bank Name']
            data = {
                'Date': date,
                'Buy/Sell/Hold': buy_sell_hold,
                'Name': stock_name,
                'Bank Name': bank_name
            }

            # Save the CSV file with the timestamp in the File_name
            df = pd.DataFrame(data, columns=column_name)
            timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S")

            file_name = f"historical_expert_analysis_data_of_the_Stock:{stock_names[0]}_timestamp_{timestamp}" \
                        f".csv"

            # Stock_names
            # replace the : with a - because the operating system of the computer does not accept the :
            file_name = file_name.replace(":", "_")
            df.to_csv(file_name, index=False)

            print("Successfully saved:", file_name)

        # Here the exception are thrown.
        except Exception as e:
            print('The file was not saved successfully!, because there is no data Found!', f'<{e}>')

    # --------------------------------------------------------------------------------------------------------------

    # This method extracts historical expert analysis for all Nasdaq 100 Stocks.
    def historical_analysis_for_all_stocks(self):

        try:
            # Here the list "self.ListSetting_index" is made empty so that we don't have an old page
            # numbers after the call of the other Methods.
            self.List_estimate_index.clear()
            # Calling the method "self.get_name_nasdaq100()" to populate the list with the stock names of
            # the NASDAQ 100.
            self.get_name_nasdaq100()

            # A for loop over all stocks and within this loop we call the method "self.historical_analysis()"
            # to extract the historical data of the current stock.
            for i in self.list_Names_for_URl:
                # Here the list "self.ListSetting_index" is made empty so that we don't have an old page
                # numbers in the next for loop.
                self.List_estimate_index.clear()
                # call the method "historical_analysis_for_one_stock()".
                self.historical_analysis_for_one_stock(i)

        # Here the exception are thrown.
        except Exception as e:
            print('No Historical data is found!', f'<{e}>')
    # --------------------------------------------------------------------------------------------------------------
