from django.db import models
from django.contrib.auth.models import User

# current choices for the category of the items that the user is selling (both men and womens)
CATEGORY_CHOICES = (
    ("Footwear", "Footwear"),
    ("Tops", "Tops"),
    ("Bottoms", "Bottoms"),
    ("Accessories", "Accessories")
)

# choices for the condition of the items (both men and womens)
CONDITION_CHOICES = (
    ("Mint", "Mint"),
    ("Good", "Good"),
    ("Fair", "Fair"),
    ("Character Flawed", "Character Flawed")
)

# size choices for the sizes of tops (both men and womens)
TOP_CHOICES = (
    ("XS", "XS"),
    ("S", "S"),
    ("M", "M"),
    ("L", "L"),
    ("XL", "L"),
    ("XXL", "XXL"),
    ("OTHER", "OTHER")
)

# size choices for the sizes of bottoms (both men and womens)
BOTTOM_CHOICES = (
    ("XS", "XS"),
    ("S", "S"),
    ("M", "M"),
    ("L", "L"),
    ("XL", "L"),
    ("XXL", "XXL"),
    ("OTHER", "OTHER")
)

# size choices for the shoes (both men and womens)
SHOE_CHOICES = (
	('4','4'),
	('5','5'),
	('6','6'),
	('7','7'),
	('8','8'),
	('9','9'),
	('10','10'),
	('11','11'),
	('12','12'),
	('13','13'),
	('14','14'),
	('15','15'),
	('16','16'),
)

# Create your models here.

# Item refers to the item that you are selling.  When you create an item, you will need to select a category, select the appropriate sizes and fill out the remainder of the form.

class Item(models.Model):
    category = models.CharField (
        max_length = 100,
        choices = CATEGORY_CHOICES,
        default = "Footwear"
    )
    title = models.CharField(max_length = 200)
    image = models.FileField(upload_to='images/', null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField (
        max_length = 100,
        choices = CONDITION_CHOICES,
        default = "Mint"
    )
    top_size = models.CharField (
        max_length = 100,
        choices = TOP_CHOICES,
        default = "M"
    )
    bottom_size = models.CharField (
        max_length = 100,
        choices = BOTTOM_CHOICES,
        default = "M"
    )
    shoe_size = models.CharField (
        max_length = 100,
        choices = SHOE_CHOICES,
        default = "10"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.title