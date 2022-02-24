GMAPS = 'https://www.google.com/maps/search/near+by+'
def get_prior_n_links(category):
    priority = "LOW"
    maps = " "
    if category.replace('_', ' ').title() == "Aid Related":
        priority = 'LOW'
        maps = GMAPS+category
    elif (category.replace('_', ' ').title() == "Direct Report"):
        priority = 'MODERATE'
        maps = GMAPS+category
    elif (category.replace('_', ' ').title() == "Medical Help"):
        priority = 'MODERATE'
        maps = GMAPS+category
    elif (category.replace('_', ' ').title() == "Medical Products"):
        priority = 'MODERATE'
        maps = GMAPS+category
    elif (category.replace('_', ' ').title() == "Search And Rescue"):
        priority = 'HIGH'
        maps = GMAPS+category
    elif (category.replace('_', ' ').title() == "Security"):
        priority = 'HIGH'
        maps = GMAPS+category
    elif (category.replace('_', ' ').title() == "Military"):
        priority = 'HIGH'
        maps = GMAPS+category
    elif (category.replace('_', ' ').title() == "Child Alone"):  
        priority = 'MODERATE'
        maps = GMAPS+category  
    elif (category.replace('_', ' ').title() == "Water"):
        priority = 'LOW'
        maps = GMAPS+category
    elif (category.replace('_', ' ').title() == "Food"):
        priority = 'LOW'
        maps = GMAPS+category    
    elif (category.replace('_', ' ').title() == "Shelter" ):
        priority = 'LOW'
        maps = GMAPS+category  
    elif (category.replace('_', ' ').title() == "Clothing"):
        priority = 'LOW'
        maps = GMAPS+category 
    elif (category.replace('_', ' ').title() == "Money"):
        priority = 'LOW'
        maps = GMAPS+category 
    elif (category.replace('_', ' ').title() == "Missing People"):
        priority = 'MODERATE'
        maps = GMAPS+category 
    elif (category.replace('_', ' ').title() == "Refugees"):
        priority = 'MODERATE'
        maps = GMAPS+category
    elif (category.replace('_', ' ').title() == "Death"):
        priority = 'HIGH'
        maps = GMAPS+category 
    elif (category.replace('_', ' ').title() == "Other Aid"):
        priority = 'LOW'
        maps = GMAPS+category 
    elif (category.replace('_', ' ').title() == "Infrastructure Related"):
        priority = 'MODERATE'
        maps = GMAPS+category 
    elif (category.replace('_', ' ').title() == "Transport"):
        priority = 'LOW'
        maps = GMAPS+category 
    elif (category.replace('_', ' ').title() == "Building"):
        priority = 'LOW'
        maps = GMAPS+category 

    elif (category.replace('_', ' ').title() == "Electricity"):
        priority = 'LOW'
        maps = GMAPS+category 

    elif (category.replace('_', ' ').title() == "Tools"):
        priority = 'LOW'
        maps = GMAPS+category 

    elif (category.replace('_', ' ').title() == "Shops"):
        priority = 'LOW'
        maps = GMAPS+category 

    elif (category.replace('_', ' ').title() == "Aid Centers"):
        priority = 'LOW'
        maps = GMAPS+category 

    elif (category.replace('_', ' ').title() == "Hospitals"):
        priority = 'HIGH'
        maps = GMAPS+category 
    elif (category.replace('_', ' ').title() == "Weather Related"):
        priority = 'MODERATE'
        maps = GMAPS+category 
    elif (category.replace('_', ' ').title() == "Transport"):
        priority = 'LOW'
        maps = GMAPS+category 

    elif (category.replace('_', ' ').title() == "Food"):
        priority = 'LOW'
        maps = GMAPS+category 

    elif (category.replace('_', ' ').title() == "Floods"):
        priority = 'HIGH'
        maps = GMAPS+category 
    elif (category.replace('_', ' ').title() == "Storm"):
        priority = 'HIGH'
        maps = GMAPS+category 
    elif (category.replace('_', ' ').title() == "Fire"):
        priority = 'HIGH'
        maps = GMAPS+category 
    elif (category.replace('_', ' ').title() == "Earthquake"):
        priority = 'HIGH'
        maps = GMAPS+category 

    elif (category.replace('_', ' ').title() == "Cold"):
        priority = 'HIGH'
        maps = GMAPS+category

    elif (category.replace('_', ' ').title() == "Genre"):
        priority = 'LOW'
        maps = GMAPS+'help' 
    
    elif (category.replace('_', ' ').title() == "Offer"):
        priority = 'LOW'
        maps = GMAPS+'services' 
    elif (category.replace('_', ' ').title() == "Other Infrastructure"):
        priority = 'LOW'
        maps = GMAPS+category 

    return priority,maps