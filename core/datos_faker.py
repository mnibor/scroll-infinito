from faker import Faker
from core.models import Post
faker = Faker()
[Post.objects.create(title=faker.sentence(), description=faker.sentence(),image=f"https://picsum.photos/id/{i+1}/300/200")for i in range(600)]