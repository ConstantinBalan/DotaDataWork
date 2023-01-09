import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def OpenDotaEndpoint(request):
    base_url='https://api.opendota.com/api'
    api_url= base_url + request
    response = requests.get(api_url)
    raw_response = response.json()
    #json_obj = json.load(raw_response)
    #json_formatted_string = json.dumps(json_obj, indent=2)
    #print("Info below: \n" )
    #print(json_formatted_string)
    country_df = pd.DataFrame.from_records(raw_response)
    country_df = country_df.dropna(axis=0)
    print(country_df)

    game_info = country_df.iloc[:,4:6]
    game_duration = list(game_info.iloc[:,0])
    game_mmr = list(game_info.iloc[:,1])   
    print(game_info)
    print(game_duration)
    print(game_mmr)

    fig, ax = plt.subplots()
    ax.scatter(game_duration, game_mmr)
    ax.set(xticks=np.arange(500, 2200, 100), yticks=np.arange(500, 5000, 500))
    ax.set_xlabel("Game Duration (Seconds)")
    ax.set_ylabel("Average MMR")
    plt.show()

OpenDotaEndpoint('/publicmatches')


