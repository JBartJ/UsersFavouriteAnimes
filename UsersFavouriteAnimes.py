import requests
import json
import webbrowser
from collections import defaultdict


def getJsonContentFromResponse(response):

    try:
        content = response.json()

    except json.decoder.JSONDecodeError:
        print("Niepoprawny format")

    else:
        return content

def getRandomAnime():

    r = requests.get("https://api.jikan.moe/v4/random/anime")

    return getJsonContentFromResponse(r)['data']

def randomAnimeOperations(randomAnime):
    print("You drew an anime:",randomAnime['title'])
    print("The english title of this anime is:", randomAnime['title_english'])
    print("The japanese tile of this anime is:", randomAnime['title_japanese'],"\n")
    addAnimeToFavourites = input("Do you want to add this anime to your favourites? (Y/N): ")
    if(addAnimeToFavourites.upper() == "Y"):
            userFavouriteAnimes[username].append(randomAnime['title'])
    showMyAnimeListPage = input("Do you want to see this anime on myanimelist.net? (Y/N): ")
    if(showMyAnimeListPage.upper() == "Y"):
            webbrowser.open_new_tab(randomAnime['url'])
    


stop = False
newUser = True
userFavouriteAnimes = defaultdict(list)

while(stop == False):
    
    if(newUser == True):
        username = input("Enter your name: ")
        print("\nHello! ",username)
        
    newUser = False
    choice = int(input('''What do you want to do?

1 - Show me my favourite animes
2 - Get random anime (you can add this anime to your favourites and check it on myanimelist.net)
3 - Delete anime from my favourites
4 - Change the user
5 - Stop

Enter-->'''))

    print()
    if(choice == 1):              
        print("Your favourite animes are: ", userFavouriteAnimes[username],"\n")
                        
    elif(choice == 2):
        randomAnime = getRandomAnime()
        randomAnimeOperations(randomAnime)
        
            
    elif(choice == 3):
            animeToDelete = input("Enter the title of anime that you want to delete: ")
            if(animeToDelete in userFavouriteAnimes[username]):
                userFavouriteAnimes[username].remove(animeToDelete)
                print("You have successfully deleted anime ", animeToDelete, "from your favourites\n")
            else:
                print("There is no such anime in your favourites!\n")

    elif(choice == 4):
        newUser = True

    elif(choice == 5):
        break

    else:
        print("Choose the right number!")
             
        

    
        
