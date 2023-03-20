import pandas as pd
import os

for i in range(2008, 2023):
    file_name = os.listdir(f'..\\data\\match data {i}')
    for j in file_name:
        df = pd.read_csv(f'..\\data\\match data {i}\\{j}')
        rows_adder = ''
        for k in range(0, len(df), 2):
            rows_adder += f'''
            <tr>
                <td>
                    IPL· T20 {df.iloc[k]['match']}  &nbsp &nbsp &nbsp &nbsp &nbsp {df.iloc[k]['date']}
                    <p style="margin-bottom:0px">
                        <img src={df.iloc[k]['team_logo']} width="24" height="24" align="center">
                        {df.iloc[k]['team']}
                    </p>
                    <p style="margin-top:5px">
                        <img src={df.iloc[k]['opponent_team_logo']} width="24" height="24" align="center">
                        {df.iloc[k]['opponent_team']}
                    </p>
                    <p align="right" style="margin-bottom:5px">
                        <a href={df.iloc[k]['scorecard']} style="text-decoration: none; color: #18388b">Scorecard</a>
                    </p>
                  </td>'''

            if k == len(df)-1:
                break

            rows_adder += f''' 
                <td>
                    IPL· T20 {df.iloc[k + 1]['match']} &nbsp &nbsp &nbsp &nbsp &nbsp {df.iloc[k + 1]['date']}
                    <p style="margin-bottom:0px">
                        <img src={df.iloc[k+1]['team_logo']} width="24" height="24" align="center">
                        {df.iloc[k + 1]['team']}
                    </p>
                    <p style="margin-top:5px">
                        <img src={df.iloc[k+1]['opponent_team_logo']} width="24" height="24" align="center">
                        {df.loc[k + 1]['opponent_team']}
                    </p>
                    <p align="right" style="margin-bottom:5px">
                        <a href={df.iloc[k + 1]['scorecard']} style="text-decoration: none; color: #18388b">Scorecard</a>
                    </p>
                </td>
            </tr>'''
                
        table_html = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
             <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=1366">

            <title>{j.replace(f' {i}.csv', '')}</title>''' + '''
            <style>
                table{
                border-collapse:collapse;
                }
                td{
               padding-left:15px;
               padding-right:15px;
               padding-top:10px;
               }
               body{
                    background-image: url('../batsman.png');
                    background-size: 100%;
                    background-attachment: fixed;
                }
            </style>
        </head>
        <body>
         <table border="solid 1px" align="center">''' + rows_adder + '''

        </table>
        </body>
        </html>'''

        with open(file=f'..\\match table pages\\matches {i}\\{j.replace(f".csv", "")}.html', mode='w',
                  encoding='UTF-8') as file:
            file.write(table_html)
