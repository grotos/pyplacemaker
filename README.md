pyplacemaker
============

Python wrapper for the Yahoo Placemaker API, based on [python-placemaker](https://github.com/bycoffe/python-placemaker) by [bycoffe](https://github.com/bycoffe).

# Usage

	p = placemaker(YOUR_API_KEY)
	p.find_places('Rainbow over Lower Mackenzie Falls, Grampians National Park, Victoria, Australia ')
	<Placemaker Place: 'Grampians National Park, Victoria, AU'>
	
	p.places
	<Placemaker Place: 'Grampians National Park, Victoria, AU'>
	
	p.administrative_scope
	Victoria, AU
	
	p.geographic_scope
	Grampians National Park, Victoria, AU
	
	for place in p.places:
        print place.latitude, place.longitude, place.type
    -37.2537 142.432 LandFeature

Many places:
	p.find_places('I used to live in New York, London. Now I live in Sydney')
	<Placemaker Place: 'Sydney, New South Wales, AU'>, <Placemaker Place: 'London, England, GB'>, <Placemaker Place: 'New York, NY, US'>
	
	p.administrative_scope
	<empty string>
	
	p.geographic_scope
	Earth
	
	for place in p.places:
        print place.latitude, place.longitude, place.type
	-33.8696 151.207 Town
	51.5063 -0.12714 Town
	40.7146 -74.0071 Town
	
Notice an administrative_scope is empty, because there is no administrative "container" for New York, London and Sydney.
geographic_scope is also quite irrelevant.
