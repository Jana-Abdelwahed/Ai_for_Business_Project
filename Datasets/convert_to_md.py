import json
import os
import pandas as pd


def convert_datasets_to_markdown():
  datasets_dir = '../Datasets' if os.path.exists('../Datasets') else './Datasets'

  csv_path = os.path.join(datasets_dir, 'funding_sources_egypt.csv')
  json_path = os.path.join(datasets_dir, 'egyptian_business_laws.json')

  # 1. Convert CSV Funding Sources to Markdown
  if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    md_output = '# Egyptian Funding Sources & Venture Capitals Directory\n\n'
    md_output += (
        'This document lists active venture capital firms, seed funds, and'
        ' government grants in Egypt.\n\n'
    )
    md_output += '| Name | Type | Focus Sector | Funding Stage | Ticket Size (USD) | Key Incentives & Services | Website |\n'
    md_output += '| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n'

    for _, row in df.iterrows():
      md_output += (
          f"| **{row['Name']}** | {row['Type']} | {row['Focus_Sector']} |"
          f" {row['Funding_Stage']} | {row['Ticket_Size_USD']} |"
          f" {row['Key_Incentives_Services']} | [{row['Website']}]({row['Website']})"
          ' |\n'
      )

    csv_output_path = os.path.join(
        datasets_dir, 'funding_sources_egypt_converted.md'
    )
    with open(csv_output_path, 'w', encoding='utf-8') as f:
      f.write(md_output)
    print(f'Successfully converted CSV to: {csv_output_path}')
  else:
    print(f'File not found: {csv_path}')

  # 2. Convert JSON Legal Data to Markdown
  if os.path.exists(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
      laws = json.load(f)

    md_output = '# Egyptian Business Laws & Regulations\n\n'
    md_output += (
      
        'Structured legal texts covering Egyptian commercial, investment, and'
        ' MSME laws.\n\n'
    )

    for item in laws:
      md_output += f"## {item['law_title']} - {item['article']}\n\n"
      md_output += f"- **Category:** {item['category']}\n"
      md_output += f"- **Source Reference:** [{item['source_url']}]({item['source_url']})\n\n"
      md_output += f"### English Summary\n{item['content_en']}\n\n"
      md_output += f"### Arabic Summary (الملخص العربي)\n{item['content_ar']}\n\n"
      md_output += '---\n\n'

    json_output_path = os.path.join(
        datasets_dir, 'egyptian_business_laws_converted.md'
    )
    with open(json_output_path, 'w', encoding='utf-8') as f:
      f.write(md_output)
    print(f'Successfully converted JSON to: {json_output_path}')
  else:
    print(f'File not found: {json_path}')


if __name__ == '__main__':
  convert_datasets_to_markdown()