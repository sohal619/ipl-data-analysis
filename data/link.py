import pandas as pd
import os

teams_logo = {
    'Super Giants': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/333800/333885.png',
    'Royals': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/313400/313423.logo.png',
    'Titans': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/334700/334707.png',
    'Supergiants': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/333800/333885.png',
    'Supergiant': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/333800/333885.png',
    'Guj Lions': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/313500/313525.logo.png',
    'Warriors': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/156200/156230.png',
    'Mumbai': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/344000/344062.png',
    'Kings XI': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/317000/317003.png',
    'Super Kings': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/313400/313421.logo.png',
    'Capitals': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/313400/313422.logo.png',
    'Sunrisers': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/313400/313480.logo.png',
    'Chargers': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/321600/321684.jpg',
    'RCB': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/313400/313418.logo.png',
    'Daredevils': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/313400/313422.logo.png',
    'Punjab Kings': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/317000/317003.png',
    'KKR': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/313400/313419.logo.png',
    'Kochi': 'https://upload.wikimedia.org/wikipedia/en/9/96/Kochi_Tuskers_Kerala_Logo.svg'}

for i in range(2008, 2023):
    address = os.listdir(f'match data {i}')
    for x in address:
        df = pd.read_csv(f'match data {i}\\{x}')
        for j in teams_logo:
            df.loc[df['team'].str.contains(j), 'team_logo'] = teams_logo[j]
            df.loc[df['oppnent_team'].str.contains(j), 'opponent_team_logo'] = teams_logo[j]

        df.to_csv(f'match data {i}\\{x}', index=False)
