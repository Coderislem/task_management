
def get_icon_for_title(title):
    default_icon = 'fa-list-alt'
    keyword_to_icon = {
        'work': 'fa-briefcase',
        'home': 'fa-home',
        'shopping': 'fa-shopping-cart',
        'personal': 'fa-user',
        'study': 'fa-book',
        'fitness': 'fa-dumbbell',
        'travel': 'fa-plane',
        'ideas': 'fa-lightbulb',
        'project': 'fa-tasks',
        'birthday': 'fa-birthday-cake',
        'meeting': 'fa-calendar-alt',
        'appointment': 'fa-calendar-check',
        'food': 'fa-utensils',
        'exercise': 'fa-running',
        'finance': 'fa-dollar-sign',
        'money': 'fa-money-bill-alt',
        'investment': 'fa-chart-line',
        'car': 'fa-car',
        'family': 'fa-users',
        'health': 'fa-heartbeat',
        'doctor': 'fa-stethoscope',
        'music': 'fa-music',
        'video': 'fa-video',
        'photography': 'fa-camera',
        'art': 'fa-palette',
        'technology': 'fa-laptop',
        'phone': 'fa-mobile-alt',
        'email': 'fa-envelope',
        'vacation': 'fa-umbrella-beach',
        'holiday': 'fa-gift',
        'recipe': 'fa-utensils',
        'event': 'fa-calendar',
        'maintenance': 'fa-tools',
        'house': 'fa-home',
        'school': 'fa-school',
        'assignment': 'fa-file-alt',
        'lecture': 'fa-chalkboard-teacher',
        'course': 'fa-graduation-cap',
        'exam': 'fa-pencil-alt',
        'meeting': 'fa-handshake',
        'party': 'fa-glass-cheers',
        'celebration': 'fa-birthday-cake',
        'wedding': 'fa-ring',
        'relationship': 'fa-heart',
        'note': 'fa-sticky-note',
        'checklist': 'fa-check-square',
        'task': 'fa-tasks',
        'priority': 'fa-exclamation-circle',
        'contact': 'fa-address-book',
        'networking': 'fa-network-wired',
        'shopping': 'fa-shopping-bag',
        'sale': 'fa-tags',
        'gift': 'fa-gift',
        'order': 'fa-shopping-basket',
        'delivery': 'fa-truck',
        'subscription': 'fa-envelope-open-text',
        'news': 'fa-newspaper',
        'announcement': 'fa-bullhorn',
        'blog': 'fa-blog',
        'write': 'fa-pen',
        'read': 'fa-book-reader',
        'library': 'fa-book-open',
        'cleaning': 'fa-broom',
        'chores': 'fa-list',
        'errands': 'fa-running',
        'garden': 'fa-seedling',
        'plants': 'fa-leaf',
        'animals': 'fa-paw',
        'pets': 'fa-dog',
        'travel': 'fa-globe',
        'journey': 'fa-route',
        'map': 'fa-map',
        'destination': 'fa-map-marker-alt',
        'transportation': 'fa-bus',
        'plane': 'fa-plane-departure',
        'train': 'fa-subway',
        'boat': 'fa-ship',
        'bike': 'fa-bicycle',
        'walk': 'fa-walking',
        'adventure': 'fa-hiking',
        'mountains': 'fa-mountain',
        'beach': 'fa-umbrella-beach',
        'city': 'fa-city',
        'country': 'fa-flag',
        'international': 'fa-globe-americas',
        'security': 'fa-shield-alt',
        'privacy': 'fa-user-secret',
        'settings': 'fa-cog',
        'configuration': 'fa-wrench',
        'support': 'fa-headset',
        'help': 'fa-question-circle',
        'information': 'fa-info-circle',
        'warning': 'fa-exclamation-triangle',
        'danger': 'fa-skull-crossbones',
        'alert': 'fa-bell',
        'favorite': 'fa-star',
        'bookmarks': 'fa-bookmark',
        'archive': 'fa-archive',
        'documents': 'fa-folder',
        'report': 'fa-file-alt',
        'chart': 'fa-chart-bar',
        'stats': 'fa-chart-pie',
        'growth': 'fa-chart-line',
        'loss': 'fa-chart-area',
        'computer': 'fa-desktop',
        'mobile': 'fa-mobile-alt',
        'tablet': 'fa-tablet-alt',
        'code': 'fa-code',
        'programming': 'fa-terminal',
        'development': 'fa-code-branch',
        'design': 'fa-pencil-ruler',
        'interface': 'fa-object-group',
        'database': 'fa-database',
        'server': 'fa-server',
        'cloud': 'fa-cloud',
        'backup': 'fa-cloud-upload-alt',
        'download': 'fa-cloud-download-alt',
        'upload': 'fa-upload',
        'link': 'fa-link',
        'connection': 'fa-link',
        'wifi': 'fa-wifi',
        'bluetooth': 'fa-bluetooth',
        'wireless': 'fa-broadcast-tower',
        'browser': 'fa-globe',
        'search': 'fa-search',
        'explore': 'fa-search-location',
        'location': 'fa-map-marker-alt',
        'gps': 'fa-map-signs',
        'directions': 'fa-compass',
        'compass': 'fa-compass',
        'compass-rose': 'fa-location-arrow',
        'hospital': 'fa-hospital',
        'medicine': 'fa-prescription-bottle',
        'pharmacy': 'fa-pills',
        'treatment': 'fa-band-aid',
        'first aid': 'fa-briefcase-medical',
        'mental health': 'fa-brain',
        'fitness': 'fa-dumbbell',
        'gym': 'fa-weight-hanging',
        'meditation': 'fa-om',
        'yoga': 'fa-spa',
        'diet': 'fa-apple-alt',
        'nutrition': 'fa-lemon',
        'hydration': 'fa-water',
        'productivity': 'fa-tasks',
        'efficiency': 'fa-rocket',
        'schedule': 'fa-calendar-check',
        'goals': 'fa-bullseye',
        'target': 'fa-crosshairs',
        'success': 'fa-trophy',
        'motivation': 'fa-thumbs-up',
        'creativity': 'fa-lightbulb',
        'innovation': 'fa-lightbulb',
        'idea': 'fa-lightbulb',
        'brainstorm': 'fa-brain',
        'startup': 'fa-rocket',
        'business': 'fa-briefcase',
        'company': 'fa-building',
        'corporate': 'fa-building',
        'legal': 'fa-gavel',
        'court': 'fa-balance-scale',
        'contract': 'fa-file-signature',
        'agreement': 'fa-handshake',
        'policy': 'fa-file-contract',
        'insurance': 'fa-shield-alt',
        'certificate': 'fa-certificate',
        'license': 'fa-id-card',
        'key': 'fa-key',
        'password': 'fa-key',
        'security': 'fa-shield-alt',
        'protection': 'fa-shield-alt',
        'firewall': 'fa-shield-virus',
        'virus': 'fa-virus',
        'data': 'fa-database',
        'privacy': 'fa-user-shield',
        'identity': 'fa-id-badge',
        'account': 'fa-user-circle',
        'profile': 'fa-user-circle',
        'avatar': 'fa-user-circle',
        'photo': 'fa-camera',
        'picture': 'fa-image',
        'gallery': 'fa-images',
        'video': 'fa-video',
        'recording': 'fa-video',
        'music': 'fa-music',
        'audio': 'fa-headphones',
        'podcast': 'fa-podcast',
        'radio': 'fa-broadcast-tower',
        'television': 'fa-tv',
        'movie': 'fa-film',
        'cinema': 'fa-film',
        'theater': 'fa-theater-masks',
        'entertainment': 'fa-laugh',
        'fun': 'fa-smile',
        'jokes': 'fa-grin-squint',
        'games': 'fa-gamepad',
        'sports': 'fa-football-ball',
        'soccer': 'fa-futbol',
        'basketball': 'fa-basketball-ball',
        'baseball': 'fa-baseball-ball',
        'football': 'fa-football-ball',
        'tennis': 'fa-table-tennis',
        'golf': 'fa-golf-ball',
        'swimming': 'fa-swimmer',
        'running': 'fa-running',
        'cycling': 'fa-biking',
        'hiking': 'fa-hiking',
        'camping': 'fa-campground',
        'nature': 'fa-tree',
        'outdoor': 'fa-campground',
        'environment': 'fa-leaf',
        'sustainability': 'fa-seedling',
        'energy': 'fa-bolt',
        'recycle': 'fa-recycle',
        'pollution': 'fa-smog',
        'climate': 'fa-temperature-high',
        'weather': 'fa-cloud-sun',
        'sun': 'fa-sun',
        'moon': 'fa-moon',
        'stars': 'fa-star',
        'space': 'fa-space-shuttle',
        'science': 'fa-flask',
        'biology': 'fa-dna',
        'chemistry': 'fa-vial',
        'physics': 'fa-atom',
        'research': 'fa-search',
        'experiment': 'fa-vials',
        'laboratory': 'fa-microscope',
        'engineering': 'fa-cogs',
        'technology': 'fa-microchip',
        'robotics': 'fa-robot',
        'artificial intelligence': 'fa-brain',
        'machine learning': 'fa-brain',
        'programming': 'fa-code',
        'software': 'fa-laptop-code',
        'hardware': 'fa-microchip',
        'internet': 'fa-globe',
        'network': 'fa-network-wired',
        'website': 'fa-globe',
        'domain': 'fa-globe',
        'server': 'fa-server',
        'cloud': 'fa-cloud',
        'database': 'fa-database',
        'api': 'fa-code',
        'developer': 'fa-laptop-code',
        'coding': 'fa-code',
        'script': 'fa-file-code',
        'app': 'fa-mobile-alt',
        'mobile': 'fa-mobile-alt',
        'desktop': 'fa-desktop',
        'application': 'fa-laptop',
        'project': 'fa-folder-open',
        'repository': 'fa-folder-open',
        'version control': 'fa-code-branch',
        'documentation': 'fa-book',
        'tutorial': 'fa-chalkboard-teacher',
        'learning': 'fa-chalkboard',
        'education': 'fa-school',
        'training': 'fa-chalkboard-teacher',
        'skills': 'fa-tools',
        'job': 'fa-briefcase',
        'career': 'fa-briefcase',
        'employment': 'fa-briefcase',
        'salary': 'fa-money-bill',
        'promotion': 'fa-trophy',
        'recognition': 'fa-award',
        'reward': 'fa-award',
        'bonus': 'fa-award',
        'gift': 'fa-gift',
        'party': 'fa-glass-cheers',
        'celebration': 'fa-birthday-cake',
        'anniversary': 'fa-birthday-cake',
        'festival': 'fa-theater-masks',
        'holiday': 'fa-umbrella-beach',
        'vacation': 'fa-umbrella-beach',
        'weekend': 'fa-umbrella-beach',
        'rest': 'fa-bed',
        'relax': 'fa-spa',
        'hobby': 'fa-futbol',
        'craft': 'fa-paint-brush',
        'diy': 'fa-hammer',
        'handmade': 'fa-paint-brush',
        'arts': 'fa-palette',
        'crafts': 'fa-paint-brush',
        'photography': 'fa-camera',
        'drawing': 'fa-pencil-alt',
        'painting': 'fa-palette',
        'sculpture': 'fa-monument',
        'design': 'fa-pencil-ruler',
        'fashion': 'fa-tshirt',
        'beauty': 'fa-heart',
        'cosmetics': 'fa-lipstick',
        'jewelry': 'fa-ring',
        'accessories': 'fa-suitcase',
        'watch': 'fa-clock',
        'time': 'fa-clock',
        'schedule': 'fa-calendar-alt',
        'calendar': 'fa-calendar-alt',
        'reminder': 'fa-bell',
        'notification': 'fa-bell',
        'alert': 'fa-bell',
        'emergency': 'fa-ambulance',
        'hospital': 'fa-hospital',
        'health': 'fa-heartbeat',
        'doctor': 'fa-stethoscope',
        'medication': 'fa-pills',
        'treatment': 'fa-prescription',
        'surgery': 'fa-user-md',
        'therapy': 'fa-user-nurse',
        'recovery': 'fa-notes-medical',
        'wellness': 'fa-smile',
        'mental health': 'fa-brain',
        'nutrition': 'fa-utensils',
        'diet': 'fa-apple-alt',
        'exercise': 'fa-running',
        'fitness': 'fa-dumbbell',
        'workout': 'fa-dumbbell',
        'sports': 'fa-basketball-ball',
        'game': 'fa-gamepad',
        'score': 'fa-trophy',
        'victory': 'fa-medal',
        'defeat': 'fa-sad-cry',
        'win': 'fa-trophy',
        'loss': 'fa-chart-line',
        'failure': 'fa-thumbs-down',
        'success': 'fa-thumbs-up',
        'achievement': 'fa-award',
        'goal': 'fa-bullseye',
        'mission': 'fa-bullseye',
        'vision': 'fa-eye',
        'plan': 'fa-clipboard',
        'strategy': 'fa-chess',
        'tactics': 'fa-chess-knight',
        'operations': 'fa-cogs',
        'logistics': 'fa-truck',
        'supply': 'fa-box',
        'inventory': 'fa-boxes',
        'stock': 'fa-boxes',
        'warehouse': 'fa-warehouse',
        'delivery': 'fa-truck',
        'shipping': 'fa-truck',
        'order': 'fa-box-open',
        'customer': 'fa-user',
        'client': 'fa-user-tie',
        'service': 'fa-headset',
        'support': 'fa-headset',
        'assistance': 'fa-hands-helping',
        'guidance': 'fa-compass',
        'direction': 'fa-compass',
        'advice': 'fa-comments',
        'feedback': 'fa-comments',
        'review': 'fa-star',
        'rating': 'fa-star',
        'opinion': 'fa-comment-dots',
        'discussion': 'fa-comments',
        'forum': 'fa-comments',
        'chat': 'fa-comment',
        'message': 'fa-envelope',
        'email': 'fa-envelope',
        'letter': 'fa-envelope',
        'post': 'fa-mail-bulk',
        'comment': 'fa-comment',
        'conversation': 'fa-comments',
        'communication': 'fa-comments',
        'contact': 'fa-address-book',
        'phone': 'fa-phone',
        'call': 'fa-phone-alt',
        'mobile': 'fa-mobile-alt',
        'sms': 'fa-sms',
        'text': 'fa-sms',
        'notification': 'fa-bell',
        'alert': 'fa-exclamation-triangle',
        'warning': 'fa-exclamation-triangle',
        'caution': 'fa-exclamation-circle',
        'danger': 'fa-skull-crossbones',
        'hazard': 'fa-exclamation-circle',
        'safety': 'fa-shield-alt',
        'security': 'fa-shield-alt',
        'protection': 'fa-shield-virus',
        'prevention': 'fa-shield-virus',
        'virus': 'fa-virus',
        'pandemic': 'fa-virus',
        'healthcare': 'fa-notes-medical',
        'medicine': 'fa-notes-medical',
        'treatment': 'fa-hospital-user',
        'diagnosis': 'fa-diagnoses',
        'prescription': 'fa-prescription',
        'medication': 'fa-pills',
        'pharmacy': 'fa-prescription-bottle-alt',
        'hospital': 'fa-hospital',
        'emergency': 'fa-ambulance',
        'first aid': 'fa-briefcase-medical',
        'ambulance': 'fa-ambulance',
        'doctor': 'fa-user-md',
        'nurse': 'fa-user-nurse',
        'patient': 'fa-procedures',
        'recovery': 'fa-notes-medical',
        'therapy': 'fa-user-md',
        'rehabilitation': 'fa-user-md',
        'mental health': 'fa-brain',
        'psychology': 'fa-brain',
        'stress': 'fa-brain',
        'anxiety': 'fa-brain',
        'depression': 'fa-brain',
        'therapy': 'fa-user-md',
        'counseling': 'fa-comments',
        'nutrition': 'fa-apple-alt',
        'diet': 'fa-apple-alt',
        'hydration': 'fa-water',
        'exercise': 'fa-running',
        'fitness': 'fa-dumbbell',
        'workout': 'fa-dumbbell',
        'sports': 'fa-basketball-ball',
        'hiking': 'fa-hiking',
        'camping': 'fa-campground',
        'outdoors': 'fa-campground',
        'nature': 'fa-tree',
        'environment': 'fa-leaf',
        'sustainability': 'fa-seedling',
        'energy': 'fa-bolt',
        'recycling': 'fa-recycle',
        'pollution': 'fa-smog',
        'climate': 'fa-temperature-high',
        'weather': 'fa-cloud-sun',
        'sun': 'fa-sun',
        'moon': 'fa-moon',
        'stars': 'fa-star',
        'space': 'fa-space-shuttle',
        'universe': 'fa-space-shuttle',
        'galaxy': 'fa-space-shuttle',
        'planet': 'fa-globe',
        'science': 'fa-flask',
        'physics': 'fa-atom',
        'chemistry': 'fa-vial',
        'biology': 'fa-dna',
        'experiment': 'fa-vials',
        'research': 'fa-search',
        'laboratory': 'fa-microscope',
        'engineering': 'fa-cogs',
        'technology': 'fa-microchip',
        'robotics': 'fa-robot',
        'programming': 'fa-code',
        'coding': 'fa-code',
        'software': 'fa-laptop-code',
        'application': 'fa-laptop-code',
        'developer': 'fa-laptop-code',
        'api': 'fa-code',
        'internet': 'fa-globe',
        'website': 'fa-globe',
        'network': 'fa-network-wired',
        'server': 'fa-server',
        'database': 'fa-database',
        'cloud': 'fa-cloud',
        'app': 'fa-mobile-alt',
        'mobile': 'fa-mobile-alt',
        'desktop': 'fa-desktop',
        'project': 'fa-folder-open',
        'repository': 'fa-folder-open',
        'version control': 'fa-code-branch',
        'git': 'fa-code-branch',
        'repository': 'fa-folder-open',
        'documentation': 'fa-book',
        'tutorial': 'fa-chalkboard-teacher',
        'education': 'fa-school',
        'learning': 'fa-chalkboard',
        'teaching': 'fa-chalkboard-teacher',
        'training': 'fa-chalkboard-teacher',
        'presentation': 'fa-chalkboard',
        'conference': 'fa-chalkboard',
        'workshop': 'fa-chalkboard-teacher',
        'skills': 'fa-tools',
        'talent': 'fa-star',
        'job': 'fa-briefcase',
        'career': 'fa-briefcase',
        'employment': 'fa-briefcase',
        'freelance': 'fa-user',
        'contract': 'fa-file-signature',
        'salary': 'fa-money-bill',
        'bonus': 'fa-gift',
        'reward': 'fa-gift',
        'incentive': 'fa-gift',
        'promotion': 'fa-trophy',
        'achievement': 'fa-trophy',
        'recognition': 'fa-award',
        'award': 'fa-award',
        'certificate': 'fa-award',
        'gift': 'fa-gift',
        'party': 'fa-glass-cheers',
        'celebration': 'fa-glass-cheers',
        'anniversary': 'fa-birthday-cake',
        'festival': 'fa-theater-masks',
        'holiday': 'fa-umbrella-beach',
        'vacation': 'fa-umbrella-beach',
        'weekend': 'fa-umbrella-beach',
        'travel': 'fa-plane',
        'flight': 'fa-plane',
        'hotel': 'fa-hotel',
        'accommodation': 'fa-bed',
        'booking': 'fa-calendar-check',
        'reservation': 'fa-calendar-check',
        'itinerary': 'fa-map',
        'tour': 'fa-map',
        'adventure': 'fa-hiking',
        'sightseeing': 'fa-binoculars',
        'exploration': 'fa-compass',
        'trip': 'fa-road',
        'journey': 'fa-road',
        'destination': 'fa-map-pin',
        'route': 'fa-route',
        'transportation': 'fa-car',
        'vehicle': 'fa-car',
        'car': 'fa-car',
        'bike': 'fa-bicycle',
        'bicycle': 'fa-bicycle',
        'scooter': 'fa-motorcycle',
        'motorcycle': 'fa-motorcycle',
        'bus': 'fa-bus',
        'train': 'fa-train',
        'subway': 'fa-subway',
        'tram': 'fa-tram',
        'airport': 'fa-plane-departure',
        'station': 'fa-subway',
        'harbor': 'fa-anchor',
        'dock': 'fa-anchor',
        'port': 'fa-anchor',
        'bridge': 'fa-road',
        'road': 'fa-road',
        'highway': 'fa-road',
        'street': 'fa-road',
        'lane': 'fa-road',
        'path': 'fa-road',
        'trail': 'fa-hiking',
        'sidewalk': 'fa-road',
        'intersection': 'fa-road',
        'crossroad': 'fa-road',
        'junction': 'fa-road',
        'roundabout': 'fa-circle',
        'traffic': 'fa-traffic-light',
        'stop': 'fa-hand-paper',
        'yield': 'fa-hand-paper',
        'go': 'fa-thumbs-up',
        'fast': 'fa-tachometer-alt',
        'speed': 'fa-tachometer-alt',
        'slow': 'fa-tachometer-alt',
        'delay': 'fa-clock',
        'wait': 'fa-clock',
        'on time': 'fa-check-circle',
        'early': 'fa-clock',
        'late': 'fa-clock',
        'departure': 'fa-plane-departure',
        'arrival': 'fa-plane-arrival',
        'terminal': 'fa-plane',
        'gate': 'fa-plane',
        'luggage': 'fa-suitcase',
        'baggage': 'fa-suitcase',
        'security': 'fa-shield-alt',
        'customs': 'fa-user-shield',
        'immigration': 'fa-passport',
        'visa': 'fa-passport',
        'passport': 'fa-passport',
        'ticket': 'fa-ticket-alt',
        'boarding pass': 'fa-ticket-alt',
        'check-in': 'fa-laptop-house',
        'lobby': 'fa-hotel',
        'lounge': 'fa-cocktail',
        'restaurant': 'fa-utensils',
        'cafe': 'fa-coffee',
        'bar': 'fa-wine-glass-alt',
        'food': 'fa-utensils',
        'drink': 'fa-glass-cheers',
        'meal': 'fa-utensils',
        'breakfast': 'fa-bacon',
        'lunch': 'fa-utensils',
        'dinner': 'fa-utensils',
        'snack': 'fa-cookie',
        'dessert': 'fa-ice-cream',
        'appetizer': 'fa-utensils',
        'menu': 'fa-utensils',
        'dish': 'fa-utensils',
        'cuisine': 'fa-utensils',
        'recipe': 'fa-utensils',
        'cooking': 'fa-utensils',
        'baking': 'fa-cookie',
        'grilling': 'fa-utensils',
        'bbq': 'fa-utensils',
        'vegetarian': 'fa-carrot',
        'vegan': 'fa-seedling',
        'organic': 'fa-leaf',
        'gluten-free': 'fa-cookie',
        'diet': 'fa-apple-alt',
        'nutrition': 'fa-apple-alt',
        'health': 'fa-heart',
        'exercise': 'fa-running',
        'fitness': 'fa-dumbbell',
        'sports': 'fa-basketball-ball',
        'athletics': 'fa-running',
        'team': 'fa-users',
        'league': 'fa-users',
        'match': 'fa-users',
        'tournament': 'fa-users',
        'game': 'fa-gamepad',
        'score': 'fa-trophy',
        'win': 'fa-trophy',
        'loss': 'fa-sad-cry',
        'draw': 'fa-balance-scale',
        'tie': 'fa-balance-scale',
        'victory': 'fa-trophy',
        'championship': 'fa-trophy',
        'final': 'fa-trophy',
        'cup': 'fa-trophy',
        'medal': 'fa-medal',
        'trophy': 'fa-trophy',
        'champion': 'fa-trophy',
        'runner-up': 'fa-medal',
        'player': 'fa-user',
        'athlete': 'fa-user',
        'coach': 'fa-user-tie',
        'referee': 'fa-user',
        'umpire': 'fa-user',
        'team': 'fa-users',
        'group': 'fa-users',
        'club': 'fa-users',
        'association': 'fa-users',
        'organization': 'fa-building',
        'business': 'fa-briefcase',
        'company': 'fa-building',
        'corporation': 'fa-building',
        'enterprise': 'fa-building',
        'firm': 'fa-building',
        'brand': 'fa-tag',
        'product': 'fa-box',
        'service': 'fa-concierge-bell',
        }
    title_lower = title.lower()
    for keyword,icon in keyword_to_icon.items():
        if title_lower==keyword:
            return icon
    return default_icon