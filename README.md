pyplacemaker
============

**Update 03. February 2013**: Yahoo [announced](http://developer.yahoo.com/blogs/ydn/posts/2012/09/introducing-boss-geo-–-the-next-chapter-for-boss/) they depreciate Placemaker (it was supposed to happen on 17. November 2012) and change service to BOSS Geo. It is no longer free to use. However, Placemaker continues to work.


Python wrapper for the [Yahoo Placemaker API](http://developer.yahoo.com/geo/placemaker/), based on [python-placemaker](https://github.com/bycoffe/python-placemaker) by [bycoffe](https://github.com/bycoffe).

# Usage

	>>> p = placemaker(YOUR_API_KEY)
	>>> p.find_places('Rainbow over Lower Mackenzie Falls, Grampians National Park, Victoria, Australia ')
	<Placemaker Place: 'Grampians National Park, Victoria, AU'>
	
	>>> p.places
	<Placemaker Place: 'Grampians National Park, Victoria, AU'>
	
	>>> p.administrative_scope
	Victoria, AU
	
	>>> p.geographic_scope
	Grampians National Park, Victoria, AU
	
	>>> for place in p.places:
        	print place.latitude, place.longitude, place.type
    -37.2537 142.432 LandFeature

Many places:

	>>> p.find_places('I used to live in New York, London. Now I live in Sydney')
	<Placemaker Place: 'Sydney, New South Wales, AU'>, 
	<Placemaker Place: 'London, England, GB'>, <Placemaker Place: 'New York, NY, US'>
	
	>>> p.administrative_scope
	<empty string>
	
	>>> p.geographic_scope
	Earth
	
	>>> for place in p.places:
        	print place.latitude, place.longitude, place.type
	-33.8696 151.207 Town
	51.5063 -0.12714 Town
	40.7146 -74.0071 Town
	
Notice the `administrative_scope` is empty, because there is no administrative "container" for New York, London and Sydney.
`geographic_scope` in this case is also quite irrelevant.
