from faker import Faker

fake = Faker()

uid = fake.uuid4()
name = fake.name()
tz = fake.timezone()
day = fake.day_of_month()
month = fake.month_name()
year = 2020
time = fake.time()


start_time = fake.date_time_this_month()
end_time = fake.date_time_this_month()

print(start_time)
print(end_time)

if start_time > end_time:
    print(True)
else:
    print(False)