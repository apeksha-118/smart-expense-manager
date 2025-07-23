
def auto_categorize(description):
    description = description.lower()
    categories = {
        'food': ['pizza', 'burger', 'restaurant', 'coffee'],
        'transport': ['uber', 'metro', 'bus', 'taxi'],
        'entertainment': ['movie', 'netflix', 'game'],
        'shopping': ['clothes', 'shoes', 'mall'],
        'groceries': ['milk', 'bread', 'eggs', 'supermarket']
    }

    for category, keywords in categories.items():
        if any(word in description for word in keywords):
            return category
    return 'other'
