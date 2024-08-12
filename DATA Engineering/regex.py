import requests
import re
from urllib.parse import urljoin

url = 'https://www.haberkorn.com/at/de'
base_url='https://www.haberkorn.com'

# <li class="col-xs-12" data-id="246269">
#   <a href="/at/de/maschinenelemente" class="wrap-word" data-ga-label="Maschinenelemente" title="Maschinenelemente">
# <div class="img-wrapper">
# <img class=" ls-is-cached lazyloaded" src="/dam/50x50/0001144A.jpg" data-src="/dam/50x50/0001144A.jpg"                    alt="Maschinenelemente">
#   </div>
#   <span class="level-text">Maschinenelemente</span>
#   <span class="count">2.749</span>
#   </a>
# </li>


try:
    response = requests.get(url)
    response.raise_for_status()
    re1 = '\<span\sclass\=\"level\-text\"\>(.*?)\<'

    match = re.findall(re1, response.text)
    if match:
        print(match)

except requests.RequestException as e:
    print(f"An error occurred: {e}")
