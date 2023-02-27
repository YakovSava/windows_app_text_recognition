# https://ru.wikipedia.org/wiki/Коды_языков#ISO_639
import requests

from bs4 import BeautifulSoup as bs 

def _save_file(listed:list) -> None:
	with open('iso.txt', 'w', encoding='utf-8') as file:
		file.write(f'{listed}')

def _get_page() -> bs:
	response = requests.get('https://ru.wikipedia.org/wiki/Коды_языков#ISO_639')
	return bs(response.text, 'html.parser')

def _parse_page():
	page = _get_page()
	# print(page, end='\n\n\n')
	table:bs = page.find('table', class_='standard sortable')
	# print(table, end='\n\n\n')
	tr:list[bs] = table.find_all('tr')
	# print(tr, end='\n\n\n')
	td:list[bs] = list(map(
			lambda x: x.find_all('td'),
			tr
		)
	)[1:]
	return list(
		map(
			lambda x: x[3].text,
			td
		)
	)

def main():
	_save_file(_parse_page())

if __name__ == '__main__':
	main()