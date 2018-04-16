from pygal.maps.world import COUNTRIES

'''
	Return the Pygal 2-digit country code for the 
	given country.
'''
associations = {
	"Congo, Dem. Rep.":'cd',
	"Congo, Rep.":'cg',
	"Egypt, Arab Rep.":'eg',
	"Gambia, The":'gm',
	"Hong Kong SAR, China":'hk',
	"Iran, Islamic Rep.":'ir',
	"Korea, Dem. Rep.":'kp',
	"Korea, Rep.":'kr',
	"Lao PDR":'la',
	"Macao SAR, China":'mo',
	"Macedonia, FYR":'mk',
	"Tanzania":'tz',
	"Venezuela, RB":'ve',
	"Yemen, Rep.":'ye',
	"Vietnam":'vn'
}

def init_flipped_COUNTRIES():
	return {value:key for key, value in COUNTRIES.items()}

def get_country_code(country_name):
	flipped_COUNTRIES = init_flipped_COUNTRIES()
	if country_name in flipped_COUNTRIES.keys():
		return flipped_COUNTRIES[country_name]
	elif country_name in associations.keys():
		return associations[country_name]
	else:
		return None