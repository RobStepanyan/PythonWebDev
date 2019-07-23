from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    
    MAKES = (('', 'Select'), ('9ff', '9ff'), ('abarth', 'Abarth'), ('ac', 'AC'), ('acm', 'ACM'), ('acura', 'Acura'), ('aixam', 'Aixam'), 
            ('alfa_romeo', 'Alfa Romeo'), ('alpina', 'Alpina'), ('alpine', 'Alpine'), ('amphicar', 'Amphicar'), 
            ('ariel_motor', 'Ariel Motor'), ('artega', 'Artega'), ('asp', 'Asp'), ('aston_martin', 'Aston Martin'), 
            ('austin', 'Austin'), ('autobianchi', 'Autobianchi'), ('auverland', 'Auverland'), ('baic', 'Baic'), 
            ('bedford', 'Bedford'), ('bellier', 'Bellier'), ('bentley', 'Bentley'), ('bolloré', 'Bolloré'), 
            ('borgward', 'Borgward'), ('brilliance', 'Brilliance'), ('bugatti', 'Bugatti'), ('buick', 'Buick'), 
            ('byd', 'BYD'), ('cadillac', 'Cadillac'), ('caravans-wohnm', 'Caravans-Wohnm'), ('casalini', 'Casalini'), 
            ('caterham', 'Caterham'), ('changhe', 'Changhe'), ('chatenet', 'Chatenet'), ('chery', 'Chery'), ('chevrolet', 'Chevrolet'), 
            ('chrysler', 'Chrysler'), ('citroen', 'Citroen'), ('cityel', 'CityEL'), ('cmc', 'CMC'), ('corvette', 'Corvette'), 
            ('courb', 'Courb'), ('cupra', 'Cupra'), ('dacia', 'Dacia'), ('daewoo', 'Daewoo'), ('daf', 'DAF'), ('daihatsu', 'Daihatsu'), 
            ('daimler', 'Daimler'), ('dangel', 'Dangel'), ('de_la_chapelle', 'De la Chapelle'), ('de_tomaso', 'De Tomaso'), 
            ('derways', 'Derways'), ('dfsk', 'DFSK'), ('dodge', 'Dodge'), ('donkervoort', 'Donkervoort'), ('dr_motor', 'DR Motor'), 
            ('ds_automobiles', 'DS Automobiles'), ('dutton', 'Dutton'), ('e.go', 'e.GO'), ('estrima', 'Estrima'), ('ferrari', 'Ferrari'), 
            ('fiat', 'Fiat'), ('fisker', 'FISKER'), ('gac_gonow', 'Gac Gonow'), ('galloper', 'Galloper'), ('gaz', 'GAZ'), ('geely', 'Geely'), 
            ('gem', 'GEM'), ('gemballa', 'GEMBALLA'), ('genesis', 'Genesis'), ('gillet', 'Gillet'), ('giotti_victoria', 'Giotti Victoria'), 
            ('gmc', 'GMC'), ('goupil', 'Goupil'), ('great_wall', 'Great Wall'), ('grecav', 'Grecav'), ('haima', 'Haima'), ('hamann', 'Hamann'), 
            ('honda', 'Honda'), ('hummer', 'HUMMER'), ('hurtan', 'Hurtan'), ('hyundai', 'Hyundai'), ('infiniti', 'Infiniti'), 
            ('innocenti', 'Innocenti'), ('iso_rivolta', 'Iso Rivolta'), ('isuzu', 'Isuzu'), ('iveco', 'Iveco'), ('izh', 'IZH'), 
            ('jaguar', 'Jaguar'), ('jeep', 'Jeep'), ('karabag', 'Karabag'), ('kia', 'Kia'), ('koenigsegg', 'Koenigsegg'), ('ktm', 'KTM'), 
            ('lada', 'Lada'), ('lamborghini', 'Lamborghini'), ('lancia', 'Lancia'), ('land_rover', 'Land Rover'), ('ldv', 'LDV'), 
            ('lexus', 'Lexus'), ('lifan', 'Lifan'), ('ligier', 'Ligier'), ('lincoln', 'Lincoln'), ('lotus', 'Lotus'), ('mahindra', 'Mahindra'), 
            ('man', 'MAN'), ('mansory', 'Mansory'), ('martin_motors', 'Martin Motors'), ('maserati', 'Maserati'), ('maxus', 'Maxus'), 
            ('maybach', 'Maybach'), ('mazda', 'Mazda'), ('mclaren', 'McLaren'), ('melex', 'Melex'), ('mg', 'MG'), ('microcar', 'Microcar'), 
            ('minauto', 'Minauto'), ('mini', 'MINI'), ('mitsubishi', 'Mitsubishi'), ('mitsuoka', 'Mitsuoka'), ('morgan', 'Morgan'), 
            ('moskvich', 'Moskvich'), ('mp_lafer', 'MP Lafer'), ('mpm_motors', 'MPM Motors'), ('nio', 'Nio'), ('nissan', 'Nissan'), 
            ('oldsmobile', 'Oldsmobile'), ('oldtimer', 'Oldtimer'), ('pagani', 'Pagani'), ('panther_westwinds', 'Panther Westwinds'), 
            ('peugeot', 'Peugeot'), ('pgo', 'PGO'), ('piaggio', 'Piaggio'), ('plymouth', 'Plymouth'), ('pontiac', 'Pontiac'), 
            ('porsche', 'Porsche'), ('proton', 'Proton'), ('puch', 'Puch'), ('qoros', 'Qoros'), ('qvale', 'Qvale'), ('ram', 'RAM'), 
            ('regis', 'Regis'), ('reliant', 'Reliant'), ('rolls-royce', 'Rolls-Royce'), ('rover', 'Rover'), ('ruf', 'Ruf'), ('saab', 'Saab'), 
            ('santana', 'Santana'), ('savel', 'Savel'), ('sdg', 'SDG'), ('seat', 'SEAT'), ('shuanghuan', 'Shuanghuan'), ('skoda', 'Skoda'), 
            ('smart', 'smart'), ('speedart', 'SpeedArt'), ('spyker', 'Spyker'), ('ssangyong', 'SsangYong'), ('streetscooter', 'StreetScooter'), 
            ('subaru', 'Subaru'), ('suzuki', 'Suzuki'), ('tagaz', 'TagAZ'), ('talbot', 'Talbot'), ('tasso', 'Tasso'), ('tata', 'Tata'), 
            ('tazzari_ev', 'Tazzari EV'), ('techart', 'TECHART'), ('tesla', 'Tesla'), ('town_life', 'Town Life'), ('toyota', 'Toyota'), 
            ('trabant', 'Trabant'), ('trailer-anhänger', 'Trailer-Anhänger'), ('triumph', 'Triumph'), ('trucks-lkw', 'Trucks-Lkw'), 
            ('tvr', 'TVR'), ('uaz', 'UAZ'), ('vanderhall', 'Vanderhall'), ('vaz', 'VAZ'), ('vem', 'VEM'), ('volvo', 'Volvo'), 
            ('vortex', 'Vortex'), ('wallys', 'Wallys'), ('wartburg', 'Wartburg'), ('westfield', 'Westfield'), ('wiesmann', 'Wiesmann'), 
            ('zastava', 'Zastava'), ('zaz', 'ZAZ'), ('zhidou', 'Zhidou'), ('zotye', 'Zotye'), ('others', 'Others'))

    YEAR = [str(x) for x in range(timezone.now().year, 1910, -1)]
    YEAR = tuple(zip(YEAR, YEAR))

    SEATS = [str(x) for x in range(1, 301)]
    SEATS = tuple(zip(SEATS, SEATS))

    DOORS = [str(x) for x in range(1, 8)]
    DOORS = tuple(zip(DOORS, DOORS))

    TRANSMISSION_TYPE = (('M', 'Manual'), ('A', 'Automatic'), ('SA', 'Semi-Automatic'))

    PRICE = ['$' + str(x) for x in range(1000, 4000000, 1000)]
    PRICE = tuple(zip(PRICE, PRICE))
    
    make = models.CharField(choices = MAKES, max_length=18)
    model = models.CharField(max_length=60)
    
    @property
    def title(self):
        return self.make + ' ' + self.model

    image = models.FileField(null=True, blank=True)
    year = models.CharField(choices=YEAR, max_length=4)
    color = models.CharField(max_length=20)
    seats = models.CharField(choices = SEATS, max_length = 3)
    doors = models.CharField(choices=DOORS, max_length=1)
    transmission_type = models.CharField(max_length = 2, choices=TRANSMISSION_TYPE)
    configuration = models.CharField(max_length=30)
    price = models.CharField(choices=PRICE, max_length=7)
    description = models.TextField(max_length = 1024)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
