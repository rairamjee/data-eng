import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'https://www.haberkorn.com/at/de'
base_url='https://www.haberkorn.com'

try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')

    category_menu = soup.find(class_='category-menu row')
    
    if category_menu:
        category_menu_item = category_menu.find_all('li')
        
        for item in category_menu_item:
            main_categories = item.find(class_="h4 level-text")
            link = item.find('a', href=True)
            
            if main_categories and link:
                main_categories_Text=main_categories.get_text(strip=True)
                sub_categories_url=urljoin(base_url, link['href'])
                # print(f"{main_categories_Text} {sub_categories_url} ")

                

                ######## Sub Categories
                response_sub_categories=requests.get(sub_categories_url)
                response_sub_categories_soup=BeautifulSoup(response_sub_categories.content,'html.parser')

                sub_categories_menu =response_sub_categories_soup.find_all(class_='category-box dropdown')
                
                if(sub_categories_menu):
                       
                      for sub_categories_menu_items in sub_categories_menu:
                          print(sub_categories_menu_items)
                    # sub_categories_menu_item=sub_categories_menu.('a')
                    # print(sub_categories_menu_item)

                #     for sub_category_item in sub_categories_menu_item:
                #         sub_categories=sub_category_item.find(class_="h4 level-text")
                #         subcategories_link= sub_category_item.find('a',href=True)

                #         if sub_categories and link:
                #             sub_categories_Text=sub_categories.get_text(strip=True)
                #             sub_sub_categories_url=urljoin(base_url,link['href'])

                #             print(f"{main_categories_Text} {sub_categories_Text} ")




                            # ######## Sub Categories
                            # response_sub_sub_categories=requests.get(sub_sub_categories_url)
                            # response_sub_sub_categories_soup=BeautifulSoup(response_sub_sub_categories.content,'html.parser')

                            # sub_sub_categories_menu =response_sub_sub_categories_soup.find(class_='category-menu row')

                            # if(sub_sub_categories_menu):
                            #     sub_sub_categories_menu_item=sub_sub_categories_menu.find_all('li')
                            #     # print(sub_categories_menu_item)

                            #     for sub_sub_category_item in sub_sub_categories_menu_item:
                            #         sub_sub_categories=sub_sub_category_item.find(class_="h4 level-text")
                            #         subsubcategories_link= sub_sub_category_item.find('a',href=True)

                            #         if sub_sub_categories and link:
                            #             sub_sub_categories_Text=sub_categories.get_text(strip=True)
                            #             # sub_sub_categories_url=urljoin(base_url,link['href'])

                            #             print(f"{main_categories_Text} {sub_categories_Text} {sub_sub_categories_Text}")














            # elif main_categories:
            #     print(f"{Main_Categories.get_text(strip=True)}: No link")
            # elif link:
            #     print(f"No text: {link['href']}")
    else:
        print("Category menu not found")
        
except requests.RequestException as e:
    print(f"An error occurred: {e}")
