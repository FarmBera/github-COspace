# %%
from faker import Faker

# %%
faker = Faker('ko-KR')

name = faker.name()
job = faker.job()
address = faker.address()

# %%
print(name, job, address)
print(f'name: {name}, job: {job}, address: {address}')
