import pandas as pd

for i in range(2008, 2023):
    df = pd.read_csv(f"..\\data\\points table\\data{i}.csv")
    rows_adder = ''
    for j in range(len(df)):
        rows_adder += f'''
                <tr class="active-row">
                    <td>
                        <img src={df.iloc[j]['LOGO']} width="20" height="20" align="center">
                        <a href="..\\match table pages\\matches {i}\\{df.iloc[j]['TEAMS']} {i}.html" 
                           style='text-decoration: none;' target="_self"> {df.iloc[j]['TEAMS']}</a></td>
                        <td>{df.iloc[j]['M']}</td>
                        <td>{df.iloc[j]['W']}</td>
                        <td>{df.iloc[j]['L']}</td>
                        <td>{df.iloc[j]['PT']}</td>
                        <td>{df.iloc[j]['NRR']}</td>
                    </tr>'''

    table_html = f'''
    <html>
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=1366">
            <title>Points Table {i}</title>''' + '''
            <style>
                body{
                    background-image: url('batsman.png');
                    background-size: 100%;
                }
                .styled-table {
                    border-collapse: collapse;
                    margin: 25px 0;
                    font-size: 0.9em;
                    font-family: sans-serif;
                    border-radius: 15px 15px 15px 15px;
                    overflow: hidden;
                    box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
                    width: 720px;
                    height: 500;
                    margin-left: auto;
                    margin-right: auto;
                    margin-top: 0px;
                }

                .styled-table thead tr {
                    background-color: #183889;
                    color: #ffffff;
                    text-align: left;
                }

                .styled-table th,
                .styled-table td {
                    padding: 12px 15px;
                }

                .styled-table tbody tr {
                    border-bottom: 1px solid #dddddd;
                    text-align: left;
                }

                .styled-table tbody tr {
                    background-color: #f3f3f3;
                }

                .styled-table tbody tr:last-of-type {
                    border-bottom: 2px solid #183889;
                }

                .styled-table tbody tr.active-row:hover {
                    background-color: #dfe6ec;
                }
            </style>
        </head>
        <body>
            <h1 align="center" style="color: #183889;">Points Table!</h1>
            <table class="styled-table">
                <thead>
                    <tr>
                        <th>TEAMS</th>
                        <th>M</th>
                        <th>W</th>
                        <th>L</th>
                        <th>PT</th>
                        <th>NRR</th>
                    </tr>
                </thead>
                <tbody>''' + rows_adder + '''

                </tbody>
            </table>
        </body>
    </html>'''

    with open(f'..\\points table pages\\Points Table{i}.html', 'w') as file:
        file.write(table_html)
