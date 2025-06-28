# * The topic:  Invest according to analysis ratings

- Idea by:
  - >  Prof. Dr. Johann Schaible.     
                                                    
- Implementation by:
  - > Yosef Abu Shanab.
    
- University:
  - > Technical University of Cologne.


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# * Contents:
    
1. Introduction.
2. Expert-Analysis.
3. Installation.
4. Code development process.
5. Discussion.
6. Conclusion.
7. Sources.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 1. Introduction:


1. In which sector is our project located?
   - > In our project, we are focused on the financial sector. We collect historical expert ratings for Nasdaq 100 stocks and use these ratings to calculate a consensus rating for each stock. Based on these 
       consensus ratings, we evaluate the Nasdaq 100 index to determine which stocks to buy, hold, or sell.
   

2. what is the problem in this sector?
   - > The problem in this sector is that there is no clear overview of expert ratings for all Nasdaq-100 stocks. Only the number of experts recommending a stock as a buy, hold, or sell is separately listed on the finanzen.net website for each stock. However, the consensus rating, which is an important decision-making factor, is not calculated and displayed. Additionally, past (historical) expert ratings are not taken into account to make informed decisions about whether to buy, sell, or hold a stock.

3. What is our goal in this project?
   
   - > Our goal in this project is to gather expert ratings for the 100 Nasdaq stocks from the website Finanzen.net. Based on this data, we calculate the consensus rating for each stock and store this 
       information in a CSV file. This will provide investors with a clear overview of all Nasdaq-100 stocks in the form of a concise table.

     > To facilitate well-informed investment decisions in specific stocks, we collect this data over a certain period to track changes in expert ratings. Subsequently, we perform various statistical operations 
       on the collected data, such as creating a box plot for each stock to observe the maximum and minimum values of the consensus rating that each stock has attained.

     > This visual representation will help us evaluate the stocks better and analyze their performance.
  
4. Which strategies have we followed to achieve our goal?
   
   - > To achieve our goal, we first extracted the expert ratings for the stocks included in the Nasdaq 100 from the website Finanzen.net and saved them in a CSV file. Next, we calculated the consensus rating 
       for each stock and stored it in the CSV file. We continued to extract the expert ratings over various time periods and calculated the consensus ratings for these stocks for those periods to observe 
       changes in the expert ratings.

     > Finally, we developed a set of methods to identify stocks with the best and worst performance. Throughout this process, we also conducted statistical operations on the collected data to gain relevant 
       insights.


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2. Expert-Analysis:

- What is Expert Analysis?
  - > "Expert: a person with a high level of knowledge or skill relating to a particular subject or activity."
      "Analysis: the act of studying or examining something in detail, in order to discover or understand more about it."

    >  "The expert review, also called expert analysis, heuristic review or heuristic evaluation. It is an expert-based research method. Is the detailed investigation and evaluation of a specific topic or 
       problem by a professional/professionals or an expert/experts in the field. Various data, information and facts are taken into account for the analysis in order to make precise assessments or 
       recommendations.In our project we will consider the expert analysis for the NASDAQ-100 stocks." [['1']](https://dictionary.cambridge.org/de/worterbuch/englisch/expert)
      [['2']](https://dictionary.cambridge.org/de/worterbuch/englisch/analysis)
      [['3']](https://www.usability.de/en/usability-user-experience/glossary/expert-review.html#:~:text=The%20expert%20review%2C%20also%20called,majority%20of%20its%20usability%20problems.)
      [['4']](https://help.metricinsights.com/m/Adding_Context_to_Metrics/l/321040-what-is-expert-analysis)
      

- Why is it Useful?
  - > "Expert analysis has many advantages that help people to make decisions in many fields, as experts are generally more efficient and have sufficient knowledge, experience and skills to help people to make the right decisions often, as experts generally have several data and facts that help them to draw the right conclusions. For example, our project is about considering experts' recommendations on whether we need to buy, sell or hold a particular stock." [['5']](https://60secondmarketer.com/2020/10/20/9-reasons-its-important-to-work-with-experts/)


- Where to get Expert Analysis?
  - > "There are many websites that provide specialized analysis in different areas and one of those websites is Finanzen.net which provides a lot of analysis on stocks for larger companies for example NASDAQ 100 and such analysis includes for example the information we share in our project have taken into account. For example, the number of analysts who recommend or support buying, selling, or holding a particular stock."[['6']](https://www.finanzen.net/analysen)


- How to interpret Expert Analysis?
  - > "interpret: to understanding/decide what the intended meaning of something is."

    > Interpretation builds on analysis and aims to give meaning to the findings and place them in a larger context. While analysis answers the question of how the experts arrived at these findings, 
      interpretation focuses on why the experts arrived at this analysis. This is to understand the data and facts used that were included in the analysis."[['7']](https://dictionary.cambridge.org/de/worterbuch/englisch/interpret)[['8']](https://www.youtube.com/watch?v=V4wvPcOK6QU)

- What is consensus rating?
  - > "Consensus rating: Current average rating of all analysts who have updated during the last 12 months." [['10']](https://www.boerse-online.de/nachrichten/aktien/die-10-dax-favoriten-der-analysten-mit-kaufempfehlung-von-boerse-online-20255352.html)

- How is the consensus rating created?
    - > "Stocks are ranked from best to worst. For a buy recommendation, there are 5 points. For a hold recommendation 3 points and for a sell recommendation only one point. When you add up these ratings and 
        divide by the number of ratings, you get the consensus rating. The higher this number is, the better. That is, if the consensus rating is high, most experts would recommend buying the stock, for 
        example, if the consensus rating is 5.0. If the consensus rating is low, the experts would either sell or hold the stock."" [['10']](https://www.boerse-online.de/nachrichten/aktien/die-10-dax-favoriten-der-analysten-mit-kaufempfehlung-von-boerse-online-20255352.html)

- Why is consensus rating important and useful?
    - > "The consensus rating is important and useful because the consensus rating is one of the best ways to get information about the projected earnings of a particular listed company.
In this process, the reports of all the stock analysts covering the shares of the listed company are analyzed to determine the consensus rating."[['11']](https://www.poems.com.sg/glossary/financial-terms/consensus-estimate/#:~:text=Consensus%20rating%20score%20is%20the,period%20are%20taken%20into%20consideration.)

- What is a box plot?
    - > "A boxplot is a standardized way of displaying the distribution of data based on a five number summary (“minimum”, first quartile [Q1], median, third quartile [Q3] and “maximum”). It can tell you about your outliers and what their values are. Boxplots can also tell you if your data is symmetrical, how tightly your data is grouped and if and how your data is skewed." 
for more information here is the link.[['12']](https://builtin.com/data-science/boxplot) [['39']](https://www.statistikpsychologie.de/boxplot/)


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 3. Installation:

  - In order to scrape a website, you need to install these various packages in Python. But first of all you have to run these different instructions in your 
      Command(cmd):[['21']](https://stackoverflow.com/questions/30362600/how-to-install-requests-module-in-python-3-4-instead-of-2-7) [['22']](https://stackoverflow.com/questions/19957194/install-beautiful-soup-using-pip)
     - > > pip install requests
     - > > pip install BeautifulSoup4
  
  - And then you can import these different packages/libraries into Pycharm:
     - > > import requests
     - > > from bs4 import BeautifulSoup

  - What is requests in python?
     - > > " The Python module requests is a library for sending HTTP requests ("requests") and preparing the responses received." [['23']](https://wiki.ubuntuusers.de/Python/Requests/)

  - What is BeautifulSoup in Python?
    - > > "Beautiful Soup is a Python library that makes it easy to scrape information from web pages. It sits atop an HTML or XML parser and provides Pythonic 
          idioms for iterating, searching, and modifying the parse tree."  [['24']](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#contents-and-children)

  - What is web scraping?
    - > > "Web scraping is a method of extracting data from web sites. It uses software to extract all the information available from the targeted site by 
           simulating human behavior." [['25']](https://www.educative.io/answers/what-is-beautiful-soup)


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 4. Code development process:

   - Our project is divided into three different Python files: 

   1. - > > The first Python file is called "get_soup_function.py" and contains the function "get_soup." This function takes a URL string as a parameter, sends a request to this page, and stores the content of the page in the 'src' variable using the .content attribute. Then, the content is parsed using the Beautiful Soup module with the lxml parser, which is usually faster than html.parser. The lxml parser is used to parse HTML or XML documents and understand their structure. The parsed data is stored in the 'BSoup' variable and returned using the 'return' statement.


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

   2. - > > The second Python file is called "website_scraping_class.py". In this file we have a class called "WebsiteScraping()" that contains all the methods we need to retrieve all the expert scores of the 
           NASDAQ 100 stocks and apply various statistical methods to the extracted data.
       - > Below you will find the methods we developed and the reasons why we developed them:

          1. __init__(self):

              The first method is the __init__(self) method, which is also called the constructor. The purpose of this method is to automatically create the variables declared in the method when an object of 
              this class is created. It also allows a particular method to be called automatically when an object is created. The variables that are present in this method are called constructor variables. 

          ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
          ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

          2. get_page_numbers(self,...):
             
             The second method is the "get_page_numbers" method. This method allows for the automatic extraction of the number of pages instead of manually inputting it. The method requires three parameters. 
             The first parameter is the base URL, the second parameter is the URL index, and the third parameter is the URL function. Here is an example of such a URL: 
              
             'https://www.finanzen.net/index/nasdaq_100/fundamental'
          
             The base URL would be:  'https://www.finanzen.net/', 

             The URL index would be:  'index/', 

             And the URL function would be:  'nasdaq_100/fundamental'.

             These three strings are combined into a single URL and passed to the 'get_soup' function to extract the content of that page. Subsequently, the function checks how many pages, for example, the 
             names of stocks, are divided into. By visiting this page, we can clearly see that the names are spread across two pages. The number of pages is then extracted and stored in the 
             'self.List_estimate_index' list.

             With the help of this method, for each entered website, it is checked whether there is more than one page.

             In the screenshot below, we can see an example where the names are divided into two pages


             ![Alt text](https://github.com/WanjaSchaible/expert-analysis/blob/main/project/pictures/Page%20%20Number.png)
             

          ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
          ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

          
          3. get_name_nasdaq100(self,...):

             The third method, "get_name_nasdaq100(self)", accepts a web page link as a parameter and retrieves the values stored in the list "self.List_estimate_index". This involves iterating through the 
             "self.List_estimate_index" list using a loop. During each iteration, we invoke the "get_soup" method, passing both the web page link and the current value from the loop as parameters. 
             Subsequently, the method extracts the names of the stocks from the web page and stores them in the "self.list_Names_for_URl" list.


          ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
          ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


          4. get_info_for_stock(self):

             The fourth method is the "get_info_for_stock(self)" method. This method takes the stock name as a parameter and retrieves the expert ratings from the website:

             "https://www.finanzen.net/schaetzungen/" + "stock name".

             This means that the recommendations of the experts for this stock, such as how many experts recommend buying, holding, or selling,... it, are extracted from this website and stored in the 
             "self.listOfValues" list.
             This method extracts expert ratings for a specific stock.

             For example:

             "https://www.finanzen.net/schaetzungen/activision_blizzard"


             Example of the expert ratings:

             ![Alt text](https://github.com/WanjaSchaible/expert-analysis/blob/main/project/pictures/Bewertung.png)


          ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
          ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


          5. get_info_for_all_stocks(self,...):

             The fifth method is named 'get_info_for_all_stocks(self)'. This method takes the list of stock names 'self.list_Names_for_URl' as a parameter. For each stock, it extracts expert ratings and saves 
             the values in the 'self.attribute' list (column name) and the 'self.listOfValues' list (expert ratings). Subsequently, a DataFrame is created from these lists and then saved to a CSV file with a 
             timestamp. Additionally, within this function, two new columns are added to the DataFrame: one named 'Name' to store the stock names in that column, and the other named 'Consensus Rating' to 
             calculate and store the consensus rating for each stock.
             
             The format of the CSV file is as follows:


             ![Alt text](https://github.com/WanjaSchaible/expert-analysis/blob/main/project/pictures/Stocks%20table%20without%20consensus%20rating.png)


          ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
          ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


          6. calculate_consensus_rating(self):

             The sixth method is called "calculate_consensus_rating(self)". This method is used to calculate the consensus rating for each stock. In this method, a for loop is used to iterate through all the 
             rows in the CSV file. For each stock, the consensus rating is calculated and saved in the CSV file. The calculation of the consensus rating follows the following formula:

             Consensus rating = ((Buy_Value * 5) + (Hold_Value * 3) + (Sell_Value * 1)) / (Number of Experts)

             ![Alt text](https://github.com/WanjaSchaible/expert-analysis/blob/main/project/pictures/Bewertung-1.png)

             ---------------------------------------------------------------------------------------------------------------------------------------------------------

             For example, let's consider the following:

             13 experts recommend "Buy"

             4 experts recommend "Hold"

             0 experts recommend "Sell" 

             Number of Experts = 13 + 4 + 5 = 22

             Consensus rating of Activision Blizzard = ((13 * 5) + (4 * 3) + (0 * 1)) / (22) = 3.5


             ---------------------------------------------------------------------------------------------------------------------------------------------------------

             
             The Stocks Table with consensus rating:

             ![Alt text](https://github.com/WanjaSchaible/expert-analysis/blob/main/project/pictures/Stocks%20table%20with%20consensus%20rating.png)

             

          ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
          ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


          7. sort_according_the_consensus_rating(self):

             The seventh method is called "sort_according_the_consensus_rating(self)". This method is used to sort the stocks in the CSV file in descending order. This means that stocks with higher consensus 
             ratings will be sorted at the beginning of the CSV file, while lower ratings will follow subsequently. 
             A higher consensus rating indicates a better-performing stock. 
             

             In the example below, we can see that the stocks are sorted in descending order based on their consensus ratings: 

             ![Alt text](https://github.com/WanjaSchaible/expert-analysis/blob/main/project/pictures/Table%20sorted%20by%20consensus%20rating.png)



          -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
          -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



          8. check_consensus_rating_for_one_stock(self):

             The eighth method is "check_consensus_rating_for_one_stock(self)". This method is used to enter the name of a stock and for that stock the historical consensus rating of the stock is displayed in a 
             boxplot, with the current consensus rating of the entered stock displayed as a red diamond in the boxplot. If the stock is not found, an exception is thrown that this stock does not exist.

             console input:

             ![Alt text](https://github.com/WanjaSchaible/expert-analysis/blob/main/project/pictures/Input%20Console%20.png)

             ---------------------------------------------------------------------------------------------------------------------------------------------------------

             Boxplot of the Stock: CrowdStrike

             ![Alt text](https://github.com/WanjaSchaible/expert-analysis/blob/main/project/pictures/Boxplot%201.png)

             ---------------------------------------------------------------------------------------------------------------------------------------------------------

            - Explain the boxplot:
              
              The box plot illustrates the historical consensus rating of the CrowdStrike stock. It shows the minimum and maximum consensus ratings, as well as the median, Q1, and Q3.

              The median divides the data into two halves, where 50% of the consensus rating values are smaller than or equal to the median, and 50% are greater than or equal to the median. Q1 covers the bottom 
              25% of the data, meaning that 25% of the consensus rating values are smaller than or equal to Q1. On the other hand, Q3 covers the bottom 75% of the data, so 75% of the consensus rating values are 
              smaller than or equal to Q3. [['9']](https://builtin.com/data-science/boxplot) [['36']](https://www.statistikpsychologie.de/boxplot/)

              The minimum and maximum values represent the consensus rating values that this stock achieved. These values were calculated from different consensus ratings over various time periods. This box 
              plot was created from 6 different CSV files.

              In the above box plot, we can see that the maximum value is 4.304 and the minimum value is 4.261 and so on. The red diamond in the boxplot represents the current consensus score, which is 4,261.
              The box plot shows that the current consensus rating for CrowdStrike stock is not good as it is at the minimum reading and below average as well as Q1 and Q3. In this situation, holding the stock 
              might be wise as the consensus rating could improve going forward.



          -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
          -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



          9. check_consensus_rating_for_several_stocks(self):

             The ninth method is "check_consensus_rating_for_several_stocks(self)". With this method you can check the historical consensus rating of one or more stocks and display it as a boxplot. The current 
             consensus rating is displayed as a red diamond in the boxplot.

             Examples:

             Console Input of the Stocks:

             ![Alt text](https://github.com/WanjaSchaible/expert-analysis/blob/main/project/pictures/Input%20Console%20for%20several%20stocks.png)

             ---------------------------------------------------------------------------------------------------------------------------------------------------------

             Boxplot of the both Stocks:
            
             ![Alt text](https://github.com/WanjaSchaible/expert-analysis/blob/main/project/pictures/Boxplot%201-1.png)

             ---------------------------------------------------------------------------------------------------------------------------------------------------------

             - Explain the boxplot:
              
              The box plot illustrates the historical consensus rating of the CrowdStrike stock. It shows the minimum and maximum consensus ratings, as well as the median, Q1, and Q3.

              The median divides the data into two halves, where 50% of the consensus rating values are smaller than or equal to the median, and 50% are greater than or equal to the median. Q1 covers the bottom 
              25% of the data, meaning that 25% of the consensus rating values are smaller than or equal to Q1. On the other hand, Q3 covers the bottom 75% of the data, so 75% of the consensus rating values are 
              smaller than or equal to Q3. [['9']](https://builtin.com/data-science/boxplot) [['36']](https://www.statistikpsychologie.de/boxplot/)

              The minimum and maximum values represent the consensus rating values that this stock achieved. These values were calculated from different consensus ratings over various time periods. This box 
              plot was created from 6 different CSV files.

              In the above box plot, we can see that the maximum value is 4.304 and the minimum value is 4.261 and so on. The red diamond in the boxplot represents the current consensus score, which is 4,261.
              The box plot shows that the current consensus rating for CrowdStrike stock is not good as it is at the minimum reading and below average as well as Q1 and Q3. In this situation, holding the stock 
              might be wise as the consensus rating could improve going forward.


             ---------------------------------------------------------------------------------------------------------------------------------------------------------


             ![Alt text](https://github.com/WanjaSchaible/expert-analysis/blob/main/project/pictures/Boxplot%20of%20the%20Stock%20Workday%20A.png)

             ---------------------------------------------------------------------------------------------------------------------------------------------------------

             - Explain the Boxplot:
              
              The box plot illustrates the historical consensus rating of the Workday A stock. It shows the minimum and maximum consensus ratings, as well as the median, Q1, and Q3.

              The median divides the data into two halves, where 50% of the consensus rating values are smaller than or equal to the median, and 50% are greater than or equal to the median. Q1 covers the bottom 
              25% of the data, meaning that 25% of the consensus rating values are smaller than or equal to Q1. On the other hand, Q3 covers the bottom 75% of the data, so 75% of the consensus rating values are 
              smaller than or equal to Q3. ['9'] ['36']

              The minimum and maximum values represent the consensus rating values that this stock achieved. These values were calculated from different consensus ratings over various time periods. This box 
              plot was created from 6 different CSV files.

              In the above box plot, we can see that the maximum value is 3.75 and the minimum value is 3.711 and so on. The red diamond in the boxplot represents the current consensus score, which is 3.711. 
              The box plot shows that the current consensus rating for Workday A stock is not good as it is at the minimum reading and below average as well as Q1 and Q3. In this situation, holding the stock 
              might be wise as the consensus rating could improve going forward.



         -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
         -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



         10. check_consensus_rating_compare_with_other_stocks(self):

             The tenth method, "check_consensus_rating_compare_with_other_stocks(self)", enables the display of the consensus rating of a specific stock. Here, the consensus rating of this stock is visualized 
             as a boxplot compared to the current consensus ratings of all Nasdaq 100 stocks.The red diamond stands for the consensus rating of the entered stock.

             Example:

             Console Input:

             ![Alt text](https://github.com/WanjaSchaible/expert-analysis/blob/main/project/pictures/Input%20Console%20check%20compare%20with%20other%20stocks.png)

            
             ---------------------------------------------------------------------------------------------------------------------------------------------------------


             Boxplot of the Stock: CrowdStrike:

             ![Alt text](https://github.com/WanjaSchaible/expert-analysis/blob/main/project/pictures/Boxplot%20of%20the%20CheckStock_ConsensusRating3%20Method.png)

             ---------------------------------------------------------------------------------------------------------------------------------------------------------

            - Explain the Boxplot:
              
              The box plot illustrates the consensus rating of CrowdStrike stock compared to all the consensus ratings of Nasdaq-100 stocks.

              In the following box plot, it is evident that the consensus rating for CrowdStrike stock is above the median and the third quartile (Q3). This indicates that the stock currently has a very 
              favorable consensus rating compared to the Nasdaq-100 stocks, as the maximum consensus rating is 4.536, while CrowdStrike's consensus rating stands at 4.261. Therefore, it is recommended to 
              consider buying this stock.


         --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
         --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



         11. classify_stocks_by_consensus_rating(self):

             The eleventh method is the "classify_stocks_by_consensus_rating(self)" method. This method can be used to display either the stocks with the best or the stocks with the worst consensus rating for a 
             given date. If the date is entered incorrectly or no dates are available for that date, an exception is thrown stating that the date is not available and the available dates are displayed to 
             provide the option to enter a new date. Stocks with a consensus rating above the average of all consensus ratings are considered good stocks, while stocks with a consensus rating below the average 
             are considered less good or not good stocks.

             The average of the consensus rating of all stocks:

             ![Alt text](https://github.com/WanjaSchaible/expert-analysis/blob/main/project/pictures/The%20average%20of%20the%20consensus%20rating%20of%20all%20stocks.png)

             ---------------------------------------------------------------------------------------------------------------------------------------------------------             

             Good Stocks:

             ![Alt text](https://github.com/WanjaSchaible/expert-analysis/blob/main/project/pictures/The%20Best%20Stocks.png)

             ---------------------------------------------------------------------------------------------------------------------------------------------------------

             - Explain the scrennshot:

             In the figure above, we can see that the 'good stocks' for a specific date are displayed in descending order. This means that stocks with the highest consensus rating are shown first, followed by 
             the next best, and so on. This can help investors identify which stocks have been rated as less good or good stocks for a given date.

             ---------------------------------------------------------------------------------------------------------------------------------------------------------

             Not Good Stocks:

             ![Alt text](https://github.com/WanjaSchaible/expert-analysis/blob/main/project/pictures/Not%20Good%20Stocks.png)


             ---------------------------------------------------------------------------------------------------------------------------------------------------------

             - Explain the scrennshot:

             In the figure above, it can be seen that the "not good stocks" for a given date are displayed in descending order. This means that the stocks with the highest consensus rating are shown first, 
             followed by the next worst, and so on. This can help investors identify which stocks have been rated as less good or good stocks for a given date.

             ---------------------------------------------------------------------------------------------------------------------------------------------------------

             - If the entered date is not available:

             If the entered date is not available, an error message will be displayed and the possibility to enter a new date will be given again, and as a help a list of available dates will be displayed, as 
             shown in the following example.

             ![Alt text](https://github.com/WanjaSchaible/expert-analysis/blob/main/project/pictures/not%20available%20Date%20.png)







      -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


      12. historical_analysis_for_one_stock(self):

          The twelfth method is the "historical_analysis_for_one_stock(self)" method. This method extracts historical expert scores for a given stock and stores them in a CSV file. The data is retrieved about 
          a specified stock and stored in the CSV file. Using this data, we can analyze the stock in detail and observe the evolution of consensus valuations for the stock.

          for Example:
 
          The historical expert evaluation at this link:

          "https://www.finanzen.net/analysen/tesla-analysen"

          
          ---------------------------------------------------------------------------------------------------------------------------------------------------------
          
         ![Alt text](https://github.com/WanjaSchaible/expert-analysis/blob/main/project/pictures/historical%20expert%20valuation%20.png)

         ---------------------------------------------------------------------------------------------------------------------------------------------------------
           
         - Explain the scrennshot

           In the above screenshot we can see that the historical expert ratings of the stock Activision Blizzard are extracted, there we can see the date of the expert rating and what was the recommendation, 
           whether to buy, sell or hold this stock and by whom this expert rating was executed, so here is the name of the bank.


         ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
         ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

      13. historical_analysis_for_all_stocks(self):

         The thirteenth method is the "historical_analysis_for_all_stocks(self):"
         This method allows to extract and store all historical expert evaluations for all Nasdaq 100 stocks in CSV files. 

         Historical expert valuation of Activision Blizzard and Adobe Stocks:

         Activision Blizzard:

         ![Alt text](https://github.com/WanjaSchaible/expert-analysis/blob/main/project/pictures/Historical%20expert%20evaluation%20of%20the%20stock%20Activision%20Blizzard.png)

         ---------------------------------------------------------------------------------------------------------------------------------------------------------

         Adobe:

         ![Alt text](https://github.com/WanjaSchaible/expert-analysis/blob/main/project/pictures/Historische%20Expertenbewertung%20der%20Aktie%20Adobe.png)



         ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
         ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


   3. The third file is the main file, which contains an object of the class 'WebsiteScraping()' named 'nasdaq100_scraping'. This file provides various methods to the user. For example, users can utilize a 
      method to display the historical consensus rating of a stock as a box plot.

      This can be seen in the following example:

      ![Alt text](https://github.com/WanjaSchaible/expert-analysis/blob/main/project/pictures/main%20file.png)

      ---------------------------------------------------------------------------------------------------------------------------------------------------------
      
      Boxplot:

      ![Alt text](https://github.com/WanjaSchaible/expert-analysis/blob/main/project/pictures/Boxplot%20for%20main%20File.png)

      ---------------------------------------------------------------------------------------------------------------------------------------------------------

   - Explain the Boxplot:
      
      The box plot illustrates the historical consensus rating of the CrowdStrike stock. It shows the minimum and maximum consensus ratings, as well as the median, Q1, and Q3.

      The median divides the data into two halves, where 50% of the consensus rating values are smaller than or equal to the median, and 50% are greater than or equal to the median. Q1 covers the bottom 
      25% of the data, meaning that 25% of the consensus rating values are smaller than or equal to Q1. On the other hand, Q3 covers the bottom 75% of the data, so 75% of the consensus rating values are 
      smaller than or equal to Q3. [['9']](https://builtin.com/data-science/boxplot) [['36']](https://www.statistikpsychologie.de/boxplot/)

      The minimum and maximum values represent the consensus rating values that this stock achieved. These values were calculated from different consensus ratings over various time periods. This box 
      plot was created from 6 different CSV files.

      In the above box plot, we can see that the maximum value is 4.304 and the minimum value is 4.261 and so on. The red diamond in the boxplot represents the current consensus score, which is 4,261.
      The box plot shows that the current consensus rating for CrowdStrike stock is not good as it is at the minimum reading and below average as well as Q1 and Q3. In this situation, holding the stock 
      might be wise as the consensus rating could improve going forward.

      

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
       
# 5. Discussion:
  
  
  - > Now, we will discuss our results by answering the following questions:
      - Have we actually achieved our goal?      
        - > We have successfully achieved our goal by creating a clear representation of expert ratings for all Nasdaq-100 stocks and calculating the consensus rating for each stock. Investors can easily view 
            expert ratings for Nasdaq-100 stocks in a table. Additionally, we take into account the historical consensus rating of each stock to provide a reliable overview of the stock's rating development.
            To enable this, we have developed a method to create a box plot of the historical consensus rating for each stock. This allows us to precisely observe the highest and lowest consensus ratings that 
            each stock has reached and monitor the rating development of each stock. Furthermore, we can use this box plot to extract other data, such as the average consensus value and more.

          > We have also developed other methods, including one that shows the stocks with the best consensus rating in the Nasdaq 100 for a given input date. Now investors have a clear overview of all Nasdaq 
            100 stocks, and several methods are available to track Nasdaq stock performance and identify good and bad stocks for specific dates.
         
      - What limitations did we encounter in our project?
        - > We encountered several limitations in our project. Firstly, we were only able to extract expert ratings from finanzen.net, which resulted in some missing ratings for certain stocks and historical 
            data for other stocks was not available. Secondly, we couldn't ensure 100 percent accuracy of the expert analysis as we couldn't compare it with other expert ratings.

          > Additionally, another limitation was that the consensus ratings of the stocks showed very minimal changes. For example, the CrowdStrike stock had a maximum consensus rating of 4.304 and a minimum of 
            4.261, which played a significant role in the representation of the Boxplot.
       


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     
# 6. Conclusion:

We have successfully solved the problem and achieved our goal by creating a clear representation of expert ratings for all Nasdaq-100 stocks and calculating the consensus rating for each stock. Investors can easily view expert ratings for Nasdaq-100 stocks in a table. Additionally, we consider the historical consensus rating of each stock to provide a reliable overview of its rating development.

In our project, we obtained the entire expert ratings from the website "finanzen.net" using Python libraries "requests" and "BeautifulSoup." Subsequently, we extracted and saved this data as a DataFrame in a CSV file. The extracted expert ratings were related to Nasdaq-100 stocks, and for each stock, we recorded the number of experts recommending buy, sell, overweight, underweight, or hold.

Based on these values, we calculated the consensus rating for each stock and stored it in the same CSV file. Furthermore, we extracted expert ratings for different time periods and saved them in new CSV files to observe changes in expert ratings over time.

To effectively analyze these data, we have developed several statistical methods. One of these methods is to create a boxplot for the historical consensus rating of a particular stock. The boxplot displays the maximum and minimum consensus ratings for the stock, with the current consensus rating represented by a red diamond. Using this visualization, investors can quickly see if the current consensus rating has improved or worsened compared to previous ratings and quickly make the decision to buy, sell or hold that stock.

These methods provide valuable insights to investors, helping them make informed decisions on whether to buy, hold, or sell a particular stock.

Another method allows the display of good and bad stocks for a given date. Stocks whose consensus rating falls below the average consensus rating of all stocks are marked as bad stocks, while those with a consensus rating above the average are marked as good stocks. Additionally, investors can view the consensus rating of a specific stock compared to all Nasdaq-100 stocks. For this purpose, we developed a method that creates a box plot with all other Nasdaq 100 consensus ratings for a given stock name. This method helps determine whether the consensus rating of this stock is good or bad compared to all Nasdaq-100 consensus ratings.

Finally, we have developed another method to extract and store all historical expert ratings for all Nasdaq 100 stocks in CSV files, which can help to better analyze and evaluate the expert ratings of the Nasdaq 100.

With our project, investors now have the opportunity to easily download and access both current and historical expert ratings for Nasdaq-100 stocks. They can also track the historical expert ratings for Nasdaq-100 stocks and use this data to make informed decisions about buying, holding, or selling a stock. Additionally, they have access to other methods, such as viewing top-performing and underperforming stocks for a specific date.


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 7. Sources:
   - > [1]  https://dictionary.cambridge.org/de/worterbuch/englisch/expert
   - > [2]  https://dictionary.cambridge.org/de/worterbuch/englisch/analysis
   - > [3]  https://www.usability.de/en/usability-user-experience/glossary/expert-review.html#:~:text=The%20expert%20review%2C%20also%20called,majority%20of%20its%20usability%20problems.
   - > [4]  https://help.metricinsights.com/m/Adding_Context_to_Metrics/l/321040-what-is-expert-analysis
   - > [5]  https://60secondmarketer.com/2020/10/20/9-reasons-its-important-to-work-with-experts/
   - > [6]  https://www.finanzen.net/analysen 
   - > [7]  https://dictionary.cambridge.org/de/worterbuch/englisch/interpret
   - > [8]  https://www.youtube.com/watch?v=V4wvPcOK6QU  
   - > [9]  https://www.juliusbaer.com/fileadmin/legal/glossary-de.pdf
   - > [10] https://www.boerse-online.de/nachrichten/aktien/die-10-dax-favoriten-der-analysten-mit-kaufempfehlung-von-boerse-online-20255352.html
   - > [11] https://www.poems.com.sg/glossary/financial-terms/consensus-estimate/#:~:text=Consensus%20rating%20score%20is%20the,period%20are%20taken%20into%20consideration.
   - > [12] https://builtin.com/data-science/boxplot
   - > [13] https://www.finanzen.net/analysen
   - > [14] http://introtopython.org/
   - > [15] https://www.youtube.com/playlist?list=PLQ7v4xu9LfgmIoIppHHLrOdL4_HiEtaPe
   - > [16] https://www.interactivebrokers.co.uk/de/?f=15763
   - > [17] https://www.youtube.com/watch?v=ce5Ks2xAXo4
   - > [18] https://www.youtube.com/watch?v=Uu1Skwz98B4&list=PLNmsVeXQZj7o46LI06XkxAqcg4Ucm7pwn&index=17
   - > [19] https://www.boerse-online.de/nachrichten/aktien/alle-40-dax-aktien-nach-den-wichtigen-quartalszahlen-im-check-kaufen-oder-verkaufen-20316681.html 
   - > [20] https://www.w3schools.com/python/pandas/ref_df_iterrows.asp
   - > [21] https://stackoverflow.com/questions/30362600/how-to-install-requests-module-in-python-3-4-instead-of-2-7
   - > [22] https://stackoverflow.com/questions/19957194/install-beautiful-soup-using-pip
   - > [23] https://wiki.ubuntuusers.de/Python/Requests/
   - > [24] https://www.crummy.com/software/BeautifulSoup/bs4/doc/#contents-and-children         
   - > [25] https://www.educative.io/answers/what-is-beautiful-soup
   - > [26] https://www.youtube.com/watch?v=spALaS5BFX8
   - > [27] https://www.youtube.com/watch?v=kcOPiK0PiV8
   - > [28] https://www.youtube.com/watch?v=Vo-bfTqEFQk
   - > [29] https://www.youtube.com/watch?v=mclAY5gY8cM
   - > [30] https://studyflix.de/statistik/boxplot-1044
   - > [31] https://www.youtube.com/watch?v=QgmUGTrqvdk
   - > [32] https://stackoverflow.com/questions/60837734/you-dont-have-permission-to-access-this-resource-python-webscraping
   - > [33] https://www.youtube.com/watch?v=BybAetckH88
   - > [34] https://www.youtube.com/watch?v=tPx9nVvVrGE
   - > [35] https://www.youtube.com/watch?v=S0EEUmsIc6c
   - > [36] https://www.youtube.com/watch?v=Fc7pnyj-ITM&list=PLI8raxzYtfGxIjoyi5kVdYGG0r5yqQPAF&index=2
   - > [37] https://www.youtube.com/watch?v=e5awiVnkuEc
   - > [38] https://github.com/hd016/finanzen-crawler/blob/master/finanzen_fundamentals/stocks.py 
   - > [39] https://www.statistikpsychologie.de/boxplot/
    
        
   

