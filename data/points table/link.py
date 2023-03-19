import pandas as pd

lin = {'MUMBAI INDIANS': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/344000/344062.png',
       'RISING PUNE SUPERGIANT': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/313500/313524.logo.png',
       'DECCAN CHARGERS': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/321600/321684.jpg',
       'SUNRISERS HYDERABAD': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/313400/313480.logo.png',
       'KOLKATA KNIGHT RIDERS': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/313400/313419.logo.png',
       'DELHI DAREDEVILS': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/313400/313422.logo.png',
       'PUNJAB KINGS': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/317000/317003.png',
       'LUCKNOW SUPER GIANTS': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/333800/333885.png',
       'GUJARAT LIONS': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/313500/313525.logo.png',
       'CHENNAI SUPER KINGS': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/313400/313421.logo.png',
       'PUNE WARRIORS': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/156200/156230.png',
       'DELHI CAPITALS': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/313400/313422.logo.png',
       'KINGS XI PUNJAB': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/317000/317003.png',
       'KOCHI TUSKERS KERALA': 'https://upload.wikimedia.org/wikipedia/en/9/96/Kochi_Tuskers_Kerala_Logo.svg',
       'ROYAL CHALLENGERS BANGALORE': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/313400/313418.logo.png',
       'RAJASTHAN ROYALS': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/313400/313423.logo.png',
       'RISING PUNE SUPERGIANTS': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/313500/313524.logo.png',
       'GUJARAT TITANS': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_80/lsci/db/PICTURES/CMS/334700/334707.png'}

for x in range(2008, 2023):
    bf = pd.read_csv(f"data{x}.csv")
    for i in lin:
        bf.loc[bf['TEAMS'] == i, 'LOGO'] = lin[i]

    bf.to_csv(f"data{x}.csv", index=False)
