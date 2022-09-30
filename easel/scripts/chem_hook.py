from bs4 import BeautifulSoup as bs
from dataclasses import dataclass
NBSP = u'\xa0'

def siblings_until_nbsp(soup):
    sibs = soup.find_next_siblings()
    desired_sibs = []
    for sib in sibs:
        if sib.text == NBSP:
            break  
        else:
            desired_sibs.append(sib)
    return desired_sibs

tags_to_text = lambda x: list(map(lambda y: y.text, x))


def parse_week_soup(week_soup):
    week_dict = {}
    learning_objectives_list = week_soup.ul
    if not learning_objectives_list:
        return [tag.name for tag in week_soup.find_all(True)]

    learning_objective_tags = list(map(lambda x: x.text, week_soup.ul.find_all('li')))
    week_dict['learning_objectives'] = learning_objective_tags

    assessments_tags = siblings_until_nbsp(week_soup.find('p', text='Assessment:'))
    week_dict['Assessment'] = list(map(lambda x: x.text, assessments_tags))
    
    weekly_reading_tags = siblings_until_nbsp(week_soup.find("p", text="Weekly Reading:"))
    week_dict['Reading'] = tags_to_text(weekly_reading_tags)

    suggested_problems_tags = siblings_until_nbsp(week_soup.find("p", text="Suggested Homework Problems:"))
    week_dict["Suggested Problems"] = tags_to_text(suggested_problems_tags)

    match_labs = lambda tag: tag.name == 'p' and tag.text.strip().startswith('Lab')
    lab_tags = siblings_until_nbsp(week_soup.find(match_labs))
    week_dict['Lab'] = tags_to_text(lab_tags)

    return week_dict

def hook(app):
    chem_id = 86059
    modules = app.api.get_modules(chem_id)
    week_module_id = 304058
    week_module = list(filter(lambda x: x['id'] == week_module_id, modules))[0]
    weeks_no_body = app.api.api_request(week_module['items_url']).json()
    page_links = list(map(lambda x: x['url'], weeks_no_body))
    weeks_with_bodies = app.api.request_many(page_links)
    week_bodies = list(map(lambda x: x['body'], weeks_with_bodies))
    weeks_soups = list(map(lambda x: bs(x, 'html.parser'), week_bodies))
    weeks = list(map(parse_week_soup, weeks_soups))
    return weeks
