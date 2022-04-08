# Display your every day status in Instagram


## Installation

1. Download the repository

    ```bash
    git clone https://github.com/Pasanlaksitha/Instagram-bio-followers-display.git
    ```

2. requirement.txt install  
    ```bash
    pip install -r requirements.txt
    ```

3. open main.py and enter your username password 
    ```python
    username = "USERNAME"
    password = "PASSWORD"
    ```
4. schedule for the run program (recommended: once per day) 
    - just open in your editor and run it, then you will see
      a promt wich asking your feelings today.

## Other Usage

you can convert this for following and posts count also 

- for following count 
    ```python
    #change scraping json to this
    followers = data2['graphql']['user']['edge_follow']['count']
    ```
- read JSON on Instagram https://www.instagram.com/boinkchimp/?__a=1 to do more


## License
[MIT](https://github.com/Pasanlaksitha/Instagram-bio-followers-display/blob/main/LICENSE/)