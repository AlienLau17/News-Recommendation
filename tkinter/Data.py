import csv

def load(fn):
    result = []
    cols = None
    with open(fn, "r") as infile:
        rdr = csv.DictReader(infile)
        for r in rdr:
            result.append(r)

    return result

business = load('./Data/business.csv')
health = load('./Data/health.csv')
general = load('./Data/general.csv')
science = load('./Data/science.csv')
sport = load('./Data/sport.csv')
technology = load('./Data/technology.csv')
entertainment = load('./Data/entertainment.csv')

news = {}
news['business'] = business
news['health'] = health
news['general'] = general
news['science'] = science
news['sport'] = sport
news['technology'] = technology
news['entertainment'] = entertainment




