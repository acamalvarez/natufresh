import csv

from accounts.models import Product, Tag

def run():
    fhand = open('static/products.csv')
    reader = csv.reader(fhand)
    next(reader)

    Product.objects.all().delete()
    Tag.objects.all().delete()

    for row in reader:

        try:
            id=row[0]
            name = row[1]
            category = row[2]
            tag = row[3]
            price = float(row[4])
            description = row[5]
            picture = row[6]
        except:
            id = None
            name = None
            category = None
            tag = None
            price = None
            description = None
            picture = None

        tag = Tag.objects.get_or_create(name=row[3])

        product, created = Product.objects.get_or_create(id=id,
            name=name, price=price, category=category, 
            description=description, product_pic=picture)

        product.tags.add(tag)
        
        product.save()


# For updating the product list run the following script
# python manage.py runscript product_load